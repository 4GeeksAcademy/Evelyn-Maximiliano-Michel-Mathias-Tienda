
// ===============================
// main.js - Script principal
// Organización por página y funcionalidad
// ===============================

// --- Inicialización global (todas las páginas) ---
document.addEventListener("DOMContentLoaded", () => {
  setupMobileMenu(); // Menú responsive (todas las páginas)
  setupQuantityControls(); // Controles de cantidad (carrito, catálogo)
  setupCartSummary(); // Resumen de carrito (carrito.html)
  setupCheckoutSteps(); // Flujo de pasos de checkout (checkout.html)
  setupCatalogFilters(); // Filtros de catálogo (catalogo.html)
  setupOnlyLettersInputs(); // Validación de solo letras (formularios)
});

// ===============================
// Funciones generales (todas las páginas)
// ===============================

// Permite solo letras en inputs marcados con data-only-letters
function setupOnlyLettersInputs() {
  const letterInputs = document.querySelectorAll("input[data-only-letters]");
  if (!letterInputs.length) return;

  letterInputs.forEach((input) => {
    input.addEventListener("input", () => {
      const cleaned = input.value
        .replace(/[^A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]/g, "")
        .replace(/\s{2,}/g, " ")
        .replace(/^\s+/, "");

      if (cleaned !== input.value) {
        input.value = cleaned;
      }
    });
  });
}

// Menú móvil responsive (todas las páginas)
function setupMobileMenu() {
  const trigger = document.querySelector("[data-menu-toggle]");
  const menu = document.querySelector("[data-menu]");

  if (!trigger || !menu) return;

  trigger.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });
}

// ===============================
// Carrito y catálogo: controles de cantidad
// ===============================
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

// ===============================
// Carrito: resumen y totales (carrito.html)
// ===============================
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

