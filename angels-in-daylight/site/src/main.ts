import './style.css'

interface Variant {
  color: string;
  image: string;
}

interface Product {
  sku: string;
  name: string;
  category: string;
  price: number;
  image: string;
  description: string;
  variants?: Variant[];
}

const productsData: Product[] = [
  {
    sku: "DAY-M-011",
    name: "Heavyweight Gothic Hoodie",
    category: "Hoodies",
    price: 120.00,
    image: "/products/DAY-M-011-black.jpg",
    description: "Premium heavyweight black cotton fleece featuring white gothic puff-print Angels in Daylight logo."
  },
  {
    sku: "DAY-M-025",
    name: "Logo Gothic Leather Shorts",
    category: "Bottoms",
    price: 180.00,
    image: "/products/DAY-M-025-black-tone.jpg", // Default is black tone-on-tone
    description: "Matte black streetwear leather shorts featuring custom embossed or embroidered gothic brand lettering.",
    variants: [
      { color: "Black", image: "/products/DAY-M-025-black-tone.jpg" },
      { color: "Pink", image: "/products/DAY-M-025-black-pink.jpg" },
      { color: "Blue", image: "/products/DAY-M-025-black-blue.jpg" }
    ]
  },
  {
    sku: "DAY-R-006",
    name: "Rhinestone Cross Denim Shorts",
    category: "Capsules",
    price: 95.00,
    image: "/products/DAY-R-006-indigo.jpg",
    description: "Vintage indigo wash denim shorts featuring a hand-encrusted rhinestone gothic cross on the front utility pocket."
  },
  {
    sku: "DAY-R-004",
    name: "Studded Rhinestone Leather Jacket",
    category: "Capsules",
    price: 290.00,
    image: "/products/rhinestone-jacket.png",
    description: "Double-breasted black leather biker jacket with custom hand-set rhinestone detailing across back panels."
  },
  {
    sku: "DAY-M-020",
    name: "Wings Backprint Varsity Jacket",
    category: "Hoodies",
    price: 210.00,
    image: "/products/wings-backprint-jacket.png",
    description: "Wool varsity jacket featuring leather sleeves and detailed angel wing backprint embroidery."
  },
  {
    sku: "DAY-M-008",
    name: "Graphic Winged Angel Tee",
    category: "Tops",
    price: 55.00,
    image: "/products/hero-winged-tee.png",
    description: "Soft vintage-wash white cotton tee featuring high-fidelity classical angel graphic chest print."
  },
  {
    sku: "DAY-M-001",
    name: "Blackletter Logo Basic Tee",
    category: "Tops",
    price: 45.00,
    image: "/products/blackletter-tee.png",
    description: "Standard streetwear black cotton tee featuring minimalist white blackletter brand text."
  },
  {
    sku: "DAY-M-009",
    name: "Graffiti Tag Jersey Tee",
    category: "Tops",
    price: 65.00,
    image: "/products/graffiti-tag-tee.png",
    description: "Dark grey jersey paneled tee featuring print graffiti details and numbers."
  }
];

// App State
let cart: { product: Product; quantity: number; selectedColor?: string }[] = [];
let activeCategory = "All";

// DOM Scaffolding
const app = document.querySelector<HTMLDivElement>('#app')!;

app.innerHTML = `
  <!-- Header -->
  <header class="store-header">
    <div class="brand-title">
      Angels in Daylight <span class="brand-tag">DAY</span>
    </div>
    
    <nav class="nav-links">
      <a href="#" class="nav-link active" data-category="All">Shop Collection</a>
    </nav>
    
    <div class="header-actions">
      <button class="cart-trigger" id="cartTriggerBtn">
        <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="9" cy="21" r="1"></circle>
          <circle cx="20" cy="21" r="1"></circle>
          <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
        </svg>
        <span>Cart</span>
        <span class="cart-count" id="cartCountBadge">0</span>
      </button>
    </div>
  </header>

  <!-- Hero Highlight -->
  <section class="hero-section">
    <div class="hero-content">
      <h1>Angels in <span>Daylight</span></h1>
      <p>Official 2026 Collection drops. Clean silhouettes, premium heavyweight fabrics, and gothic typography accents. Free global shipping on all capsules.</p>
      <button class="action-btn" id="btnHeroShop">Explore Capsule</button>
    </div>
    <div class="hero-image-container">
      <img src="/products/DAY-M-011-black.jpg" alt="DAY-M-011 Heavyweight Gothic Hoodie" class="hero-image">
    </div>
  </section>

  <!-- Filter Navigation Pills -->
  <div class="filter-tabs" id="filterTabsContainer">
    <!-- Rendered dynamically -->
  </div>

  <!-- Main Catalog Grid -->
  <section class="catalog-section">
    <div class="products-grid" id="productsGrid">
      <!-- Injected dynamically -->
    </div>
  </section>

  <!-- Cart Drawer -->
  <div class="cart-drawer" id="cartDrawer">
    <div class="cart-header">
      <h2>Shopping Cart</h2>
      <button class="close-btn" id="btnCloseCart">&times;</button>
    </div>
    <div class="cart-items" id="cartItemsContainer">
      <!-- Injected dynamically -->
    </div>
    <div class="cart-footer">
      <div class="cart-total-row">
        <span>Subtotal</span>
        <span id="cartSubtotalText">$0.00</span>
      </div>
      <button class="checkout-btn" id="btnCheckout">Proceed to Checkout</button>
    </div>
  </div>

  <!-- Toast Notification -->
  <div class="toast-msg" id="toastMsg">Added to cart!</div>
`;

