#!/usr/bin/env node
/** Capture live nav logo and hero tagline crops from index.html for OG thumbnail. */
import fs from "fs";
import http from "http";
import path from "path";
import { fileURLToPath } from "url";
import puppeteer from "puppeteer-core";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "blog-assets", "og-crops");
const PORT = 8765;

function startServer() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let urlPath = decodeURIComponent(req.url.split("?")[0]);
      if (urlPath === "/") urlPath = "/index.html";
      const filePath = path.join(ROOT, urlPath.replace(/^\//, ""));
      if (!filePath.startsWith(ROOT) || !fs.existsSync(filePath) || fs.statSync(filePath).isDirectory()) {
        res.writeHead(404);
        res.end("Not found");
        return;
      }
      const ext = path.extname(filePath).toLowerCase();
      const types = {
        ".html": "text/html",
        ".css": "text/css",
        ".js": "text/javascript",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".svg": "image/svg+xml",
        ".webp": "image/webp",
        ".ico": "image/x-icon",
      };
      res.writeHead(200, { "Content-Type": types[ext] || "application/octet-stream" });
      fs.createReadStream(filePath).pipe(res);
    });
    server.listen(PORT, "127.0.0.1", () => resolve(server));
  });
}

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const server = await startServer();

  const browser = await puppeteer.launch({
    executablePath: process.env.CHROME_PATH || "/usr/local/bin/google-chrome",
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox", "--font-render-hinting=medium"],
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1200, height: 800, deviceScaleFactor: 1 });
    await page.goto(`http://127.0.0.1:${PORT}/index.html`, { waitUntil: "networkidle0" });
    await page.evaluateHandle("document.fonts.ready");

    const logo = await page.$("nav .nav-logo");
    if (!logo) throw new Error("nav logo not found");
    const logoBox = await logo.boundingBox();
    await logo.screenshot({ path: path.join(OUT, "logo-crop.png") });

    const clip = await page.evaluate(() => {
      const kicker = document.querySelector(".hero-kicker");
      const subtitle = document.querySelector(".hero-subtitle");
      if (!kicker || !subtitle) return null;
      const k = kicker.getBoundingClientRect();
      const s = subtitle.getBoundingClientRect();
      return {
        x: Math.max(0, Math.floor(k.left - 4)),
        y: Math.max(0, Math.floor(k.top - 4)),
        width: Math.ceil(Math.max(k.right, s.right) - k.left + 8),
        height: Math.ceil(s.bottom - k.top + 8),
      };
    });

    if (!clip) throw new Error("hero tagline elements not found");

    await page.screenshot({
      path: path.join(OUT, "hero-tagline-crop.png"),
      clip,
    });

    fs.writeFileSync(
      path.join(OUT, "meta.json"),
      JSON.stringify(
        {
          viewport: { width: 1200, height: 800 },
          logo: logoBox,
          tagline: clip,
        },
        null,
        2
      )
    );

    console.log("wrote", path.join(OUT, "logo-crop.png"));
    console.log("wrote", path.join(OUT, "hero-tagline-crop.png"));
  } finally {
    await browser.close();
    server.close();
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
