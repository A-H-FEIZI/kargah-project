// ============================================================
// Kargah — master.js  (Master profile + sessions page)
// The master ID comes from the URL: master.html?id=3
// ============================================================

const API_BASE = "http://127.0.0.1:8000";

const SESSION_LABELS = {
  studio:     { icon: "🏛️", label: "Studio Session",   color: "#8b4513" },
  mobile:     { icon: "🚐", label: "Mobile (سیار)",    color: "#2e7d32" },
  commission: { icon: "✉️", label: "Custom Commission", color: "#1565c0" },
};

function getIdFromUrl() {
  return new URLSearchParams(window.location.search).get("id");
}

async function loadMaster() {
  const id = getIdFromUrl();
  if (!id) { showNotFound(); return; }

  try {
    const res = await fetch(`${API_BASE}/masters/${id}`);
    if (res.status === 404) { showNotFound(); return; }
    if (!res.ok) throw new Error();
    const master = await res.json();
    renderMaster(master);
    loadSessions(id);
  } catch {
    showNotFound();
  }
}

function renderMaster(master) {
  document.title = `${master.name} — Kargah`;
  document.getElementById("avatar").textContent       = master.category_emoji || "🎨";
  document.getElementById("master-name").textContent  = master.name;
  document.getElementById("master-category").textContent = master.category_name || "Artisan";
  document.getElementById("master-city").textContent  = master.city || "Iran";
  document.getElementById("master-bio").textContent   = master.bio || "No biography available.";

  if (master.years_exp) {
    document.getElementById("master-exp").textContent = `${master.years_exp} years of experience`;
  }

  const emailEl = document.getElementById("master-email");
  if (master.contact_email) {
    emailEl.href        = `mailto:${master.contact_email}`;
    emailEl.textContent = master.contact_email;
  } else {
    emailEl.textContent = "Not provided";
  }

  document.getElementById("loading").classList.add("hidden");
  document.getElementById("profile").classList.remove("hidden");
}

async function loadSessions(masterId) {
  try {
    const res = await fetch(`${API_BASE}/masters/${masterId}/sessions`);
    const sessions = await res.json();

    document.getElementById("sessions-loading").classList.add("hidden");

    if (sessions.length === 0) {
      document.getElementById("sessions-empty").classList.remove("hidden");
      return;
    }

    const grid = document.getElementById("sessions-grid");
    sessions.forEach((s) => grid.appendChild(createSessionCard(s)));
    grid.classList.remove("hidden");
  } catch {
    document.getElementById("sessions-loading").classList.add("hidden");
    document.getElementById("sessions-empty").classList.remove("hidden");
  }
}

function createSessionCard(session) {
  const meta     = SESSION_LABELS[session.type] || { icon: "🎨", label: session.type, color: "#555" };
  const duration = session.duration_hr ? `${session.duration_hr}h` : "";
  const people   = session.max_people  ? `Up to ${session.max_people} people` : "";

  const card = document.createElement("div");
  card.className = "artisan-card";
  card.style.cursor = "default";
  card.innerHTML = `
    <div class="card-image" style="font-size:2rem;">${meta.icon}</div>
    <div class="card-body">
      <div class="card-name">${session.title}</div>
      <span class="card-category" style="background:${meta.color};">${meta.label}</span>
      <div style="font-size:0.82rem; color:#777; margin-top:6px;">
        ${duration ? `⏱ ${duration}` : ""}
        ${people   ? `&nbsp;· 👥 ${people}` : ""}
      </div>
      <p class="card-bio" style="margin-top:8px;">${session.description || ""}</p>
      ${session.price_range
        ? `<div style="margin-top:10px; font-weight:600; color:#8b4513; font-size:0.9rem;">💰 ${session.price_range}</div>`
        : ""}
      <button class="btn btn-primary" style="margin-top:12px; width:100%;"
              onclick="openBooking(${session.id}, '${session.title.replace(/'/g,"\\'")}')">
        Request This Session
      </button>
    </div>
  `;
  return card;
}

async function openBooking(sessionId, title) {
  const name  = prompt(`Your name (for: "${title}"):`);
  if (!name) return;
  const email = prompt("Your email address:");
  if (!email) return;
  const msg   = prompt("Message for the master? (optional)") || "";

  try {
    const res = await fetch(`${API_BASE}/booking-requests`, {
      method:  "POST",
      headers: { "Content-Type": "application/json" },
      body:    JSON.stringify({ session_id: sessionId, seeker_name: name, seeker_email: email, message: msg }),
    });
    if (!res.ok) throw new Error();
    alert("✅ Request sent! The master will contact you.");
  } catch {
    alert("❌ Could not send request. Is the backend running?");
  }
}

function showNotFound() {
  document.getElementById("loading").classList.add("hidden");
  document.getElementById("not-found").classList.remove("hidden");
}

loadMaster();
