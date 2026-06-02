# 2:22 Church — Design & Context Notes

Living reference for the website's design system, structure, and the redesign work done so far.
Keep this updated when the look & feel or structure changes.

---

## 1. What this project is

- A **static website** (plain HTML + CSS + a little JS) for **2:22 Church** — a house church movement.
- Hosted on **GitHub Pages** from the **`main`** branch of repo `freelanceanjish/2-22church`.
- Custom domain: **https://2-22church.com** (see `CNAME`). HTTPS is enforced.
- **No build step / no framework.** Editing an `.html`, `.css`, `.js`, or asset and pushing to `main` redeploys automatically (Pages build takes ~30–60s).

---

## 2. Design system (the "Antioch-inspired" light theme)

The site was redesigned to mirror the visual direction of `antiochlakecities.church`: clean, light, editorial, single accent.

### Typography
- **Font family: `Poppins`** (Google Fonts), weights 300/400/500/600/700.
- Everything uses Poppins — headings and body. (The old theme used Cormorant Garamond + DM Sans; those are fully removed.)
- Headlines are tight: large size, `font-weight:500–600`, negative letter-spacing.

### Color tokens (CSS variables in `style.css` `:root`, mirrored in each page's inline `<style>`)
| Token | Value | Use |
|---|---|---|
| `--gold` | `#172A36` | Primary brand accent (dark charcoal-blue). Labels, marks, icons, ink. |
| `--gold-light` | `#EAF1F4` | Pale blue-gray fills/accents. |
| `--gold-dark` | `#0D171F` | Footer background (dark). |
| `--deep` | `#FFFFFF` | Page background. |
| `--deep-mid` | `#F4F7F5` | Alternate section background (light gray). |
| `--surface` | `#FFFFFF` | Card backgrounds. |
| `--surface-light` | `#EEF4F7` | Subtle card hover/fill. |
| `--text-primary` | `#0E0E0E` | Headings / primary text. |
| `--text-secondary` | `#47545B` | Body text. |
| `--text-muted` | `#778187` | Captions / small labels. |
| `--border` | `rgba(23,42,54,0.14)` | Hairline borders. |
| `--border-subtle` | `rgba(14,14,14,0.08)` | Lighter dividers. |
| `--shadow-soft` | `0 24px 70px rgba(23,42,54,0.12)` | Card shadow. |
| `--radius-xl/lg/md` | `28px / 18px / 12px` | Rounded corners. |

> NOTE: the variable names still say `--gold*` for historical reasons, but the palette is charcoal-blue, **not** gold. Don't rename without updating every page (each HTML file has its own copy of the `:root` block).

### Visual language
- Light/white pages, generous whitespace.
- **Rounded cards** with soft shadows and hairline borders.
- **Pill buttons** (`border-radius:999px`), dark fill (`--text-primary`) with white text; light variant = white fill + border.
- Single dark accent (`--gold` / `#172A36`); diagrams are monochrome dark ink on transparent/white.

---

## 3. File structure

### Pages (each is self-contained: shares `style.css` + has its own inline `<style>` for page-specific rules)
`index.html` (home) · `articles.html` · `blog.html` · `blogs.html` · `post.html` · `gatherings.html` · `our-story.html` · `cosmology.html` · `old-maps.html` · `project314.html` · `qa.html` · `references.html` · `scripturalism.html` · `testimonies.html` · `subscribers.html`

### Shared / data
- `style.css` — shared stylesheet (nav, footer, typography system, buttons, page-header, blog cards).
- `posts.js` — **the only file to edit to manage blog/article posts** (see `README.md`). Posts render into `index.html`, `articles.html`, `blog.html`, `post.html`.
- `CNAME` — custom domain.
- `README.md` — non-technical guide for publishing blog posts.

### Key images / diagrams (light-theme, brand ink `#172A36`)
- `hero-bg.jpg` — homepage hero + sub-page header background. A bright **wheat-field** photo (optimized from `wheat.jpg`, ~241 KB, 1920×1170). Replaced the old dark `hero3.jpg` "2:22" graphic (deleted).
- `foundations-pillars.svg` — Foundation section: a four-pillar house ("Teaching · Fellowship · Breaking Bread · Prayer", "Acts 2:42"). **User-supplied SVG.**
- `why-the-name.svg` — "Why the name" section: two overlapping circles / central flame, "Apostolic Teaching & Inward Purity". **User-supplied SVG.**
- `yhwh_is_not_jesus_diagram.svg` — "The Distinction" diagram (YHWH vs Jesus). Recolored to the light palette (dark "God" circle w/ light text, light "Jesus" circle w/ dark text/border, dark connectors + "IS NOT").
- `YHWH-is-not-Jesus.png` — a high-res (2912×2840) white-background export of the Distinction SVG, kept for direct download at `/YHWH-is-not-Jesus.png`.
- Other study SVGs (`agencies_of_god.svg`, `apostles_vs_translators.svg`, etc.) belong to study/article pages.

