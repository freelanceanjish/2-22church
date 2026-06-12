# 2:22 Church — Writing Voice Guide

Saved from author direction. Apply to every page, article, and study before publishing.

## Who is speaking

**We** for the church voice on most pages: study hub, home, gatherings, Q&amp;A, promoted research summaries, and site-wide banners. **I** only where the writing is personal testimony: Our Story, blogs, articles, and first-person testimony posts.

One human voice behind We, with conviction to write and compassion for people lost in religion, ritual, and mainstream Christianity. Written with love. No pride. No arrogance. No show-off tone.

The goal is to present facts that help genuine people in their pursuit of truth, and to lead them out of the darkness of religion, fake Christianity, performance, and lies.

## Audience

Genuine people searching for the truth. They detect AI-generated text immediately. They do not want instructions, formats, or paragraph structures that feel machine-made.

## What to sound like

Use *Autopsy of a Soul* (posts.js, testimony) as the standard: first-person where appropriate, honest, conversational, full sentences that breathe, mixed length but **never** staccato stacks of tiny sentences or one-word sentences.

## Human reasoning, not machine output

Readers can tell when a piece was assembled by pattern-matching instead of thought. The difference is not vocabulary. It is whether the writer has **reasoned through** the topic and is **thinking aloud** with the reader.

**Sound like a person who researched, reflected, and is sharing what they found:**
- Follow a real line of inquiry: a question you had, what surprised you, what you had to sit with, what you concluded and why.
- Let one idea lead to the next. Cause, then effect. Claim, then evidence. Comparison, then what it means for someone reading.
- Use "I" where the journey is personal (articles, testimony). Show your mind working: "I kept reading," "That stopped me," "I had assumed X until Y."
- Vary rhythm. Some paragraphs unpack one detail slowly. Others move faster. Do not march through identical paragraph shapes.

**Machine patterns to avoid:**
- Filling sections with parallel bullets or side-by-side boxes that only **label** things without explaining them.
- Announcing structure instead of writing it ("In this section we will examine…", "What follows is a comparison of…").
- Symmetric templates: same sentence opener three times, same "Feature / Vedic / Jewish" rhythm with no narrative between tables.
- Stacking facts like a catalogue with no connective tissue between them.
- Conclusions that only restate the introduction in different words.

**The read-aloud test for reasoning:** Would a thoughtful friend explain it this way after doing the reading themselves? Or does it sound like a summary bot?

## Research depth before you publish

Do not skim a topic and paste the surface. **Go deep first, then write.**

Before drafting an article or study section:
1. **Research thoroughly** across primary sources, tradition, and lived practice (not one Wikipedia paragraph).
2. **Understand both (or all) sides** of a comparison: mechanics **and** how people actually live the calendar, feast, ritual, or text.
3. **Bring the reader something they could not get from a chart alone**: court sessions in Adar, Purim Katan, what Hindus do in Purushottama Maas, why a month is called "mal" in one tradition and "most sacred" in another.
4. **Earn the comparison.** Tables and diagrams support the prose; they do not replace it.

If you only know the astronomy of a leap month but not what Jews and Hindus **do** during it, you are not ready to publish that section. Keep researching until the reader leaves with real knowledge, not just labels.

## Timeline when comparing cultures or texts

Whenever you compare Scripture, Hebrew tradition, or apostolic faith with another culture's texts, rituals, or calendars, **anchor the comparison in time**. Do not line items up side by side as if they appeared together. Show **when** each witness belongs on the line.

**Why:** The reader needs to see precedence. Truth is not a tie between equal inventors. Creation, the flood, Babel, Sinai, the prophets, and Messiah sit at the centre of history. Other traditions often preserve **echoes** of what came earlier, not parallel originals.

