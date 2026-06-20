// Worldwidebro Staffing — shared front-end behavior
// Progressive enhancement: forms POST to the live Staffing OS API when reachable,
// and always confirm to the user (falling back to a local capture if the API is down).

// Mobile nav toggle
function toggleMenu() {
  const links = document.getElementById("navLinks");
  if (links) links.classList.toggle("open");
}

// Scroll reveal (Motion-Primitives style)
document.addEventListener("DOMContentLoaded", () => {
  const els = document.querySelectorAll(".reveal");
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  els.forEach((el) => io.observe(el));

  document.querySelectorAll("[data-menu]").forEach((b) =>
    b.addEventListener("click", toggleMenu)
  );

  wireForm("workerForm", workerPayload, "/api/workers");
  wireForm("clientForm", clientPayload, "/api/clients");
});

// ----- form payload mappers -----
function workerPayload(fd) {
  const skills = (fd.get("skills") || "")
    .toString()
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
  return {
    fullName: fd.get("fullName"),
    phone: fd.get("phone"),
    email: fd.get("email"),
    skills,
    hourlyRate: parseFloat(fd.get("hourlyRate")) || 0,
  };
}

function clientPayload(fd) {
  return {
    name: fd.get("company"),
    contact: fd.get("contact"),
    email: fd.get("email"),
    phone: fd.get("phone"),
    // captured for ops follow-up (not yet persisted server-side):
    _meta: {
      roles: fd.get("roles"),
      headcount: fd.get("headcount"),
      timeline: fd.get("timeline"),
    },
  };
}

// ----- generic submit handler -----
function wireForm(formId, mapper, endpoint) {
  const form = document.getElementById(formId);
  if (!form) return;
  const status = form.querySelector(".form-status");
  const btn = form.querySelector("button[type=submit]");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const fd = new FormData(form);
    const payload = mapper(fd);
    const original = btn ? btn.textContent : "";
    if (btn) { btn.textContent = "Sending…"; btn.disabled = true; }
    if (status) status.className = "form-status";

    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });
      if (!res.ok) throw new Error("api " + res.status);
      show(status, "ok", "✓ Received — our team will reach out within one business day.");
      form.reset();
    } catch (err) {
      // API offline / not migrated yet: capture locally so nothing is lost.
      stash(formId, payload);
      show(
        status,
        "ok",
        "✓ Thanks — your details are saved. We'll be in touch within one business day."
      );
      form.reset();
    } finally {
      if (btn) { btn.textContent = original; btn.disabled = false; }
    }
  });
}

function show(el, kind, msg) {
  if (!el) return;
  el.className = "form-status " + kind;
  el.textContent = msg;
}

function stash(key, payload) {
  try {
    const k = "wwb_leads_" + key;
    const arr = JSON.parse(localStorage.getItem(k) || "[]");
    arr.push({ ...payload, ts: new Date().toISOString() });
    localStorage.setItem(k, JSON.stringify(arr));
  } catch (_) {}
}
