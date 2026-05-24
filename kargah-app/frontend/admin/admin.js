// ============================================================
// Kargah — admin.js  (Masters + Sessions management)
// Week 10 task: replace sessionStorage auth with real tokens.
// ============================================================

const API_BASE = "http://127.0.0.1:8000";

if (!sessionStorage.getItem("kargah_admin")) {
  window.location.href = "login.html";
}

// ---- Boot ----
loadCategories();
loadMasters();
loadSessions();

// ============================================================
// Categories — populate dropdowns
// ============================================================
async function loadCategories() {
  try {
    const cats = await fetch(`${API_BASE}/categories`).then(r => r.json());
    const mCat = document.getElementById("m-category");
    cats.forEach(c => {
      const o = new Option(`${c.emoji} ${c.name}`, c.id);
      mCat.appendChild(o);
    });
  } catch (e) { console.error(e); }
}

// ============================================================
// MASTERS
// ============================================================
async function loadMasters() {
  document.getElementById("masters-loading").classList.remove("hidden");
  document.getElementById("masters-table").classList.add("hidden");

  try {
    const masters = await fetch(`${API_BASE}/masters`).then(r => r.json());

    // Also populate the master select in the session form
    const sMaster = document.getElementById("s-master");
    sMaster.innerHTML = '<option value="">Select master...</option>';
    masters.forEach(m => sMaster.appendChild(new Option(`${m.category_emoji || ""} ${m.name} (${m.city || "?"})`, m.id)));

    const tbody = document.getElementById("masters-tbody");
    tbody.innerHTML = "";
    masters.forEach(m => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${m.id}</td>
        <td><strong>${m.name}</strong></td>
        <td>${m.category_name || "—"}</td>
        <td>${m.city || "—"}</td>
        <td>${m.years_exp ? m.years_exp + " yrs" : "—"}</td>
        <td><button class="btn btn-danger" onclick="deleteMaster(${m.id},'${m.name.replace(/'/g,"\\'")}')">Delete</button></td>
      `;
      tbody.appendChild(tr);
    });

    document.getElementById("masters-loading").classList.add("hidden");
    document.getElementById("masters-table").classList.remove("hidden");
  } catch (e) {
    showAlert("master-alert", "Could not load masters. Is the backend running?", "error");
    document.getElementById("masters-loading").classList.add("hidden");
  }
}

document.getElementById("add-master-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = {
    name:          document.getElementById("m-name").value.trim(),
    category_id:   parseInt(document.getElementById("m-category").value) || null,
    city:          document.getElementById("m-city").value.trim(),
    years_exp:     parseInt(document.getElementById("m-exp").value) || null,
    bio:           document.getElementById("m-bio").value.trim(),
    contact_email: document.getElementById("m-email").value.trim(),
  };
  try {
    const res = await fetch(`${API_BASE}/masters`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error((await res.json()).detail || "Failed");
    showAlert("master-alert", `"${data.name}" added.`, "success");
    e.target.reset();
    loadMasters();
  } catch (err) {
    showAlert("master-alert", err.message, "error");
  }
});

async function deleteMaster(id, name) {
  if (!confirm(`Delete master "${name}"? Their sessions will also be removed.`)) return;
  try {
    const res = await fetch(`${API_BASE}/masters/${id}`, { method: "DELETE" });
    if (!res.ok) throw new Error("Failed");
    showAlert("master-alert", `"${name}" deleted.`, "success");
    loadMasters();
    loadSessions();
  } catch (err) {
    showAlert("master-alert", err.message, "error");
  }
}

// ============================================================
// SESSIONS
// ============================================================
const SESSION_ICONS = { studio: "🏛️", mobile: "🚐", commission: "✉️" };

async function loadSessions() {
  document.getElementById("sessions-loading").classList.remove("hidden");
  document.getElementById("sessions-table").classList.add("hidden");

  try {
    const sessions = await fetch(`${API_BASE}/sessions`).then(r => r.json());
    const tbody = document.getElementById("sessions-tbody");
    tbody.innerHTML = "";
    sessions.forEach(s => {
      const tr = document.createElement("tr");
      tr.innerHTML = `
        <td>${s.id}</td>
        <td><strong>${s.title}</strong></td>
        <td>${SESSION_ICONS[s.type] || ""} ${s.type}</td>
        <td>${s.master_name || "—"}</td>
        <td>${s.duration_hr ? s.duration_hr + "h" : "—"}</td>
        <td>${s.price_range || "—"}</td>
        <td><button class="btn btn-danger" onclick="deleteSession(${s.id},'${s.title.replace(/'/g,"\\'")}')">Delete</button></td>
      `;
      tbody.appendChild(tr);
    });
    document.getElementById("sessions-loading").classList.add("hidden");
    document.getElementById("sessions-table").classList.remove("hidden");
  } catch (e) {
    showAlert("session-alert", "Could not load sessions.", "error");
    document.getElementById("sessions-loading").classList.add("hidden");
  }
}

document.getElementById("add-session-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const data = {
    master_id:   parseInt(document.getElementById("s-master").value),
    title:       document.getElementById("s-title").value.trim(),
    type:        document.getElementById("s-type").value,
    duration_hr: parseFloat(document.getElementById("s-duration").value) || null,
    max_people:  parseInt(document.getElementById("s-people").value) || 1,
    price_range: document.getElementById("s-price").value.trim(),
    description: document.getElementById("s-desc").value.trim(),
  };
  try {
    const res = await fetch(`${API_BASE}/sessions`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    if (!res.ok) throw new Error((await res.json()).detail || "Failed");
    showAlert("session-alert", `Session "${data.title}" added.`, "success");
    e.target.reset();
    loadSessions();
  } catch (err) {
    showAlert("session-alert", err.message, "error");
  }
});

async function deleteSession(id, title) {
  if (!confirm(`Delete session "${title}"?`)) return;
  try {
    const res = await fetch(`${API_BASE}/sessions/${id}`, { method: "DELETE" });
    if (!res.ok) throw new Error("Failed");
    showAlert("session-alert", `"${title}" deleted.`, "success");
    loadSessions();
  } catch (err) {
    showAlert("session-alert", err.message, "error");
  }
}

// ============================================================
// Helpers
// ============================================================
function showAlert(elId, msg, type = "success") {
  const el = document.getElementById(elId);
  el.textContent = msg;
  el.className = `alert alert-${type}`;
  setTimeout(() => { el.className = "alert hidden"; }, 4000);
}

function logout() {
  sessionStorage.removeItem("kargah_admin");
  window.location.href = "login.html";
}
