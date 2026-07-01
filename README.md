# 🌿 The Stoner Book

A private, local-first cannabis journal that lives entirely in your browser. Track sessions, strains, terpenes, effects, ideas, voice notes, and mood changes — then discover patterns in your own creativity and well-being. Your data never leaves your device (unless you choose to chat with Dave, the AI buddy).

## ✨ Features

### 📖 Journal
- **Log sessions** with strain, type, terpenes, mood before/after, effects, notes, and voice notes
- **Audio recording** via MediaRecorder API (Opus codec, 5-min cap)
- **Strain autocomplete** from a built-in library of 75+ strains with terpene/effect profiles
- **Wikipedia lookup** for strains not in the library — auto-fills type, terpenes, effects, and image
- **Save strains to your personal library** for future autocomplete

### 📚 Strain Library
- 75+ built-in strains (Sativa, Indica, Hybrid, CBD-dominant) with terpene profiles, effects, flavors, and descriptions
- Search and filter by type
- Tap any strain for full details + "Log session with this strain" shortcut
- Add custom strains from Wikipedia lookups
- **Terpene tooltips** — tap any terpene tag to learn what it does (14 terpenes documented)

### 📖 History
- Searchable, filterable session history
- **Edit** any past session
- **Duplicate** sessions (great for "smoking the same strain again")
- **Delete** sessions
- Full session detail modal with audio playback

### ✨ Insights
Four sub-tabs of visualizations:

- **📊 Overview** — stats grid (total sessions, this month, ideas, voice notes), average mood lift, top strains/effects/terpenes leaderboards, best strain by mood lift
- **🕐 Hours** — 24-hour heatmap timeline (toggle between session count and average mood lift), like a weather app's hourly forecast
- **📅 Days** — day-of-week bar chart + 7-day activity strip
- **🗓️ Year** — full-year GitHub-style contribution calendar with longest streak tracking

### 🚪 Dave (AI Buddy)
A chatbot named after the Cheech & Chong character ("Dave's not here, man"), powered by Google Gemini 2.0 Flash:
- Streaming responses
- Chill stoner buddy personality — knowledgeable about cannabis
- Optionally sees your 10 most recent sessions for personalized advice
- Bring-your-own API key (free from Google AI Studio)
- All chat history stored locally

### 🔒 Privacy-first
- **100% local** — no backend, no accounts, no tracking
- IndexedDB storage (handles hundreds of MB of audio)
- Export/import JSON backups (includes audio + custom strains)
- PWA installable — works offline, lives on your home screen
- Your API key for Dave is stored only in your browser, sent only to Google

## 🚀 Deploy to GitHub Pages

This is a single `index.html` file — no build step needed.

1. Push `index.html` to the root of a GitHub repository
2. Go to **Settings → Pages**
3. Source: `main` branch, `/` (root) folder
4. Save — your app goes live at `https://YOUR_USERNAME.github.io/REPO_NAME/`

## 🛠️ Tech Stack

- **Vanilla HTML/CSS/JS** — no build step, no framework
- [Dexie.js](https://dexie.org/) — IndexedDB wrapper for local storage
- **MediaRecorder API** — audio recording
- **Wikipedia REST API** — strain lookups
- **Google Gemini 2.0 Flash** — Dave the chatbot (bring your own key)
- **PWA** — manifest + service worker built at runtime via Blob URLs (keeps file single-file)

## 📱 Install as an App

Open the site in Chrome (desktop or mobile) → after a few seconds an install banner appears, or use the browser menu → "Install app". It'll live on your home screen with its own icon and work offline.

## 📤 Backing Up Your Data

Tap the **⬇** icon in the header to export a JSON backup (includes all sessions, audio, and custom strains). Tap **⬆** to import. Move between devices by exporting from one and importing on another.

## ⚖️ Legal & Privacy Notes

- For use only where cannabis is legal
- Not medical advice — consult a healthcare professional
- 21+ only
- Cannabis data is sensitive even where legal — this app keeps everything on your device by design
- When chatting with Dave, your data goes to Google's Gemini API per their privacy policy

## 🎨 The Concept

> This platform becomes more than a diary. It becomes a personal creativity tracker.
>
> Users will discover:
> - Which strains spark ideas
> - Which terpenes boost creativity
> - What time of day they think best
> - Which sessions produce the most insights

The non-obvious insight: this isn't a strain-review app (Leafly exists). It's a **quantified-self tool for your own creative process** — what sparks YOUR best ideas, tracked over time.

---

*Built one feature at a time, in conversation.*
