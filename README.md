# 2:22 Church Website

## Your Website Files

| File | What it is |
|------|------------|
| `index.html` | Your main homepage |
| `blog.html` | Full blog listing — shows ALL posts |
| `post.html` | Individual post reader page |
| `posts.js` | **The only file you edit to manage blog posts** |
| `style.css` | Shared styles (don't need to touch this) |

---

## How to Publish a New Blog Post

Open `posts.js` in any text editor (Notepad, TextEdit, VS Code, etc.)

At the very top of the file, you will see the `POSTS` array starting with `const POSTS = [`.

**Copy and paste this template right after that opening bracket** (before the existing first post), then fill in your content:

```js
{
  id: "short-url-title-here",
  title: "Your Blog Title Here",
  date: "21 April 2026",
  category: "Teaching",
  excerpt: "One or two sentence summary shown on the blog listing page.",
  image: "",
  content: `
    <p>Your first paragraph here.</p>

    <h2>A Section Heading</h2>

    <p>More content here.</p>

    <blockquote>"A scripture verse here." — Reference</blockquote>

    <p>Closing thoughts.</p>
  `
},
```

### Field guide

- **id** — Short, lowercase, no spaces. Use hyphens. Example: `"the-holy-spirit-our-helper"`. This becomes the URL.
- **title** — Your full post title.
- **date** — Written in full. Example: `"21 April 2026"`.
- **category** — Choose one: `Teaching` · `Baptism` · `Service` · `Giving` · `Community` · `Prayer` · `Testimony` · `Leadership` · `Reflection`
- **excerpt** — 1–2 sentences shown on the blog listing page and homepage.
- **image** — Paste an image URL (from Unsplash, your own photos, etc.) or leave as `""` for no image.
- **content** — Your full post in HTML. Use `<p>` for paragraphs, `<h2>` for section headings, `<blockquote>` for scripture.

### Content formatting inside `content`

```html
<p>A normal paragraph.</p>

<h2>A section heading</h2>

<h3>A smaller sub-heading</h3>

<blockquote>"Scripture or important quote here." — Reference</blockquote>

<p>Text with <strong>bold words</strong> or <em>italic words</em>.</p>
```

### Always paste new posts at the TOP of the array

The website automatically shows the newest posts first. The first post in the array = the featured post on the homepage.

---

## How to Delete a Post

Open `posts.js` and find the post you want to remove.

Delete everything from its opening `{` to its closing `},`

Save the file and push to GitHub.

---

## How to Deploy to GitHub Pages

### First time setup

1. Go to [github.com](https://github.com) and sign in.
2. Click the **+** button → **New repository**.
3. Name it `2-22church` (or any name you like).
4. Set it to **Public**.
5. Click **Create repository**.
6. Upload all 5 files (`index.html`, `blog.html`, `post.html`, `posts.js`, `style.css`) by dragging them into the repository page.
7. Click **Commit changes**.
8. Go to **Settings** → **Pages** (in the left sidebar).
9. Under **Branch**, select `main` and click **Save**.
10. Your site will be live at `https://YOUR-USERNAME.github.io/2-22church/` within a minute or two.

### Connecting your domain (2-22church.com)

1. In GitHub Pages settings, under **Custom domain**, type `2-22church.com` and click **Save**.
2. In your domain registrar (wherever you bought 2-22church.com), add these DNS records:

   | Type | Name | Value |
   |------|------|-------|
   | A | @ | 185.199.108.153 |
   | A | @ | 185.199.109.153 |
   | A | @ | 185.199.110.153 |
   | A | @ | 185.199.111.153 |
   | CNAME | www | YOUR-USERNAME.github.io |

3. Wait up to 24 hours for DNS to propagate. GitHub will also automatically enable HTTPS for you.

### Publishing a new post (after initial setup)

1. Open `posts.js` on your computer, add the new post at the top, save.
2. Go to your GitHub repository.
3. Click on `posts.js` in the file list.
4. Click the **pencil icon** (Edit this file) in the top right.
5. Paste in your updated content.
6. Click **Commit changes**.
7. Your site updates in about 60 seconds.

*Alternatively: use GitHub Desktop app for a more visual drag-and-drop experience.*

---

## Getting Help

If you want help writing or publishing a post, simply share your content with the assistant and ask them to format it and add it to `posts.js`. They will give you the updated file ready to upload.