---

## 4. Key components

### Logo (nav + footer) — "Circle monogram"
- Markup (in every page's nav and footer):
  `<a class="nav-logo"><span class="logo-mark">2-22</span><span class="logo-word">Church</span></a>`
- `.logo-mark` = a 38px **circle**: dark `--gold` fill + white "2-22" in the nav; in the footer it **inverts** (white circle, dark text) because the footer background is dark.
- Note it reads **`2-22`** (hyphen), not `2:22`.
- CSS lives in `style.css` (`.nav-logo .logo-mark`, plus footer overrides). The old `.logo-text`/`.logo-colon` classes are unused now.

### Homepage hero (`.home-hero` in `index.html` inline style)
- Two-column grid: copy (kicker + `<h1>` + subtitle + pill buttons) on the left, **two "2 Timothy" verse cards** on the right.
- Eyebrow/kicker = "Built on the Living Word"; `<h1>` = "A house church movement".
- Verse cards are **centered** beside the copy (`align-items:center`) so they're visible at first glance. Mobile = content-height hero, smaller title, inline buttons, side-by-side cards.
- Background = `hero-bg.jpg` with a left-to-right white gradient overlay so dark text stays readable.

### Figure cards (`.home-figure`)
- Light rounded cards used to present the three homepage diagrams. The diagrams contain their own titles, so surrounding duplicate labels were removed (only "The Distinction" keeps a `.home-figure-label` because its SVG has no internal title).

### Footer
- Dark background (`--gold-dark` `#0D171F`), white text, inverted logo. Brand + Explore + Resources + Connect columns.

---

## 5. Deployment & verification

1. Edit files, then:
   `git add -A && git commit -m "..." && git push origin main`
2. GitHub Pages auto-builds. Check status:
   `gh api repos/freelanceanjish/2-22church/pages/builds/latest --jq '.status,.commit'`
   (status goes `building` → `built`, ~30–60s.)
3. Verify live: `curl -s -o /dev/null -w '%{http_code}' https://2-22church.com/`
4. Browser may cache CSS/images aggressively — hard-refresh (Cmd/Ctrl+Shift+R) or append `?cb=<timestamp>`.

> Each page duplicates the `:root` tokens and font link in its own `<head>`/inline `<style>`. When changing the palette or fonts, update **all** pages (a small script that does a string-replace across `*.html` is the easiest way).

---

## 6. Change history (high level)

1. **Redesign** from the old dark/serif "2:22" theme to the light Poppins "Antioch-inspired" system (palette, nav, footer, hero, typography) across all pages.
2. **Hero** reworked into a photo-led layout; later trimmed the title, moved "Built on the Living Word" to the eyebrow, kept the two 2 Timothy scriptures, and centered those cards.
3. **Three homepage diagrams** (Foundation, Why the name, The Distinction): first framed in dark cards, then recolored to the light palette; Foundation & Why-the-name later **replaced with user-supplied SVGs**; figure cards switched to light.
4. **De-duplicated** the Foundation / Why-the-name sections (removed redundant Acts 2:42 box, figure labels, and the four-pillar paragraph/tags now shown inside the images).
5. **Logo** changed to the circle monogram reading **`2-22`**.
6. **Hero/header background** swapped from the dark `hero3.jpg` "2:22" graphic to the clean `hero-bg.jpg` wheat field.

---

## 7. Notes / gotchas

- This site is maintained by a **cloud agent that runs on a remote VM** — it cannot read files from a local machine (e.g. `~/Downloads`). To hand it custom files, **commit them to the repo** (GitHub web "Upload files" works) or paste text (for SVG).
- The variable names `--gold*` are charcoal-blue, not gold (legacy naming).
- Don't reintroduce the fonts `Cormorant Garamond` / `DM Sans` or the old dark colors (`#060C18`, `#0C1830`, `#F0EAD6`, etc.) — they were intentionally removed.
- To add/edit blog posts, edit `posts.js` only (see `README.md`).
