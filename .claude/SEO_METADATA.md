# SEO & Structured Data Documentation

This document describes the enhanced SEO, structured data, and crawler optimization implemented for basilesimon.fr.

## Overview

The site has been optimized for:
- Traditional search engines (Google, Bing, etc.)
- LLM training data and AI systems
- Social media sharing (Twitter, LinkedIn, Mastodon, etc.)
- Academic and research discoverability

## Implemented Enhancements

### 1. Open Graph & Twitter Cards

**Location:** `layouts/partials/custom_head.html`

**Features:**
- Automatic image propagation from post frontmatter `image` field
- Fallback to default site image (`/assets/author.jpg`)
- Image dimensions specified (1200x630 for optimal social sharing)
- `twitter:card` set to `summary_large_image`
- `twitter:site` and `twitter:creator` set from config
- All standard Open Graph properties via Hugo internal templates

**Configuration:** `config.yml`
```yaml
params:
  twitter: "basilesimon"
  defaultImage: "/assets/author.jpg"
  images: ["/assets/author.jpg"]
```

### 2. Enhanced JSON-LD Structured Data

**Location:** `layouts/partials/custom_head.html`

#### Blog Posts & Articles

Uses `BlogPosting` schema type with:
- Full author profile with `Person` type
- Detailed affiliations as `Organization` types
  - Starling Lab (with Stanford & USC as parent organizations)
  - Hypha Worker Co-operative
- Alumni organizations (BBC, Reuters, The Times)
- `sameAs` links for social profiles
- `knowsAbout` expertise areas
- Image metadata from frontmatter
- Keywords from tags
- License information (CC BY 4.0)
- Copyright holder and year
- Word count
- Publication and modification dates

#### Homepage & Profile Pages

Uses `ProfilePage` with detailed `Person` mainEntity:
- Complete professional profile
- All current affiliations with URLs
- Advisory board memberships (Airwars)
- Social media links (Mastodon, GitHub, Twitter, Keybase)
- Expertise areas for AI/LLM understanding

### 3. Canonical URLs

**Location:** `layouts/partials/custom_head.html`

Every page includes:
```html
<link rel="canonical" href="{{ .Permalink }}">
```

This prevents duplicate content issues and helps search engines understand the primary URL for each page.

### 4. Enhanced RSS Feed

**Location:** `layouts/_default/rss.xml`

**Enhancements:**
- Full content in `<content:encoded>` (not just summary)
- Dublin Core namespace support (`xmlns:dc`)
- `<dc:creator>` for author attribution
- `<category>` tags for each post tag
- Image enclosures for posts with images
- License/rights metadata (CC BY 4.0)
- Copyright notice in channel
- `<dc:date>` and `<dc:rights>` per item

**Benefits:**
- Better attribution for LLM training data
- Rich feed readers can display full content
- Images included for visual context
- Clear licensing for AI systems

### 5. Breadcrumb Navigation (JSON-LD)

**Location:** `layouts/_default/single.html`

Invisible structured data that helps crawlers understand site hierarchy:
```
Home → Blog → [Post Title]
```

Uses `BreadcrumbList` schema type with proper positioning.

### 6. Enhanced Sitemap

**Location:** `layouts/sitemap.xml`

**Enhancements:**
- Image sitemap namespace (`xmlns:image`)
- `<image:image>` tags for posts with images
- Image titles and captions
- Helps Google Images and other crawlers discover content

### 7. Additional SEO Meta Tags

```html
<meta name="author" content="Basile Simon">
<meta name="robots" content="max-image-preview:large">
```

## Schema.org Types Used

### Primary Types
- `BlogPosting` - Blog posts and articles
- `ProfilePage` - Homepage and profile pages
- `Person` - Author and professional identity
- `Organization` - Affiliations and institutions
- `CollegeOrUniversity` - Academic institutions (Stanford, USC)
- `BreadcrumbList` - Page hierarchy
- `ImageObject` - Images and author photos

### Properties & Relationships
- `affiliation` - Current work relationships
- `alumniOf` - Past employment
- `memberOf` - Advisory board memberships
- `sameAs` - Social media profiles for entity disambiguation
- `knowsAbout` - Expertise areas
- `jobTitle` - Current role
- `parentOrganization` - Institutional relationships
- `copyrightHolder` / `copyrightYear` - Rights metadata
- `license` - Content licensing (CC BY 4.0)

