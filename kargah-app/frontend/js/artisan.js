// ============================================================
// Kargah — artisan.js
// Loads and renders a single artisan's profile page.
// The artisan ID comes from the URL: artisan.html?id=3
// ============================================================

const API_BASE = "http://127.0.0.1:8000";

const CATEGORY_EMOJI = {
  "Carpet Weaving": "🪡",
  "Pottery":        "🏺",
  "Calligraphy":    "✍️",
  "Miniature":      "🖼️",
  "Metalwork":      "⚒️",
  "Woodcarving":    "🪵",
  "Jewelry":        "💍",
};


// Read the ?id= value from the current URL
function getArtisanIdFromUrl() {
  const params = new URLSearchParams(window.location.search);
  return params.get("id");
}


async function loadArtisan() {
  const artisanId = getArtisanIdFromUrl();

  if (!artisanId) {
    showNotFound();
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/artisans/${artisanId}`);

    if (response.status === 404) {
      showNotFound();
      return;
    }

    if (!response.ok) {
      throw new Error(`Server returned ${response.status}`);
    }

    const artisan = await response.json();
    renderArtisan(artisan);
  } catch (error) {
    console.error("Could not load artisan:", error);
    showNotFound();
  }
}


function renderArtisan(artisan) {
  // Update page title
  document.title = `${artisan.name} — Kargah`;

  // Avatar emoji
  const emoji = CATEGORY_EMOJI[artisan.category_name] || "🎨";
  document.getElementById("avatar").textContent = emoji;

  // Profile fields
  document.getElementById("artisan-name").textContent     = artisan.name;
  document.getElementById("artisan-category").textContent = artisan.category_name || "Artisan";
  document.getElementById("artisan-city").textContent     = artisan.city || "Iran";
  document.getElementById("artisan-bio").textContent      = artisan.bio || "No biography available.";

  // Contact email
  const emailEl = document.getElementById("artisan-email");
  if (artisan.contact_email) {
    emailEl.href        = `mailto:${artisan.contact_email}`;
    emailEl.textContent = artisan.contact_email;
  } else {
    emailEl.textContent = "Not provided";
  }

  // Show the profile, hide loader
  document.getElementById("loading").classList.add("hidden");
  document.getElementById("profile").classList.remove("hidden");
}


function showNotFound() {
  document.getElementById("loading").classList.add("hidden");
  document.getElementById("not-found").classList.remove("hidden");
}


// Boot
loadArtisan();
