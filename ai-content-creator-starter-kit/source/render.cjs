// Renders every document listed in out/manifest.json to PDF, saves page
// snapshots used by the Gumroad preview images, then renders those images.
//
// Usage: node render.cjs                      (run build.py first)
//        node render.cjs manifest-ar.json     (run build_ar.py first)
const { chromium } = require("playwright");
const fs = require("fs");
const path = require("path");

const SRC = __dirname;
const OUT = path.join(SRC, "out");
// Optional argument: another manifest in out/, e.g. "manifest-ar.json".
const MANIFEST = process.argv[2] || "manifest.json";
const manifest = JSON.parse(fs.readFileSync(path.join(OUT, MANIFEST), "utf8"));

async function renderDocs(browser) {
  const failures = [];
  const page = await browser.newPage({ viewport: { width: 1400, height: 1000 }, deviceScaleFactor: 2 });
  page.on("pageerror", (e) => failures.push(String(e)));
  for (const doc of manifest.documents) {
    await page.goto("file://" + path.join(OUT, doc.html));
    await page.waitForFunction(() => window.__layout, null, { timeout: 60000 });
    const layout = await page.evaluate(() => window.__layout);
    for (const w of layout.warnings) failures.push(`${doc.pdf}: ${w}`);

    fs.mkdirSync(path.dirname(doc.pdf), { recursive: true });
    await page.pdf({ path: doc.pdf, preferCSSPageSize: true, printBackground: true });

    const snapDir = path.join(OUT, "snapshots");
    fs.mkdirSync(snapDir, { recursive: true });
    const pages = await page.$$(".page");
    for (const i of doc.snapshots || []) {
      if (pages[i]) await pages[i].screenshot({ path: path.join(snapDir, `${doc.id}-${i + 1}.png`) });
    }
    console.log(`${String(layout.pages).padStart(3)} pages  ${path.basename(doc.pdf)}`);
    doc.pages = layout.pages;
  }
  await page.close();
  fs.writeFileSync(path.join(OUT, MANIFEST.replace("manifest", "page-counts")), JSON.stringify(manifest.documents.map((d) => ({ pdf: path.basename(d.pdf), pages: d.pages })), null, 2));
  return failures;
}

async function renderImages(browser) {
  for (const img of manifest.images) {
    const page = await browser.newPage({ viewport: { width: img.width, height: img.height }, deviceScaleFactor: img.scale || 2 });
    await page.goto("file://" + path.join(OUT, img.html));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(150);
    fs.mkdirSync(path.dirname(img.png), { recursive: true });
    await page.screenshot({ path: img.png });
    console.log(`image  ${path.basename(img.png)}`);
    await page.close();
  }
}

(async () => {
  const browser = await chromium.launch();
  const failures = await renderDocs(browser);
  await renderImages(browser);
  await browser.close();
  if (failures.length) {
    console.error("\nLAYOUT PROBLEMS:\n" + failures.join("\n"));
    process.exit(1);
  }
})();
