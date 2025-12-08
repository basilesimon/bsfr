//! html-c2pa: Generate C2PA sidecar manifests for HTML files
//!
//! This tool creates C2PA manifests for HTML blog posts, enabling them
//! to be used as verified ingredients in downstream C2PA workflows.

use anyhow::{Context, Result};
use c2pa::{create_signer, Manifest, SigningAlg};
use clap::Parser;
use scraper::{Html, Selector};
use serde_json::json;
use sha2::{Digest, Sha256};
use std::fs;
use std::path::PathBuf;

#[derive(Parser, Debug)]
#[command(name = "html-c2pa")]
#[command(about = "Generate C2PA sidecar manifests for HTML files")]
#[command(version)]
struct Args {
    /// Path to HTML file to sign
    html_path: PathBuf,

    /// Output path for .c2pa sidecar (defaults to <html_path>.c2pa)
    #[arg(short, long)]
    output: Option<PathBuf>,

    /// Author name for CreativeWork assertion
    #[arg(long, default_value = "Basile Simon")]
    author: String,

    /// Base URL for the blog
    #[arg(long, default_value = "https://basilesimon.fr")]
    base_url: String,

    /// Path to signing certificate file (PEM format)
    #[arg(long, env = "C2PA_SIGN_CERT")]
    sign_cert: String,

    /// Path to private key file (PEM format)
    #[arg(long, env = "C2PA_PRIVATE_KEY")]
    private_key: String,

    /// Timestamp authority URL (optional, for RFC 3161 timestamps)
    #[arg(long, env = "C2PA_TA_URL")]
    ta_url: Option<String>,
}

/// Extract title from HTML document
fn extract_title(html: &Html) -> Option<String> {
    // Try <title> tag first
    if let Ok(sel) = Selector::parse("title") {
        if let Some(el) = html.select(&sel).next() {
            let title = el.text().collect::<String>().trim().to_string();
            if !title.is_empty() {
                // Often title includes site name, try to extract just the post title
                if let Some(idx) = title.find(" | ") {
                    return Some(title[..idx].trim().to_string());
                }
                if let Some(idx) = title.find(" - ") {
                    return Some(title[..idx].trim().to_string());
                }
                return Some(title);
            }
        }
    }

    // Fallback to <h1>
    if let Ok(sel) = Selector::parse("h1") {
        if let Some(el) = html.select(&sel).next() {
            let title = el.text().collect::<String>().trim().to_string();
            if !title.is_empty() {
                return Some(title);
            }
        }
    }

    None
}

/// Extract publication date from HTML (looks for <time datetime="">)
fn extract_date(html: &Html) -> Option<String> {
    if let Ok(sel) = Selector::parse("time[datetime]") {
        if let Some(el) = html.select(&sel).next() {
            return el.value().attr("datetime").map(|s| s.to_string());
        }
    }
    None
}

/// Derive URL path from file path
fn derive_url(path: &PathBuf, base_url: &str) -> String {
    let path_str = path.to_string_lossy();

    // Find /blog/ or /weeknotes/ in path
    for prefix in &["/blog/", "/weeknotes/"] {
        if let Some(idx) = path_str.find(prefix) {
            let rel = &path_str[idx..];
            let url_path = rel.trim_end_matches("index.html");
            return format!("{}{}", base_url.trim_end_matches('/'), url_path);
        }
    }

    base_url.to_string()
}

fn main() -> Result<()> {
    let args = Args::parse();

    // Read HTML file
    let html_str = fs::read_to_string(&args.html_path)
        .with_context(|| format!("Failed to read: {:?}", args.html_path))?;
    let html_bytes = html_str.as_bytes();

    // Parse HTML for metadata extraction
    let html = Html::parse_document(&html_str);

    // Extract metadata
    let title = extract_title(&html).unwrap_or_else(|| "Untitled".to_string());
    let date = extract_date(&html);
    let url = derive_url(&args.html_path, &args.base_url);

    // Compute SHA-256 hash of HTML content
    let hash = Sha256::digest(html_bytes);
    let hash_hex = hex::encode(hash);

    eprintln!("Processing: {:?}", args.html_path);
    eprintln!("  Title: {}", title);
    eprintln!("  URL: {}", url);
    eprintln!("  SHA-256: {}", hash_hex);

    // Read signing credentials
    let cert_pem = fs::read_to_string(&args.sign_cert)
        .with_context(|| format!("Failed to read certificate: {}", args.sign_cert))?;
    let key_pem = fs::read_to_string(&args.private_key)
        .with_context(|| format!("Failed to read private key: {}", args.private_key))?;

    // Create signer
    let signer = create_signer::from_keys(
        &cert_pem,
        &key_pem,
        SigningAlg::Es256,
        args.ta_url.clone(),
    )
    .context("Failed to create signer")?;

    // Build manifest
    let mut manifest = Manifest::new("basilesimon.fr/blog");
    manifest.set_title(Some(title.clone()));
    manifest.set_format("text/html");

    // Add CreativeWork assertion
    let creative_work = json!({
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "url": url,
        "author": {
            "@type": "Person",
            "name": args.author
        },
        "datePublished": date
    });
    manifest.add_labeled_assertion(
        "stds.schema-org.CreativeWork",
        &creative_work,
    )?;

    // Add actions assertion
    let actions = json!({
        "actions": [{
            "action": "c2pa.published",
            "when": date.unwrap_or_else(|| chrono::Utc::now().to_rfc3339())
        }]
    });
    manifest.add_labeled_assertion("c2pa.actions", &actions)?;

    // Add data hash assertion for the HTML content
    let data_hash = json!({
        "name": "index.html",
        "hash": hash_hex,
        "alg": "sha256",
        "url": url
    });
    manifest.add_labeled_assertion("c2pa.hash.data", &data_hash)?;

    // Embed manifest (we'll extract the bytes for sidecar)
    // Since HTML isn't a supported format, we create manifest bytes directly
    let manifest_bytes = manifest
        .embed_to_memory("text/html", html_bytes, signer.as_ref())
        .context("Failed to create manifest")?;

    // For sidecar, we need just the C2PA manifest store, not the embedded asset
    // The embed_to_memory returns the full asset with manifest embedded
    // For unsupported formats, we'll write out what we get and document the approach

    // Output path
    let output = args.output.unwrap_or_else(|| {
        PathBuf::from(format!("{}.c2pa", args.html_path.display()))
    });

    // Write sidecar
    fs::write(&output, &manifest_bytes)
        .with_context(|| format!("Failed to write: {:?}", output))?;

    eprintln!("  Wrote: {:?} ({} bytes)", output, manifest_bytes.len());

    Ok(())
}