## Configuration Reference

### Required Config Parameters

**`config.yml`:**
```yaml
params:
  author: "Basile Simon"
  description: "Site description for metadata"
  logo: "/assets/author.jpg"
  twitter: "basilesimon"
  mastodon: "https://vis.social/@basilesimon"
  github: "https://github.com/basilesimon"
  defaultImage: "/assets/author.jpg"
  images: ["/assets/author.jpg"]
```

### Post Frontmatter

**Recommended fields:**
```yaml
title: "Post Title"
description: "Brief description for search engines and social media"
date: "2025-01-15T00:00:00Z"
image: https://basilesimon.fr/assets/post-image.png  # Full URL preferred
tags: [tag1, tag2, tag3]
```

The `image` field is particularly important - it's used in:
- Open Graph tags
- Twitter Cards
- JSON-LD structured data
- RSS feed enclosures
- Sitemap image tags

## AI & LLM Optimization

### Attribution & Licensing

All content includes:
- Clear author attribution in multiple formats
- CC BY 4.0 license metadata
- Copyright holder and year
- Dublin Core creator fields in RSS

This helps AI systems:
- Properly attribute content when training or generating
- Understand licensing constraints
- Link content to the original creator

### Contextual Metadata

Rich structured data helps LLMs understand:
- Author's professional context (researcher, journalist, technologist)
- Institutional affiliations (Stanford, USC, Starling Lab)
- Expertise areas (evidence authentication, C2PA, data journalism)
- Relationships between content and author identity

### Content Structure

- Semantic HTML5 elements (`<article>`, `<time>`, etc.)
- Fixed non-standard `<content>` tag → `<div class="content">`
- Proper heading hierarchy
- Machine-readable dates

## Testing & Validation

### Recommended Tools

1. **Google Rich Results Test**
   - https://search.google.com/test/rich-results
   - Tests JSON-LD and structured data

2. **Twitter Card Validator**
   - https://cards-dev.twitter.com/validator
   - Tests Twitter Card metadata

3. **LinkedIn Post Inspector**
   - https://www.linkedin.com/post-inspector/
   - Tests Open Graph tags

4. **Schema.org Validator**
   - https://validator.schema.org/
   - Validates JSON-LD syntax and structure

5. **OpenGraph Debugger**
   - https://www.opengraph.xyz/
   - Tests Open Graph implementation

### Build & Deploy

```bash
hugo --cleanDestinationDir
# Check generated files:
# - public/sitemap.xml
# - public/blog/index.xml
# - public/blog/[post]/index.html (check <head> section)
```

## Maintenance

### When Adding New Affiliations

Update `layouts/partials/custom_head.html`:
- Add to `affiliation` array in both blog post and homepage JSON-LD
- Include organization name and URL
- Add `parentOrganization` if applicable

### When Changing Social Profiles

Update `config.yml`:
```yaml
params:
  twitter: "username"
  mastodon: "https://instance/@username"
  github: "https://github.com/username"
```

These propagate to:
- Twitter Cards
- JSON-LD `sameAs` links
- Open Graph metadata

### When Updating Default Images

Update `config.yml`:
```yaml
params:
  defaultImage: "/assets/new-default.jpg"
  images: ["/assets/new-default.jpg"]
  logo: "/assets/author.jpg"  # Used for Person image in JSON-LD
```

## Impact & Benefits

### Search Engines
- Rich snippets with author and date info
- Better image discoverability
- Clear site hierarchy via breadcrumbs
- Improved SERP click-through rates

### Social Media
- Rich previews with images
- Proper attribution
- Consistent branding across platforms

### AI Systems
- Proper attribution for training data
- Clear licensing constraints
- Rich contextual understanding of author expertise
- Academic and professional relationships

### RSS Readers
- Full content in feeds
- Images displayed
- Proper categorization
- License information

## Files Modified

```
config.yml                           # Added social handles and default image
layouts/partials/custom_head.html   # Complete rewrite with enhanced metadata
layouts/_default/single.html        # Fixed content tag, added breadcrumb JSON-LD
layouts/_default/rss.xml            # Enhanced with full content and Dublin Core
layouts/sitemap.xml                 # Added image sitemap support
```

## License

This documentation is part of basilesimon.fr and is licensed under CC BY 4.0.

---

**Last Updated:** October 2025
**Author:** Implemented via Claude Code