// ===============================
// Checkout: pasos, validación y modal (checkout.html)
// ===============================
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
        // Limpiar contenido previo
        dot.innerHTML = "";
        if (index < current) {
          dot.classList.add("done");
          dot.innerHTML = '<span style="color: green; font-size: 1.2em;">✓</span>';
        } else if (index === current) {
          dot.classList.add("active");
          dot.innerHTML = (index + 1).toString();
        } else {
          dot.innerHTML = (index + 1).toString();
        }
    });

    if (prevBtn) prevBtn.disabled = current === 0;
    if (nextBtn) nextBtn.classList.toggle("hidden", current === steps.length - 1);
    if (finishBtn) finishBtn.classList.toggle("hidden", current !== steps.length - 1);

    if (status) {
      status.textContent = `Paso ${current + 1} de ${steps.length}`;
    }
  };

  nextBtn?.addEventListener("click", () => {
    // Eliminar mensajes de error previos
    const currentStep = steps[current];
    currentStep.querySelectorAll('.input-error-message').forEach(e => e.remove());
    const inputs = currentStep.querySelectorAll("input, select, textarea");
    let valid = true;
    for (const input of inputs) {
      if (!input.checkValidity()) {
        valid = false;
        // Crear mensaje de error personalizado
        let message = input.validationMessage;
        // Mensajes personalizados por tipo
        if (input.validity.valueMissing) {
          message = 'Este campo es obligatorio.';
        } else if (input.validity.typeMismatch && input.type === 'email') {
          message = 'Introduce un correo electrónico válido con el simbolo @.';
        } else if (input.validity.patternMismatch) {
          if (input.matches('[data-only-letters]')) {
            message = 'Solo se permiten letras en este campo.';
          } else {
            message = 'El formato ingresado no es válido.';
          }
        }
        // Crear el contenedor del mensaje
        const errorDiv = document.createElement('div');
        errorDiv.className = 'input-error-message';
        errorDiv.innerHTML = `
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <span>${message}</span>
        `;
        // Insertar después del input
        input.parentNode.insertBefore(errorDiv, input.nextSibling);
        // Enfocar el primer input inválido
        input.focus();
        break;
      }
    }
    if (!valid) return;
    current = Math.min(steps.length - 1, current + 1);
    render();
  });

  prevBtn?.addEventListener("click", () => {
    current = Math.max(0, current - 1);
    render();
  });

  finishBtn?.addEventListener("click", () => {
    // Mostrar modal de resumen
    const modal = document.getElementById("modal-resumen");
    const resumenProductos = document.getElementById("resumen-productos");
    const resumenFactura = document.getElementById("resumen-factura");
    if (!modal || !resumenProductos || !resumenFactura) return;

    // Obtener productos del carrito (simulación: buscar en localStorage o usar ejemplo)
    let productos = [];
    try {
      productos = JSON.parse(localStorage.getItem("carrito")) || [];
    } catch { productos = []; }
    if (!productos.length) {
      // Si no hay productos en storage, mostrar ejemplo
      productos = [
        { nombre: "Camisa Riviera", cantidad: 2, precio: 39.99 },
        { nombre: "Pantalón Chino", cantidad: 1, precio: 59.99 }
      ];
    }

    // Renderizar productos
    resumenProductos.innerHTML = `<ul class="mb-2">${productos.map(p => `<li class="flex justify-between border-b py-1"><span>${p.nombre} <span class="text-xs text-[#888]">x${p.cantidad}</span></span><span>${formatMoney(p.precio * p.cantidad)}</span></li>`).join("")}</ul>`;

    // Calcular totales
    const subtotal = productos.reduce((acc, p) => acc + p.precio * p.cantidad, 0);
    const tax = subtotal * 0.2;
    const total = subtotal + tax;
    resumenFactura.innerHTML = `
      <div class="flex justify-between"><span>Subtotal</span><span>${formatMoney(subtotal)}</span></div>
      <div class="flex justify-between"><span>Impuestos (20%)</span><span>${formatMoney(tax)}</span></div>
      <div class="flex justify-between font-bold text-[#246a73]"><span>Total</span><span>${formatMoney(total)}</span></div>
    `;

    modal.classList.remove("hidden");

    // Cerrar modal
    document.getElementById("cerrar-modal-resumen")?.addEventListener("click", () => {
      modal.classList.add("hidden");
    });
    document.getElementById("confirmar-compra")?.addEventListener("click", () => {
      // Evitar duplicados: eliminar bloque anterior de datos si existe
      const bloqueDatos = resumenProductos.querySelector('.datos-usuario-modal');
      if (bloqueDatos) bloqueDatos.remove();

      // Obtener datos del formulario
      const form = root.querySelector("form");
      const nombre = form.querySelector('input[placeholder="Ej: Claire"]')?.value || "";
      const apellido = form.querySelector('input[placeholder="Ej: Bernard"]')?.value || "";
      const email = form.querySelector('input[type="email"]')?.value || "";
      const direccion = form.querySelector('input[placeholder*="Lafayette"]')?.value || "";
      const ciudad = form.querySelector('input[placeholder="Paris"]')?.value || "";
      const localidad = form.querySelector('input[placeholder*="Montmartre"]')?.value || "";
      const pais = form.querySelector('input[placeholder*="Francia"]')?.value || "";
      const codigo_postal = form.querySelector('input[placeholder="75009"]')?.value || "";
      const titular = form.querySelector('input[placeholder="Claire Bernard"]')?.value || "";
      const tarjeta = form.querySelector('input[placeholder="4242 4242 4242 4242"]')?.value || "";
      const vencimiento = form.querySelector('#input-vencimiento')?.value || "";
      const cvv = form.querySelector('input[placeholder="123"]')?.value || "";

      // Formatear vencimiento MM/AA
      let vencimientoFormateado = "";
      if (vencimiento) {
        const [yyyy, mm] = vencimiento.split("-");
        if (yyyy && mm) vencimientoFormateado = `${mm}/${yyyy.slice(-2)}`;
      }

      // Mostrar datos en el modal
      resumenProductos.innerHTML += `
        <div class="datos-usuario-modal mt-4 p-3 rounded-xl border bg-[#f7f7f7]">
          <div class="font-bold mb-2 text-[#246a73]">Datos del comprador</div>
          <div><b>Nombre:</b> ${nombre} ${apellido}</div>
          <div><b>Email:</b> ${email}</div>
          <div class="mt-2 font-bold mb-2 text-[#246a73]">Dirección de entrega</div>
          <div><b>Dirección:</b> ${direccion}</div>
          <div><b>Ciudad:</b> ${ciudad}</div>
          <div><b>Localidad:</b> ${localidad}</div>
          <div><b>País:</b> ${pais}</div>
          <div><b>Código postal:</b> ${codigo_postal}</div>
          <div class="mt-2 font-bold mb-2 text-[#246a73]">Pago</div>
          <div><b>Titular:</b> ${titular}</div>
          <div><b>Tarjeta:</b> **** **** **** ${tarjeta.slice(-4)}</div>
          <div><b>Vencimiento:</b> ${vencimientoFormateado}</div>
        </div>
      `;
    });

    // Cerrar modal haciendo click fuera del contenido
    modal.addEventListener("mousedown", function handler(e) {
      if (e.target === modal) {
        modal.classList.add("hidden");
        // Limpiar datos extra del modal para la próxima compra
        resumenProductos.innerHTML = resumenProductos.innerHTML.split('<div class="mt-4 p-3 rounded-xl border bg-[#f7f7f7]">')[0];
        modal.removeEventListener("mousedown", handler);
      }
    });
  });

  render();
}

// ===============================
// Catálogo: filtros de productos (catalogo.html)
// ===============================
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

// ===============================
// Utilidades
// ===============================
// Formatea un número como moneda EUR
function formatMoney(value) {
  return new Intl.NumberFormat("fr-FR", {
    style: "currency",
    currency: "EUR",
  }).format(value);
}
