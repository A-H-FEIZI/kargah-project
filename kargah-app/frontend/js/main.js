// ============================================================
// Kargah — main.js  (Masters listing page)
// Week 5 task: read every line and understand what it does.
// Week 9 task: add city filter, improve card UI.
// ============================================================

const API_BASE = "http://127.0.0.1:8000";

const masterGrid    = document.getElementById("master-grid");
const loadingEl     = document.getElementById("loading");
const emptyStateEl  = document.getElementById("empty-state");
const searchInput   = document.getElementById("search-input");
const categoryFilter = document.getElementById("category-filter");

// ---- Boot ----
loadCategories();
loadMasters();

// ============================================================
// Load categories into the <select> dropdown
// ============================================================
async function loadCategories() {
  try {
    const res = await fetch(`${API_BASE}/categories`);
    const categories = await res.json();
    categories.forEach((cat) => {
      const option = document.createElement("option");
      option.value = cat.id;
      option.textContent = `${cat.emoji} ${cat.name}`;
      categoryFilter.appendChild(option);
    });
  } catch (err) {
    console.error("Could not load categories:", err);
  }
}

// ============================================================
// Load masters from the API
// ============================================================
async function loadMasters(filters = {}) {
  showLoading();
  const params = new URLSearchParams();
  if (filters.search)     params.append("search", filters.search);
  if (filters.categoryId) params.append("category_id", filters.categoryId);

  try {
    const res = await fetch(`${API_BASE}/masters?${params}`);
    if (!res.ok) throw new Error(`Server error ${res.status}`);
    const masters = await res.json();
    renderMasters(masters);
  } catch (err) {
    console.error("Could not load masters:", err);
    showEmpty();
  }
}

// ============================================================
// Render master cards
// ============================================================
function renderMasters(masters) {
  masterGrid.innerHTML = "";
  if (masters.length === 0) { showEmpty(); return; }

  masters.forEach((master) => masterGrid.appendChild(createMasterCard(master)));
  showGrid();
}

function createMasterCard(master) {
  const card = document.createElement("a");
  card.href = `master.html?id=${master.id}`;
  card.className = "artisan-card";

  const emoji = master.category_emoji || "🎨";
  card.innerHTML = `
    <div class="card-image">${emoji}</div>
    <div class="card-body">
      <div class="card-name">${master.name}</div>
      <span class="card-category">${master.category_name || "Artisan"}</span>
      <div class="card-city">${master.city || "Iran"}</div>
      ${master.years_exp ? `<div class="card-exp" style="font-size:0.8rem;color:#888;margin-top:4px;">${master.years_exp} years experience</div>` : ""}
      <p class="card-bio">${master.bio || ""}</p>
    </div>
  `;
  return card;
}

// ============================================================
// Filter actions
// ============================================================
function applyFilters() {
  loadMasters({ search: searchInput.value.trim(), categoryId: categoryFilter.value });
}

function clearFilters() {
  searchInput.value = "";
  categoryFilter.value = "";
  loadMasters();
}

searchInput.addEventListener("keydown", (e) => { if (e.key === "Enter") applyFilters(); });

// ============================================================
// UI helpers
// ============================================================
function showLoading() {
  loadingEl.classList.remove("hidden");
  masterGrid.classList.add("hidden");
  emptyStateEl.classList.add("hidden");
}
function showGrid() {
  loadingEl.classList.add("hidden");
  masterGrid.classList.remove("hidden");
  emptyStateEl.classList.add("hidden");
}
function showEmpty() {
  loadingEl.classList.add("hidden");
  masterGrid.classList.add("hidden");
  emptyStateEl.classList.remove("hidden");
}
