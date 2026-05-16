document.addEventListener("DOMContentLoaded", () => {
  setupMobileMenu();
  setupQuantityControls();
  setupCartSummary();
  setupCheckoutSteps();
  setupCatalogFilters();
});

function setupMobileMenu() {
  const trigger = document.querySelector("[data-menu-toggle]");
  const menu = document.querySelector("[data-menu]");

  if (!trigger || !menu) return;

  trigger.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });
}

function setupQuantityControls() {
  const wrappers = document.querySelectorAll("[data-qty-wrap]");
  if (!wrappers.length) return;

  wrappers.forEach((wrapper) => {
    const input = wrapper.querySelector("[data-qty-input]");
    if (!input) return;

    wrapper.querySelector("[data-qty-minus]")?.addEventListener("click", () => {
      const current = Number(input.value) || 1;
      input.value = Math.max(1, current - 1);
    });

    wrapper.querySelector("[data-qty-plus]")?.addEventListener("click", () => {
      const current = Number(input.value) || 1;
      input.value = Math.min(15, current + 1);
    });
  });
}

function setupCartSummary() {
  const container = document.querySelector("[data-cart-lines]");
  if (!container) return;

  const subtotalTarget = document.querySelector("[data-subtotal]");
  const taxTarget = document.querySelector("[data-tax]");
  const totalTarget = document.querySelector("[data-total]");

  const update = () => {
    const rows = [...container.querySelectorAll("[data-cart-item]")];
    const subtotal = rows.reduce((acc, row) => {
      const price = Number(row.dataset.price || 0);
      const qtyInput = row.querySelector("[data-qty-input]");
      const qty = Number(qtyInput?.value || 1);
      const lineTotal = price * qty;
      const target = row.querySelector("[data-line-total]");
      if (target) target.textContent = formatMoney(lineTotal);
      return acc + lineTotal;
    }, 0);

    const tax = subtotal * 0.2;
    const total = subtotal + tax;

    if (subtotalTarget) subtotalTarget.textContent = formatMoney(subtotal);
    if (taxTarget) taxTarget.textContent = formatMoney(tax);
    if (totalTarget) totalTarget.textContent = formatMoney(total);
  };

  container.addEventListener("click", (event) => {
    const minus = event.target.closest("[data-qty-minus]");
    const plus = event.target.closest("[data-qty-plus]");
    if (!minus && !plus) return;

    const row = event.target.closest("[data-cart-item]");
    const input = row?.querySelector("[data-qty-input]");
    if (!input) return;

    const current = Number(input.value) || 1;
    if (minus) input.value = Math.max(1, current - 1);
    if (plus) input.value = Math.min(20, current + 1);
    update();
  });

  container.addEventListener("change", (event) => {
    if (!event.target.matches("[data-qty-input]")) return;
    const normalized = Math.max(1, Math.min(20, Number(event.target.value) || 1));
    event.target.value = normalized;
    update();
  });

  update();
}

function setupCheckoutSteps() {
  const root = document.querySelector("[data-checkout]");
  if (!root) return;

  const steps = [...root.querySelectorAll("[data-step]")];
  const dots = [...root.querySelectorAll("[data-step-dot]")];
  const nextBtn = root.querySelector("[data-next]");
  const prevBtn = root.querySelector("[data-prev]");
  const finishBtn = root.querySelector("[data-finish]");
  const status = root.querySelector("[data-status]");

  let current = 0;

  const render = () => {
    steps.forEach((step, index) => {
      step.classList.toggle("hidden", index !== current);
    });

    dots.forEach((dot, index) => {
      dot.classList.remove("active", "done");
      if (index < current) dot.classList.add("done");
      if (index === current) dot.classList.add("active");
    });

    if (prevBtn) prevBtn.disabled = current === 0;
    if (nextBtn) nextBtn.classList.toggle("hidden", current === steps.length - 1);
    if (finishBtn) finishBtn.classList.toggle("hidden", current !== steps.length - 1);

    if (status) {
      status.textContent = `Paso ${current + 1} de ${steps.length}`;
    }
  };

  nextBtn?.addEventListener("click", () => {
    current = Math.min(steps.length - 1, current + 1);
    render();
  });

  prevBtn?.addEventListener("click", () => {
    current = Math.max(0, current - 1);
    render();
  });

  finishBtn?.addEventListener("click", () => {
    if (!status) return;
    status.textContent = "Pago simulado enviado. Prototipo listo para validacion.";
  });

  render();
}

function setupCatalogFilters() {
  const grid = document.querySelector("[data-catalog-grid]");
  const category = document.querySelector("[data-filter-category]");
  const size = document.querySelector("[data-filter-size]");
  if (!grid || !category || !size) return;

  const cards = [...grid.querySelectorAll("[data-category]")];

  const applyFilters = () => {
    const catValue = category.value;
    const sizeValue = size.value;

    cards.forEach((card) => {
      const cardCategory = card.dataset.category;
      const cardSizes = (card.dataset.sizes || "").split(",");

      const categoryOk = catValue === "all" || cardCategory === catValue;
      const sizeOk = sizeValue === "all" || cardSizes.includes(sizeValue);

      card.classList.toggle("hidden", !(categoryOk && sizeOk));
    });
  };

  category.addEventListener("change", applyFilters);
  size.addEventListener("change", applyFilters);
}

function formatMoney(value) {
  return new Intl.NumberFormat("fr-FR", {
    style: "currency",
    currency: "EUR",
  }).format(value);
}
