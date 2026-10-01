// ============================================================
//  STORE CONFIGURATION — edit this part with your Gumroad info
// ============================================================
const STORE = {
    // Your Gumroad username (from https://USERNAME.gumroad.com)
    gumroadUsername: 'waslerr',
    name: 'Waslerr',
    bio: 'Produits numériques, templates et ressources pour créateurs.',
    currency: '€',
};

// One entry per product. "permalink" is the end of the product URL on Gumroad:
// https://waslerr.gumroad.com/l/PERMALINK  →  permalink: 'PERMALINK'
// Leave permalink empty ('') to send buyers to your main Gumroad page instead.
// "image" is optional: put a URL or a path like 'assets/img/produit.jpg'.
const PRODUCTS = [
    {
        title: 'Pack de templates Notion',
        description: 'Organisez vos projets, vos finances et vos habitudes avec 10 templates prêts à l\'emploi.',
        price: 9,
        category: 'Templates',
        permalink: '',
        image: '',
    },
    {
        title: 'Guide : lancer son produit numérique',
        description: 'Un e-book étape par étape pour créer, fixer le prix et vendre votre premier produit.',
        price: 15,
        category: 'E-books',
        permalink: '',
        image: '',
    },
    {
        title: 'Kit UI Glassmorphism',
        description: 'Composants HTML/CSS modernes : cartes, formulaires, boutons et arrière-plans animés.',
        price: 19,
        category: 'Design',
        permalink: '',
        image: '',
    },
    {
        title: 'Fonds d\'écran abstraits',
        description: 'Collection de 25 fonds d\'écran 4K pour ordinateur et mobile.',
        price: 0,
        category: 'Design',
        permalink: '',
        image: '',
    },
];

// ============================================================
//  RENDERING — no need to edit below
// ============================================================
const ALL = 'Tous';
const gradients = [
    'linear-gradient(135deg, #6366f1 0%, #a855f7 100%)',
    'linear-gradient(135deg, #db2777 0%, #f97316 100%)',
    'linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%)',
    'linear-gradient(135deg, #10b981 0%, #06b6d4 100%)',
];

const storeUrl = `https://${STORE.gumroadUsername}.gumroad.com`;

function productUrl(product) {
    return product.permalink ? `${storeUrl}/l/${product.permalink}` : storeUrl;
}

function formatPrice(price) {
    return price > 0 ? `${price} ${STORE.currency}` : 'Gratuit';
}

function createCard(product, index) {
    const card = document.createElement('article');
    card.className = 'product-card';
    card.dataset.category = product.category;
    card.dataset.search = `${product.title} ${product.description} ${product.category}`.toLowerCase();

    const thumb = document.createElement('div');
    thumb.className = 'product-thumb';
    if (product.image) {
        const img = document.createElement('img');
        img.src = product.image;
        img.alt = product.title;
        img.loading = 'lazy';
        thumb.appendChild(img);
    } else {
        thumb.style.background = gradients[index % gradients.length];
        thumb.textContent = product.title.charAt(0);
    }

    const body = document.createElement('div');
    body.className = 'product-body';

    const category = document.createElement('span');
    category.className = 'product-category';
    category.textContent = product.category;

    const title = document.createElement('h2');
    title.className = 'product-title';
    title.textContent = product.title;

    const desc = document.createElement('p');
    desc.className = 'product-desc';
    desc.textContent = product.description;

    const footer = document.createElement('div');
    footer.className = 'product-footer';

    const price = document.createElement('span');
    price.className = 'product-price';
    price.textContent = formatPrice(product.price);

    const buy = document.createElement('a');
    buy.className = 'buy-btn';
    buy.href = productUrl(product);
    buy.target = '_blank';
    buy.rel = 'noopener';
    buy.textContent = product.price > 0 ? 'Acheter' : 'Télécharger';

    footer.append(price, buy);
    body.append(category, title, desc, footer);
    card.append(thumb, body);
    return card;
}

function renderStore() {
    document.getElementById('storeBrand').textContent = STORE.name;
    document.getElementById('storeName').textContent = STORE.name;
    document.getElementById('storeBio').textContent = STORE.bio;
    document.getElementById('storeAvatar').textContent = STORE.name.charAt(0).toUpperCase();
    document.getElementById('gumroadProfileLink').href = storeUrl;

    const grid = document.getElementById('productGrid');
    PRODUCTS.forEach((product, i) => grid.appendChild(createCard(product, i)));

    const categories = [ALL, ...new Set(PRODUCTS.map(p => p.category))];
    const chips = document.getElementById('filterChips');
    categories.forEach(cat => {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'chip';
        chip.textContent = cat;
        chip.setAttribute('aria-pressed', String(cat === ALL));
        chip.addEventListener('click', () => {
            chips.querySelectorAll('.chip').forEach(c => c.setAttribute('aria-pressed', 'false'));
            chip.setAttribute('aria-pressed', 'true');
            applyFilters();
        });
        chips.appendChild(chip);
    });

    document.getElementById('productSearch').addEventListener('input', applyFilters);
}

// Cards are shown/hidden rather than re-rendered, so Gumroad's overlay keeps working on every link
function applyFilters() {
    const query = document.getElementById('productSearch').value.trim().toLowerCase();
    const active = document.querySelector('.chip[aria-pressed="true"]').textContent;
    let visible = 0;

    document.querySelectorAll('.product-card').forEach(card => {
        const show = (active === ALL || card.dataset.category === active) &&
            card.dataset.search.includes(query);
        card.hidden = !show;
        if (show) visible++;
    });

    document.getElementById('emptyState').hidden = visible > 0;
}

renderStore();
