# BlueSky/ATProto Integration Setup

## Minimum Requirements Checklist

- [x] BlueSky account (you have this!)
- [x] BlueSky handle: `basilesimon.bsky.social`
- [ ] App password (create this now)
- [ ] Test your access

---

## Quick Start (5 minutes)

### Step 1: Create an App Password

1. Visit: https://bsky.app/settings/app-passwords
2. Click **"Add App Password"**
3. Name it: `Blog Integration`
4. **Copy the password immediately** (format: `xxxx-xxxx-xxxx-xxxx`)
5. You won't be able to view it again!

### Step 2: Set Up Credentials

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your app password
nano .env  # or use your preferred editor
```

In `.env`, add your credentials:
```env
BSKY_HANDLE=basilesimon.bsky.social
BSKY_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
```

### Step 3: Install Dependencies

```bash
npm install
```

### Step 4: Test Your Access

```bash
npm run test:atproto
```

You should see output like:
```
✅ Authentication successful!

=== Your ATProto Account Details ===
DID:         did:plc:...
Handle:      basilesimon.bsky.social
Display Name: ...
Followers:   ...
```

---

## What You Get

With these credentials, you can:

- ✅ **Create posts** programmatically via ATProto API
- ✅ **Upload images** and media to your PDS
- ✅ **Read your timeline** and fetch posts
- ✅ **Access your DID** and account information
- ✅ **Build automations** (e.g., RSS-to-BlueSky)

---

## Your ATProto Identity

Your BlueSky account comes with:

1. **Handle**: `basilesimon.bsky.social`
   - Human-readable identifier
   - Can be changed to your own domain (e.g., `basile@basilesimon.fr`)

2. **DID** (Decentralized Identifier): `did:plc:...`
   - Permanent, cryptographic identity
   - Never changes, even if you change your handle
   - Run the test script to see yours

3. **PDS** (Personal Data Server): `https://bsky.social`
   - Where your data is stored
   - You own your data, can migrate to another PDS

---

## Security Notes

- **Never commit** `.env` to git (already in `.gitignore`)
- **App passwords** can be revoked anytime at https://bsky.app/settings/app-passwords
- **Each integration** should have its own app password
- **Rotate passwords** if you suspect they've been compromised

---

## Next Steps

Once you've verified your access with the test script, you can:

1. **Set up RSS-to-BlueSky automation** (recommended first step)
2. **Experiment with WhiteWind** for long-form content
3. **Build custom integrations** using the `@atproto/api` package

See the main integration proposal for detailed implementation options.

---

## Troubleshooting

### "AuthenticationRequired" error
- Check that your app password is correct
- Ensure there are no extra spaces in `.env`
- Try creating a new app password

### "InvalidRequest" error
- Verify your handle is exactly: `basilesimon.bsky.social`
- Don't include the `@` symbol

### Can't find your DID?
- Run `npm run test:atproto` - it will display your DID
- Or visit: https://basilesimon.bsky.social/.well-known/atproto-did

---

## Resources

- [ATProto Documentation](https://atproto.com/)
- [BlueSky API Docs](https://docs.bsky.app/)
- [@atproto/api Package](https://www.npmjs.com/package/@atproto/api)
- [App Passwords Info](https://github.com/bluesky-social/atproto-ecosystem/blob/main/app-passwords.md)
