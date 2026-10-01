// Builds the e-book PDF and the Gumroad cover/thumbnail images.
// Usage: node gumroad/ebook/build.js   (needs Playwright + Chromium, and Python with pypdf)
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const SRC = __dirname;
const OUT = path.join(SRC, '..', 'dist');
const TMP = fs.mkdtempSync(path.join(require('os').tmpdir(), 'ebook-'));
const url = (file, query = '') => `file://${path.join(SRC, file)}${query}`;

const PDF_NAME = 'Your-First-Digital-Product.pdf';

const footer = `
<div style="width:100%; font-family: Helvetica, Arial, sans-serif; font-size:8px; color:#94a3b8;
            padding: 0 18mm; display:flex; justify-content:space-between;">
    <span>Your First Digital Product</span>
    <span class="pageNumber"></span>
</div>`;

(async () => {
    fs.mkdirSync(OUT, { recursive: true });
    const browser = await chromium.launch();

    // 1. Cover page (full bleed, no margins)
    const cover = await browser.newPage();
    await cover.goto(url('cover.html'), { waitUntil: 'networkidle' });
    await cover.evaluate(() => document.fonts.ready);
    await cover.pdf({ path: path.join(TMP, 'cover.pdf'), format: 'A4', printBackground: true, preferCSSPageSize: true });

    // 2. Interior pages (with margins and page numbers)
    const book = await browser.newPage();
    await book.goto(url('book.html'), { waitUntil: 'networkidle' });
    await book.evaluate(() => document.fonts.ready);
    await book.pdf({
        path: path.join(TMP, 'book.pdf'),
        format: 'A4',
        printBackground: true,
        margin: { top: '18mm', bottom: '20mm', left: '18mm', right: '18mm' },
        displayHeaderFooter: true,
        headerTemplate: '<span></span>',
        footerTemplate: footer,
    });

    // 3. Merge cover + interior
    const merge = `
import sys
from pypdf import PdfWriter
w = PdfWriter()
for f in sys.argv[1:3]:
    w.append(f)
w.add_metadata({'/Title': 'Your First Digital Product', '/Author': 'Waslerr'})
w.write(sys.argv[3])
`;
    execFileSync('python3', ['-c', merge, path.join(TMP, 'cover.pdf'), path.join(TMP, 'book.pdf'), path.join(OUT, PDF_NAME)]);

    // 4. Gumroad images (rendered at 2× for sharpness)
    for (const [mode, width, height, file] of [
        ['wide', 1280, 720, 'gumroad-cover.png'],
        ['square', 600, 600, 'gumroad-thumbnail.png'],
    ]) {
        const page = await browser.newPage({ viewport: { width, height }, deviceScaleFactor: 2 });
        await page.goto(url('promo.html', `?mode=${mode}`), { waitUntil: 'networkidle' });
        await page.waitForTimeout(300);
        await page.screenshot({ path: path.join(OUT, file) });
    }

    await browser.close();
    fs.rmSync(TMP, { recursive: true, force: true });
    console.log(`Built ${PDF_NAME}, gumroad-cover.png and gumroad-thumbnail.png in ${OUT}`);
})();
