// ============================================================
// Kargah — sessions.js  (Sessions listing page)
// Week 9 task: add city filter and price range display.
// ============================================================

const API_BASE = "http://127.0.0.1:8000";

const sessionGrid = document.getElementById("session-grid");
const loadingEl   = document.getElementById("loading");
const emptyEl     = document.getElementById("empty-state");

const SESSION_LABELS = {
  studio:     { icon: "🏛️", label: "Studio Session",   color: "#8b4513" },
  mobile:     { icon: "🚐", label: "Mobile (سیار)",    color: "#2e7d32" },
  commission: { icon: "✉️", label: "Custom Commission", color: "#1565c0" },
};

// Read ?type= from URL (set by the homepage quick-filter pills)
const urlParams = new URLSearchParams(window.location.search);
let currentType = urlParams.get("type") || "";

// ---- Boot ----
highlightActiveTab();
loadSessions(currentType);

// ============================================================
// Load sessions
// ============================================================
async function loadSessions(type = "") {
  showLoading();
  const params = new URLSearchParams();
  if (type) params.append("type", type);

  try {
    const res = await fetch(`${API_BASE}/sessions?${params}`);
    if (!res.ok) throw new Error(`Server error ${res.status}`);
    const sessions = await res.json();
    renderSessions(sessions);
  } catch (err) {
    console.error("Could not load sessions:", err);
    showEmpty();
  }
}

// ============================================================
// Filter by type (called by tab buttons)
// ============================================================
function filterByType(type) {
  currentType = type;
  highlightActiveTab();
  loadSessions(type);
}

function highlightActiveTab() {
  ["all", "studio", "mobile", "commission"].forEach((t) => {
    const el = document.getElementById(`tab-${t}`);
    if (!el) return;
    el.className = (currentType === t || (t === "all" && currentType === ""))
      ? "btn btn-primary"
      : "btn btn-secondary";
  });
}

// ============================================================
// Render session cards
// ============================================================
function renderSessions(sessions) {
  sessionGrid.innerHTML = "";
  if (sessions.length === 0) { showEmpty(); return; }

  sessions.forEach((s) => sessionGrid.appendChild(createSessionCard(s)));
  showGrid();
}

function createSessionCard(session) {
  const meta = SESSION_LABELS[session.type] || { icon: "🎨", label: session.type, color: "#555" };
  const duration = session.duration_hr ? `${session.duration_hr}h session` : "";
  const people   = session.max_people  ? `Up to ${session.max_people} people` : "";

  const card = document.createElement("div");
  card.className = "artisan-card";
  card.style.cursor = "default";
  card.innerHTML = `
    <div class="card-image" style="font-size:2.5rem; flex-direction:column; gap:4px;">
      <span>${session.category_emoji || "🎨"}</span>
      <span style="font-size:1.2rem;">${meta.icon}</span>
    </div>
    <div class="card-body">
      <div class="card-name">${session.title}</div>
      <span class="card-category" style="background:${meta.color};">${meta.label}</span>
      <div class="card-city">${session.master_city || "Iran"}</div>
      <div style="font-size:0.82rem; color:#777; margin-top:4px;">
        by <strong>${session.master_name || "—"}</strong>
        ${duration ? `· ${duration}` : ""}
        ${people   ? `· ${people}`   : ""}
      </div>
      <p class="card-bio" style="margin-top:8px;">${session.description || ""}</p>
      ${session.price_range ? `<div style="margin-top:10px; font-weight:600; color:#8b4513; font-size:0.9rem;">💰 ${session.price_range}</div>` : ""}
      <button class="btn btn-primary" style="margin-top:12px; width:100%;"
              onclick="openBooking(${session.id}, '${session.title.replace(/'/g,"\\'")}')">
        Request Booking
      </button>
    </div>
  `;
  return card;
}

// ============================================================
// Booking modal (Week 9 task: build the full booking form here)
// ============================================================
function openBooking(sessionId, sessionTitle) {
  const name  = prompt(`Your name (booking: "${sessionTitle}"):`);
  if (!name) return;
  const email = prompt("Your email address:");
  if (!email) return;
  const msg   = prompt("Any message for the master? (optional)") || "";

  submitBooking(sessionId, name, email, msg);
}

async function submitBooking(sessionId, name, email, message) {
  try {
    const res = await fetch(`${API_BASE}/booking-requests`, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ session_id: sessionId, seeker_name: name, seeker_email: email, message }),
    });
    if (!res.ok) throw new Error("Failed");
    alert("✅ Booking request sent! The master will contact you.");
  } catch {
    alert("❌ Could not send booking request. Is the backend running?");
  }
}

// ============================================================
// UI helpers
// ============================================================
function showLoading() {
  loadingEl.classList.remove("hidden");
  sessionGrid.classList.add("hidden");
  emptyEl.classList.add("hidden");
}
function showGrid() {
  loadingEl.classList.add("hidden");
  sessionGrid.classList.remove("hidden");
  emptyEl.classList.add("hidden");
}
function showEmpty() {
  loadingEl.classList.add("hidden");
  sessionGrid.classList.add("hidden");
  emptyEl.classList.remove("hidden");
}