// Element References
const productsGrid = document.getElementById("productsGrid")!;
const filterTabsContainer = document.getElementById("filterTabsContainer")!;
const cartTriggerBtn = document.getElementById("cartTriggerBtn")!;
const cartDrawer = document.getElementById("cartDrawer")!;
const btnCloseCart = document.getElementById("btnCloseCart")!;
const cartItemsContainer = document.getElementById("cartItemsContainer")!;
const cartSubtotalText = document.getElementById("cartSubtotalText")!;
const cartCountBadge = document.getElementById("cartCountBadge")!;
const toastMsg = document.getElementById("toastMsg")!;
const btnCheckout = document.getElementById("btnCheckout")!;
const btnHeroShop = document.getElementById("btnHeroShop")!;

// Toast utility
function triggerToast(message: string) {
  toastMsg.textContent = message;
  toastMsg.classList.add("show");
  setTimeout(() => {
    toastMsg.classList.remove("show");
  }, 2200);
}

// Render Products Grid
function renderCatalog() {
  const filtered = activeCategory === "All" 
    ? productsData 
    : productsData.filter(p => p.category === activeCategory);
    
  if (filtered.length === 0) {
    productsGrid.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: var(--text-muted); padding: 40px 0;">No items found in this section.</div>`;
    return;
  }
  
  productsGrid.innerHTML = filtered.map(p => {
    // Generate colorway selector HTML if variants exist
    let colorwayHtml = "";
    if (p.variants) {
      colorwayHtml = `
        <div class="color-selectors" style="display:flex; gap:8px; margin: 10px 0;">
          ${p.variants.map((v, i) => {
            let bgStyle = "";
            if (v.color === "Black") bgStyle = "background: #000; border: 1px solid var(--border-glass-glow);";
            else if (v.color === "Pink") bgStyle = "background: #e272a2; border: 1px solid transparent;";
            else if (v.color === "Blue") bgStyle = "background: #4a779d; border: 1px solid transparent;";
            
            return `
              <span class="color-dot ${i === 0 ? 'active' : ''}" 
                    style="${bgStyle} width:14px; height:14px; border-radius:50%; cursor:pointer; display:inline-block; transition:transform 0.15s ease;"
                    data-color="${v.color}"
                    data-img="${v.image}"
                    data-sku="${p.sku}"></span>
            `;
          }).join("")}
        </div>
      `;
    }

    return `
      <div class="product-card" data-sku="${p.sku}">
        <div class="card-img-wrapper">
          <img src="${p.image}" alt="${p.name}" class="card-img" id="img-${p.sku}">
        </div>
        <div class="card-meta">
          <span class="card-sku">${p.sku}</span>
          <span class="card-category">${p.category}</span>
        </div>
        <h3 class="card-title">${p.name}</h3>
        ${colorwayHtml}
        <div class="card-footer">
          <span class="card-price">$${p.price.toFixed(2)}</span>
          <button class="add-to-cart-btn" data-sku="${p.sku}">
            <svg viewBox="0 0 24 24">
              <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
            </svg>
          </button>
        </div>
      </div>
    `;
  }).join("");
  
  // Wire color dots listeners
  document.querySelectorAll(".color-dot").forEach(dot => {
    dot.addEventListener("click", (e) => {
      const el = e.currentTarget as HTMLElement;
      const sku = el.getAttribute("data-sku")!;
      const img = el.getAttribute("data-img")!;
      
      // Update image
      const imgEl = document.getElementById(`img-${sku}`) as HTMLImageElement;
      if (imgEl) {
        imgEl.src = img;
      }
      
      // Update active dot styling
      const siblingDots = el.parentNode?.querySelectorAll(".color-dot");
      siblingDots?.forEach(d => d.classList.remove("active"));
      el.classList.add("active");
    });
  });

  // Bind Cart Add buttons
  productsGrid.querySelectorAll(".add-to-cart-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const sku = btn.getAttribute("data-sku")!;
      // Find currently selected variant color on card
      const cardEl = btn.closest(".product-card")!;
      const activeDot = cardEl.querySelector(".color-dot.active") as HTMLElement | null;
      const color = activeDot ? activeDot.getAttribute("data-color")! : undefined;
      
      addToCart(sku, color);
    });
  });
}

