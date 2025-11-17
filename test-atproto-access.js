#!/usr/bin/env node

/**
 * BlueSky/ATProto Access Test Script
 *
 * This script verifies your ATProto credentials and fetches your account info.
 *
 * Usage:
 *   1. Install dependencies: npm install @atproto/api
 *   2. Set environment variables:
 *      export BSKY_HANDLE="basilesimon.bsky.social"
 *      export BSKY_APP_PASSWORD="xxxx-xxxx-xxxx-xxxx"
 *   3. Run: node test-atproto-access.js
 */

const { AtpAgent } = require('@atproto/api');

async function testAtProtoAccess() {
  const handle = process.env.BSKY_HANDLE;
  const password = process.env.BSKY_APP_PASSWORD;

  if (!handle || !password) {
    console.error('❌ Missing credentials!');
    console.log('\nPlease set environment variables:');
    console.log('  export BSKY_HANDLE="your-handle.bsky.social"');
    console.log('  export BSKY_APP_PASSWORD="xxxx-xxxx-xxxx-xxxx"');
    process.exit(1);
  }

  try {
    console.log('🔐 Authenticating with ATProto...');
    console.log(`   Handle: ${handle}`);

    const agent = new AtpAgent({
      service: 'https://bsky.social'
    });

    await agent.login({
      identifier: handle,
      password: password
    });

    console.log('✅ Authentication successful!\n');

    // Fetch profile information
    console.log('📊 Fetching account information...');
    const profile = await agent.getProfile({ actor: handle });

    console.log('\n=== Your ATProto Account Details ===');
    console.log(`DID:         ${profile.data.did}`);
    console.log(`Handle:      ${profile.data.handle}`);
    console.log(`Display Name: ${profile.data.displayName || 'Not set'}`);
    console.log(`Followers:   ${profile.data.followersCount || 0}`);
    console.log(`Following:   ${profile.data.followsCount || 0}`);
    console.log(`Posts:       ${profile.data.postsCount || 0}`);

    if (profile.data.description) {
      console.log(`\nBio: ${profile.data.description.substring(0, 100)}${profile.data.description.length > 100 ? '...' : ''}`);
    }

    console.log('\n=== Technical Details ===');
    console.log(`PDS Service: ${agent.service}`);
    console.log(`Session Active: ${agent.session ? 'Yes' : 'No'}`);
    if (agent.session) {
      console.log(`Session DID: ${agent.session.did}`);
    }

    console.log('\n✨ You are ATProto-ready! You can now:');
    console.log('   - Create posts programmatically');
    console.log('   - Upload images and media');
    console.log('   - Read and interact with your timeline');
    console.log('   - Access your PDS data');
    console.log('   - Build automated integrations');

    return profile.data;

  } catch (error) {
    console.error('\n❌ Error:', error.message);

    if (error.message.includes('AuthenticationRequired')) {
      console.log('\n💡 Tip: Check that your app password is correct');
    } else if (error.message.includes('InvalidRequest')) {
      console.log('\n💡 Tip: Verify your handle is correct (should end in .bsky.social)');
    }

    process.exit(1);
  }
}

// Run the test
testAtProtoAccess();
