// Lays the hidden #source sections out into fixed-size .page elements.
//
// <section class="full">  -> one full-bleed page, no header/footer.
// <section class="flow" data-section="Title" [data-break="none"]>
//   Direct children are atomic blocks. A block with data-split="items" is a
//   container (list, grid, table) whose children may be spread over pages;
//   the container is re-created on each page (tables keep their <thead>).
//   Blocks with class "kwn" (keep with next) travel to the next page with
//   whatever follows them.
(function () {
  const book = document.getElementById("book");
  const source = document.getElementById("source");
  const docTitle = document.body.dataset.doc || "";
  const warnings = [];
  let body = null;
  let sectionTitle = "";

  function overflow(el) {
    return el.scrollHeight > el.clientHeight + 0.5;
  }

  function newPage(title) {
    const page = document.createElement("div");
    page.className = "page";
    page.innerHTML =
      '<div class="page-header"><span class="brand"></span><span class="sect"></span></div>' +
      '<div class="page-rule"></div><div class="page-body"></div>' +
      '<div class="page-footer"><span class="doc"></span><span class="num"></span></div>';
    page.querySelector(".brand").textContent = document.body.dataset.brand || "";
    page.querySelector(".sect").textContent = title;
    page.querySelector(".doc").textContent = docTitle;
    book.appendChild(page);
    return page.querySelector(".page-body");
  }

  function describe(el) {
    return (el.textContent || "").trim().replace(/\s+/g, " ").slice(0, 70);
  }

  // Headings marked keep-with-next sitting at the end of the current page.
  function takeTrailingKeepers() {
    const carry = [];
    while (body.lastElementChild && body.lastElementChild.classList.contains("kwn") && body.firstElementChild !== body.lastElementChild) {
      carry.unshift(body.lastElementChild);
      body.lastElementChild.remove();
    }
    return carry;
  }

  function breakPage(carry) {
    body = newPage(sectionTitle);
    carry.forEach((c) => body.appendChild(c));
  }

  function placeAtomic(block) {
    body.appendChild(block);
    if (!overflow(body)) return;
    block.remove();
    const carry = takeTrailingKeepers();
    breakPage(carry);
    body.appendChild(block);
    if (overflow(body)) warnings.push("Block taller than a page: " + describe(block));
  }

  function shell(block) {
    const s = block.cloneNode(false);
    if (block.tagName === "TABLE") {
      const head = block.tHead;
      if (head) s.appendChild(head.cloneNode(true));
      s.appendChild(document.createElement("tbody"));
    }
    return s;
  }

  function itemHost(s) {
    return s.tagName === "TABLE" ? s.tBodies[0] : s;
  }

  function placeSplittable(block) {
    const items = Array.from(itemHost(block).children);
    let current = shell(block);
    body.appendChild(current);
    for (const item of items) {
      const host = itemHost(current);
      host.appendChild(item);
      if (!overflow(body)) continue;
      item.remove();
      if (host.children.length === 0) {
        current.remove();
        const carry = takeTrailingKeepers();
        breakPage(carry);
      } else {
        breakPage([]);
      }
      current = shell(block);
      body.appendChild(current);
      itemHost(current).appendChild(item);
      if (overflow(body)) warnings.push("Item taller than a page: " + describe(item));
    }
  }

  function layout() {
    for (const section of Array.from(source.children)) {
      if (section.classList.contains("full")) {
        const page = document.createElement("div");
        page.className = "page full";
        page.appendChild(section);
        book.appendChild(page);
        body = null;
        continue;
      }
      sectionTitle = section.dataset.section || "";
      if (!body || section.dataset.break !== "none") {
        body = newPage(sectionTitle);
      } else {
        // Continuing on the same page: the header keeps the section that opened it.
      }
      for (const block of Array.from(section.children)) {
        if (block.dataset.split === "items") placeSplittable(block);
        else placeAtomic(block);
      }
    }

    // Drop pages that ended up empty (e.g. a trailing break), then number.
    book.querySelectorAll(".page-body").forEach((b) => {
      if (b.children.length === 0) b.closest(".page").remove();
    });
    const pages = Array.from(book.querySelectorAll(".page"));
    const total = pages.length;
    pages.forEach((p, i) => {
      const num = p.querySelector(".page-footer .num");
      if (num) num.innerHTML = String(i + 1).padStart(2, "0") + " <span>/ " + String(total).padStart(2, "0") + "</span>";
    });
    source.remove();
    window.__layout = { pages: book.querySelectorAll(".page").length, warnings };
  }

  document.fonts.ready.then(() => requestAnimationFrame(layout));
})();
