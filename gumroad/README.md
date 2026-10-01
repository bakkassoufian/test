# Gumroad e-book: "Your First Digital Product"

- **`dist/`**: the files to upload to Gumroad (PDF, cover image, thumbnail)
- **`LISTING.md`**: the text to paste into the Gumroad product page (name, price, description, tags…)
- **`ebook/`**: the source files, if you want to change the e-book

## Changing the e-book

1. Edit the text in `ebook/book.html`. Change the cover in `ebook/cover.html`.
2. Rebuild the PDF and the images:

```bash
pip install pypdf
NODE_PATH=$(npm root -g) node gumroad/ebook/build.js
```

This needs Node.js with Playwright (Chromium) installed. The new files are written to `dist/`.

To change the author name, search for `Waslerr` in `ebook/book.html` and `ebook/cover.html`.
