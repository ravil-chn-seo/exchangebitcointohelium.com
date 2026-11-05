# exchangebitcointohelium.com

Static one-page comparison site: "Best Ways to Exchange Bitcoin to Helium (BTC to HNT)".

- Source: `build.py` (content, templates, JSON-LD, generated hex art) + `src/` (CSS, JS, self-hosted fonts, OG image)
- Build: `python3 build.py` → `dist/` (committed, served as-is)
- Deploy: Railway "Deploy from GitHub repo" using the `Dockerfile` (Caddy serves `/app/dist`)
- Analytics: `dataLayer` events only, no third-party scripts
