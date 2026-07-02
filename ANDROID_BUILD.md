# Android App Build Guide

The Stoner Book is a PWA (Progressive Web App) that can be installed on Android in two ways:

## Option 1: Install from Chrome/Edge (Easiest — no build required)

This is the simplest path. Users visit the site in Chrome or Edge on Android and install it directly.

### For Users:
1. Open **https://lykujenkins.github.io/KN-420/** in Chrome or Edge on Android
2. Wait a few seconds — an "Install app" banner may appear, OR
3. Tap the **three-dot menu** → **Install app** / **Add to Home screen**
4. The app installs with its own icon, opens full-screen, works offline

### What makes this work:
- `manifest.json` — defines the app name, icons, colors, display mode
- `sw.js` — service worker enables offline functionality
- `icons/` — PNG icons at multiple sizes (36px–512px)
- HTTPS — GitHub Pages serves over HTTPS (required for PWA)

---

## Option 2: Build an Android APK/AAB for Google Play Store

To publish as a real Android app on the Play Store, you wrap the PWA in a **Trusted Web Activity (TWA)** using Google's Bubblewrap CLI.

### Prerequisites
- **Node.js** 16+ installed
- **Java JDK** 11+ installed
- **Android Studio** (for the SDK, optional but helpful)

### Steps:

#### 1. Install Bubblewrap CLI
```bash
npm install -g @bubblewrap/cli
```

#### 2. Initialize the project
```bash
cd /path/to/stoner-book-repo
bubblewrap init --manifest=https://lykujenkins.github.io/KN-420/manifest.json
```
This reads your PWA manifest and generates the Android project files. It will use the `twa-manifest.json` already in this repo as a template.

#### 3. Generate a signing key
When prompted during init, or separately:
```bash
keytool -genkey -v -keystore android.keystore -alias android -keyalg RSA -keysize 2048 -validity 10000
```
Save this keystore file — you need it for ALL future updates. If you lose it, you can't update the app on the Play Store.

#### 4. Get your signing key fingerprint
```bash
keytool -list -v -keystore android.keystore -alias android
```
Copy the **SHA256** fingerprint.

#### 5. Update `.well-known/assetlinks.json`
Replace `REPLACE_WITH_YOUR_SIGNING_KEY_FINGERPRINT` in `.well-known/assetlinks.json` with your actual SHA256 fingerprint (without colons). This file must be served at:
```
https://lykujenkins.github.io/.well-known/assetlinks.json
```
GitHub Pages will serve it automatically once committed.

#### 6. Build the APK (for testing) or AAB (for Play Store)
```bash
# Build debug APK (sideload on your phone for testing)
bubblewrap build --release

# The output will be in app-release-signed.apk
```

#### 7. Test the APK
- Copy `app-release-signed.apk` to your Android phone
- Enable "Install from unknown sources" in Settings
- Install the APK
- The app should open with no browser address bar

#### 8. Publish to Google Play Store
1. Go to [Google Play Console](https://play.google.com/console)
2. Pay the $25 one-time developer fee
3. Create a new app → upload the `.aab` file
4. Fill in store listing, screenshots, etc.
5. Submit for review (usually 1-3 days)

### Important Notes:
- The `assetlinks.json` file MUST be accessible at your domain's `/.well-known/assetlinks.json` path — otherwise the app shows a browser URL bar at the top
- The signing key MUST be the same for all updates — back it up somewhere safe
- The app package name is `com.stonerbook.app` (defined in `twa-manifest.json`) — change this if you want a different package name
- Update the `host` and URLs in `twa-manifest.json` if you move to a custom domain

---

## File Structure

```
stoner-book-repo/
├── index.html              # The app (single file)
├── manifest.json           # PWA manifest (app name, icons, colors)
├── sw.js                   # Service worker (offline caching)
├── favicon.ico             # Browser tab icon
├── .nojekyll               # Disables Jekyll on GitHub Pages
├── README.md               # Main readme
├── ANDROID_BUILD.md        # This file
├── twa-manifest.json       # Bubblewrap TWA config (for Play Store)
├── .well-known/
│   └── assetlinks.json     # Digital Asset Links (for TWA verification)
├── icons/
│   ├── icon.svg            # Source SVG
│   ├── icon-16.png         # 16x16
│   ├── icon-32.png         # 32x32
│   ├── icon-36.png         # 36x36 (Android ldpi)
│   ├── icon-48.png         # 48x48 (Android mdpi)
│   ├── icon-72.png         # 72x72 (Android hdpi)
│   ├── icon-96.png         # 96x96
│   ├── icon-144.png        # 144x144 (Android xhdpi)
│   ├── icon-180.png        # 180x180 (Apple touch)
│   ├── icon-192.png        # 192x192 (PWA standard)
│   ├── icon-512.png        # 512x512 (PWA standard)
│   └── apple-touch-icon.png
└── scripts/
    └── generate-icons.py   # Regenerate icons if needed
```

## Regenerating Icons

If you change the icon design, edit the SVG in `icons/icon.svg`, then:
```bash
python3 scripts/generate-icons.py
```
This regenerates all PNG sizes from the design.