**How to do it:**
- State approximate dates openly (e.g. post-flood Noah tradition, Mosaic Torah ~1400 BC, Rigveda range ~1600 BC onward, classical Ayurveda compilation centuries later, Second Temple scrolls, medieval Puranic layers). Note when scholars disagree.
- Put the **biblical or Hebrew witness first** in the timeline when it is earlier or claims an earlier origin (Noah, Shem, Sinai, Job, Exodus calendar).
- When a later text echoes an earlier pattern, say so in plain language: "India's temple rites as practised today developed **after** the worship God gave Moses at Sinai," or "the Charaka Samhita was compiled long after the post-flood book the Hebrew prologue describes."
- Use a short prose timeline, a dated table row, or a `timeline-note` paragraph at the start of a comparison section. Do not bury dates in a footnote alone.
- The goal is not academic one-upmanship. It is to show that the **dominant line of revelation** runs through what God spoke to Israel and fulfilled in Christ, and that other cultures often carry surviving fragments of that older memory.

## Same skeleton, different object of worship (Hindu–Hebrew articles)

In every article comparing Hebrew and Hindu (or Vedic) tradition, name the pattern plainly:

- What is **built, celebrated, and narrated** often shares the same **skeleton** (three-room sanctuary, lunar calendar, sacrifice grammar, medical frame, messianic hope, and so on).
- The decisive difference is not the outer shape. **Israel worshipped the God who cannot be seen and who dwells in heaven.** Hindu temple and popular religious life often centres on **many visible figures**, lower gods and emblems shaped like created beings.
- End with a **coincidence question** in a `coincidence-question` block: ask the reader what **percentage** of the parallel they are willing to call coincidence, and invite them to **rethink history in search of truth**. Do not lecture. Ask.

## What never to do

- **No dashes** in prose (no em dash, no en dash used as punctuation). Use commas, "and," or a new sentence instead.
- **No instructing the reader** ("Read this first," "Pick a study," "Click any," "Look," "Take your time," "Argue with me if you need to").
- **No one-word or micro-sentences** stacked in a row ("Wide. Low. Stable." / "That is all." / "He is One." as a punch line after a list).
- **No AI tics**: "honestly," "Look:", numbered gallery captions, section numbering, "Traditional — fails," corporate "We believe," hedged "in our view."
- **No pride or debate posture** ("unpopular conclusions," "argue with me," "as far as I can see it" as a repeated crutch).
- **No shallow compare-and-label articles** that read like generated glossaries instead of a human who did the homework.

## Identity (important)

Do **not** write "I am part of a spiritual family." The author carries a **burden to create** a spiritual family around apostolic faith, not to describe membership in one that already exists.

## Burden and compassion

Write from burden (called to speak, to gather, to pass on truth) and compassion (for the confused, the burned, the sincere person still inside institutional Christianity). Offer Scripture and evidence as a fellow searcher who found something, not as a lecturer correcting inferiors.

## Read-aloud test

If you would not say it to someone over tea, rewrite it. If it sounds like a blog template, a FAQ bot, or a theology brochure, rewrite it.

## When a reader reports a broken image or diagram

If one article asset fails on the live site, **do not fix only that file and stop**. Treat it as a site-wide quality issue.

Before closing the task:
1. Run `./scripts/check-post-assets.sh` and fix **every** missing or invalid asset referenced in `posts.js` (cover images, inline diagrams, SVGs).
2. Validate **all** `.svg` files in the repo as well-formed UTF-8 XML (invalid bytes break rendering even when HTTP returns 200).
3. Bump cache on the fixed asset (`?v=2`) and bump `posts.js` version in `post.html` when article content changes.
4. Test locally with `python3 -m http.server` and confirm each broken report returns **HTTP 200** and parses as valid SVG.
5. Note in the PR which articles were audited, not only the one the reader named.

Broken diagrams are unfinished work. Ship only after the full article asset pass.

## Do not duplicate copy

Write each page with its own purpose. Do not paste the same burden paragraph, house church essay, or passion block across headers, banners, and body sections. The full personal burden lives on **Our Story** (`#house-church`). Other pages get a short, page-specific line only, or a link back to Our Story when context needs it.