// Render Category Filter Pills
function renderFilters() {
  const categories = ["All", "Hoodies", "Bottoms", "Tops", "Capsules"];
  
  filterTabsContainer.innerHTML = categories.map(cat => `
    <button class="filter-tab ${cat === activeCategory ? 'active' : ''}" data-category="${cat}">
      ${cat}
    </button>
  `).join("");
  
  filterTabsContainer.querySelectorAll(".filter-tab").forEach(tab => {
    tab.addEventListener("click", () => {
      activeCategory = tab.getAttribute("data-category")!;
      renderFilters();
      renderCatalog();
    });
  });
}

// Cart Manager Functions
function addToCart(sku: string, color?: string) {
  const product = productsData.find(p => p.sku === sku);
  if (!product) return;
  
  const existing = cart.find(item => item.product.sku === sku && item.selectedColor === color);
  if (existing) {
    existing.quantity++;
  } else {
    cart.push({ product, quantity: 1, selectedColor: color });
  }
  
  updateCartUI();
  triggerToast(`Added: ${product.name}${color ? ` (${color})` : ""}`);
}

function removeFromCart(sku: string, color?: string) {
  cart = cart.filter(item => !(item.product.sku === sku && item.selectedColor === color));
  updateCartUI();
}

function updateCartUI() {
  if (cart.length === 0) {
    cartItemsContainer.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 40px 0; font-size: 0.9rem;">Your cart is empty.</div>`;
  } else {
    cartItemsContainer.innerHTML = cart.map(item => {
      // Pick variant image if color selected
      let displayImg = item.product.image;
      if (item.selectedColor && item.product.variants) {
        const v = item.product.variants.find(x => x.color === item.selectedColor);
        if (v) displayImg = v.image;
      }

      return `
        <div class="cart-item">
          <img src="${displayImg}" alt="${item.product.name}" class="cart-item-img">
          <div class="cart-item-details">
            <div class="cart-item-title">${item.product.name} ${item.selectedColor ? `<span style="color:var(--accent-pink); font-size:0.8rem;">(${item.selectedColor})</span>` : ""}</div>
            <div class="cart-item-price">$${item.product.price.toFixed(2)} &times; ${item.quantity}</div>
            <button class="remove-item-btn" data-sku="${item.product.sku}" data-color="${item.selectedColor || ''}">Remove</button>
          </div>
        </div>
      `;
    }).join("");
    
    // Bind remove clicks
    cartItemsContainer.querySelectorAll(".remove-item-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const sku = btn.getAttribute("data-sku")!;
        const color = btn.getAttribute("data-color") || undefined;
        removeFromCart(sku, color);
      });
    });
  }
  
  // Update totals
  const total = cart.reduce((sum, item) => sum + (item.product.price * item.quantity), 0);
  const totalQty = cart.reduce((sum, item) => sum + item.quantity, 0);
  
  cartSubtotalText.textContent = `$${total.toFixed(2)}`;
  cartCountBadge.textContent = String(totalQty);
}

// Cart Drawer Visibility listeners
cartTriggerBtn.addEventListener("click", () => {
  cartDrawer.classList.toggle("open");
});

btnCloseCart.addEventListener("click", () => {
  cartDrawer.classList.remove("open");
});

btnCheckout.addEventListener("click", () => {
  if (cart.length === 0) {
    triggerToast("Your cart is empty!");
  } else {
    triggerToast("Proceeding to simulated checkout...");
    cart = [];
    updateCartUI();
    setTimeout(() => {
      cartDrawer.classList.remove("open");
    }, 1500);
  }
});

btnHeroShop.addEventListener("click", (e) => {
  e.preventDefault();
  filterTabsContainer.scrollIntoView({ behavior: "smooth" });
});

// App Initialization
function init() {
  renderFilters();
  renderCatalog();
  updateCartUI();
}

init();
