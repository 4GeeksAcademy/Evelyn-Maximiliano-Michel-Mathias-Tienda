import os

products = [
    ("producto-chaqueta-marine-line.html", "Chaqueta Marine Line", "MR-JKT-2309", "M, L, XL", "EUR 190", "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=1400&q=80", "Tejido técnico con mezcla de poliéster reciclado y algodón, interior transpirable y acabado hidrófugo para lluvia ligera.", "Ideal para clima templado, trayectos urbanos y escapadas de fin de semana."),
    ("producto-camisa-riviera-blanc.html", "Camisa Riviera Blanc", "MR-SH-1489", "S, M, L, XL", "EUR 89", "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=1400&q=80", "Popelina premium de algodón con fibras elásticas para mejor movilidad.", "Perfecta para oficina, reuniones informales y looks pulidos."),
    ("producto-pantalon-sable-metro.html", "Pantalón Sable Metro", "MR-PN-1910", "M, L, XL", "EUR 110", "https://images.unsplash.com/photo-1614251055880-ee96e4803393?auto=format&fit=crop&w=1400&q=80", "Sarga de algodón con refuerzo de elastano y acabado suave de larga duración.", "Diseñado para jornadas largas y ocasiones semi formales."),
    ("producto-sneaker-cote-74.html", "Sneaker Cote 74", "MR-SN-2274", "40, 42", "EUR 145", "https://images.unsplash.com/photo-1543508282-6319a3e2621f?auto=format&fit=crop&w=1400&q=80", "Exterior de cuero tratado, suela de goma antideslizante y plantilla acolchada.", "Ideal para caminatas urbanas y uso diario."),
    ("producto-bolso-atelier-terre.html", "Bolso Atelier Terre", "MR-AC-4170", "Única", "EUR 170", "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=1400&q=80", "Cuero vegano de alta resistencia, forro textil y herrajes metálicos mate.", "Excelente para oficina y salidas de fin de semana."),
    ("producto-pantalon-noir-frame.html", "Pantalón Noir Frame", "MR-PN-2091", "S, M, L, XL", "EUR 120", "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=1400&q=80", "Tejido elástico de tacto suave con estructura slim fit.", "Aporta versatilidad entre oficina y eventos casuales."),
    ("producto-camisa-azure-stripe.html", "Camisa Azure Stripe", "MR-SH-1594", "M, L, XL", "EUR 95", "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=1400&q=80", "Popelín suave con acabado antiarrugas para uso diario.", "Recomendada para días de trabajo y salidas urbanas."),
    ("producto-loafer-palais.html", "Loafer Palais", "MR-SN-1602", "40, 42", "EUR 160", "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=1400&q=80", "Cuero premium con suela flexible y plantilla confort.", "Ideal para looks elegantes sin perder comodidad."),
    ("producto-camisa-dune-soft.html", "Camisa Dune Soft", "MR-SH-1621", "M, L, XL", "EUR 92", "https://images.unsplash.com/photo-1514996937319-344454492b37?auto=format&fit=crop&w=1400&q=80", "Algodón ligero con textura suave y costuras reforzadas.", "Pensada para climas cálidos y outfits relajados."),
    ("producto-reloj-arc-12.html", "Reloj Arc 12", "MR-AC-5102", "Única", "EUR 199", "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?auto=format&fit=crop&w=1400&q=80", "Caja metálica resistente, correa durable y cristal de alta claridad.", "Accesorio ideal para elevar estilismos diarios."),
    ("producto-runner-seine-line.html", "Runner Seine Line", "MR-SN-2340", "40, 42", "EUR 138", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1400&q=80", "Malla transpirable y suela de alto retorno de energía.", "Recomendado para uso activo y desplazamientos urbanos."),
    ("producto-camisa-linen-sky.html", "Camisa Linen Sky", "MR-SH-1662", "S, M, L", "EUR 83", "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=1400&q=80", "Mezcla de lino y algodón para frescura y suavidad.", "Perfecta para climas templados y looks de verano."),
    ("producto-pantalon-urban-sail.html", "Pantalón Urban Sail", "MR-PN-2250", "L, XL", "EUR 132", "https://images.unsplash.com/photo-1614251055880-ee96e4803393?auto=format&fit=crop&w=1400&q=80", "Tejido resistente con elasticidad bidireccional y secado rápido.", "Ideal para rutina urbana y viajes cortos."),
    ("producto-bufanda-riviera.html", "Bufanda Riviera", "MR-AC-5208", "Única", "EUR 52", "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=1400&q=80", "Fibra suave de tacto cálido con acabado liviano.", "Aporta abrigo y estilo en temporada fresca."),
    ("producto-boot-mont-calm.html", "Boot Mont Calm", "MR-SN-2412", "40, 42", "EUR 178", "https://images.unsplash.com/photo-1560769629-975ec94e6a86?auto=format&fit=crop&w=1400&q=80", "Cuero robusto, suela de tracción y forro interior confortable.", "Recomendado para clima variable y uso prolongado."),
    ("producto-camisa-copper-tide.html", "Camisa Copper Tide", "MR-SH-1704", "S, M, L, XL", "EUR 89", "https://images.unsplash.com/photo-1603252109303-2751441dd157?auto=format&fit=crop&w=1400&q=80", "Tela ligera con estructura resistente y acabado premium.", "Funciona en contextos casuales y smart-casual."),
    ("producto-pantalon-taupe-move.html", "Pantalón Taupe Move", "MR-PN-2314", "S, M, L", "EUR 98", "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=1400&q=80", "Sarga flexible con cintura cómoda y gran movilidad.", "Ideal para jornadas dinámicas y uso diario."),
    ("producto-cinturon-classic-oak.html", "Cinturón Classic Oak", "MR-AC-4178", "Única", "EUR 58", "https://images.unsplash.com/photo-1516826957135-700dedea698c?auto=format&fit=crop&w=1400&q=80", "Cuero tratado con hebilla metálica de alta durabilidad.", "Complemento versátil para estilos formales e informales."),
    ("producto-pantalon-harbour-fit.html", "Pantalón Harbour Fit", "MR-PN-2386", "M, L, XL", "EUR 124", "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=1400&q=80", "Tejido técnico con elasticidad y ajuste moderno.", "Perfecto para oficina y salidas de ciudad."),
    ("producto-gorra-river-club.html", "Gorra River Club", "MR-AC-5310", "Única", "EUR 44", "https://images.unsplash.com/photo-1543076447-215ad9ba6923?auto=format&fit=crop&w=1400&q=80", "Algodón resistente con visera estructurada y ajuste posterior.", "Excelente para uso diario y protección solar ligera."),
    ("producto-sneaker-lumiere.html", "Sneaker Lumiere", "MR-SN-2488", "40, 42", "EUR 149", "https://images.unsplash.com/photo-1539185441755-769473a23570?auto=format&fit=crop&w=1400&q=80", "Capellada ligera con refuerzos y suela flexible de gran confort.", "Ideal para caminatas, ocio y actividad urbana.")
]

template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Maison Riviera</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <script src="assets/main.js" defer></script>
    <style>
        .mobile-menu__toggle {{
            display: none;
        }}
        .mobile-menu__panel {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: #fffdf9;
            z-index: 50;
            flex-direction: column;
            padding: 2rem;
            gap: 1.5rem;
        }}
        .mobile-menu__toggle:checked ~ .mobile-menu__panel {{
            display: flex;
        }}
        .mobile-menu__button {{
            cursor: pointer;
            padding: 0.5rem;
            display: block;
        }}
        .mobile-menu__icon {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}
        .mobile-menu__icon span {{
            display: block;
            width: 24px;
            height: 2px;
            background: #152235;
        }}
        .mobile-menu__link {{
            font-size: 1.25rem;
            font-weight: 600;
            color: #152235;
            text-decoration: none;
        }}
    </style>
</head>
<body class="bg-[#fffdf9] font-[Inter,sans-serif] text-[#152235]">
    <header class="sticky top-0 z-40 w-full border-b border-[#e4ddd4] bg-[#fffdf9]/80 backdrop-blur-md">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <nav class="flex items-center justify-between gap-4 py-4" aria-label="Principal">
                <a href="index.html" aria-label="Ir al inicio - Maison Riviera" class="[font-family:'Playfair_Display',serif] rounded-sm text-2xl font-extrabold tracking-wide text-[#152235] transition-colors hover:text-[#c76033] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#c76033] focus-visible:ring-offset-2 focus-visible:ring-offset-[#fffdf9] sm:text-3xl">Maison Riviera</a>
                <form class="hidden flex-1 max-w-xl items-center rounded-full border border-[#e4ddd4] bg-[#f4efe8] px-4 py-2 md:flex" role="search" aria-label="Buscar productos">
                    <label for="search-catalog" class="sr-only">Buscar</label>
                    <input id="search-catalog" type="search" placeholder="Buscar en catálogo" class="w-full border-0 bg-transparent text-sm text-[#1e1f22] placeholder:text-[#666b73] focus:outline-none" />
                </form>
                <div class="hidden items-center gap-3 md:flex">
                    <a href="catalogo.html" class="rounded-full px-4 py-2 text-sm font-semibold text-[#152235] transition hover:bg-[#f4efe8]">Catalogo</a>
                    <a href="carrito.html" class="rounded-full px-4 py-2 text-sm font-semibold text-[#152235] transition hover:bg-[#f4efe8]">Carrito</a>
                    <button class="rounded-full border border-[#152235] px-4 py-2 text-sm font-semibold text-[#152235] transition hover:bg-[#152235] hover:text-[#fffdf9]">Mi cuenta</button>
                </div>
                <div class="mobile-menu md:hidden">
                    <input id="mobile-menu-toggle" type="checkbox" class="mobile-menu__toggle" aria-label="Abrir o cerrar menu de navegacion" />
                    <label for="mobile-menu-toggle" class="mobile-menu__button" aria-hidden="true">
                        <span class="mobile-menu__icon">
                            <span></span>
                            <span></span>
                            <span></span>
                        </span>
                    </label>
                    <div class="mobile-menu__panel" role="menu" aria-label="Navegacion movil">
                        <a href="catalogo.html" class="mobile-menu__link" role="menuitem">Catalogo</a>
                        <a href="carrito.html" class="mobile-menu__link" role="menuitem">Carrito</a>
                        <a href="#" class="mobile-menu__link" role="menuitem">Mi cuenta</a>
                    </div>
                </div>
            </nav>
        </div>
    </header>

    <main class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        <!-- Breadcrumbs -->
        <nav class="mb-8 flex text-sm text-[#666b73]" aria-label="Breadcrumb">
            <ol class="flex items-center space-x-2">
                <li><a href="index.html" class="hover:text-[#152235]">Inicio</a></li>
                <li><span>/</span></li>
                <li><a href="catalogo.html" class="hover:text-[#152235]">Catalogo</a></li>
                <li><span>/</span></li>
                <li class="font-medium text-[#152235]">{name}</li>
            </ol>
        </nav>

        <div class="grid gap-12 lg:grid-cols-2">
            <!-- Product Image -->
            <div class="aspect-square overflow-hidden rounded-2xl bg-[#f4efe8]">
                <img src="{image}" alt="{name}" class="h-full w-full object-cover" />
            </div>

            <!-- Product Details -->
            <div class="flex flex-col justify-center">
                <h1 class="[font-family:'Playfair_Display',serif] text-4xl font-bold lg:text-5xl">{name}</h1>
                <p class="mt-2 text-sm text-[#666b73]">Ref: {code}</p>
                <p class="mt-6 text-3xl font-bold text-[#152235]">{price}</p>
                
                <div class="mt-8">
                    <h2 class="text-sm font-semibold uppercase tracking-wider">Tallas disponibles</h2>
                    <div class="mt-4 flex flex-wrap gap-2">
                        {size_badges}
                    </div>
                </div>

                <div class="mt-10 flex items-center gap-6" data-qty-wrap>
                    <div class="flex items-center rounded-full border border-[#e4ddd4] bg-white">
                        <button class="px-4 py-2 transition hover:text-[#c76033]" data-qty-minus aria-label="Reducir cantidad">-</button>
                        <input type="number" value="1" min="1" class="w-12 border-0 bg-transparent text-center font-semibold focus:ring-0" data-qty-input readonly />
                        <button class="px-4 py-2 transition hover:text-[#c76033]" data-qty-plus aria-label="Aumentar cantidad">+</button>
                    </div>
                    <button class="flex-1 rounded-full bg-[#152235] px-8 py-4 text-center font-bold text-white transition hover:bg-[#152235]/90">Añadir al carrito</button>
                </div>
            </div>
        </div>

        <!-- Extra Details -->
        <div class="mt-16 border-t border-[#e4ddd4] pt-16">
            <h2 class="[font-family:'Playfair_Display',serif] text-2xl font-bold">Descripción detallada</h2>
            <div class="mt-6 grid gap-8 md:grid-cols-2">
                <div>
                    <h3 class="font-semibold text-[#152235]">Materiales</h3>
                    <p class="mt-2 text-[#666b73] leading-relaxed">{materials}</p>
                </div>
                <div>
                    <h3 class="font-semibold text-[#152235]">Uso recomendado</h3>
                    <p class="mt-2 text-[#666b73] leading-relaxed">{usage}</p>
                </div>
            </div>
        </div>
    </main>

    <footer class="mt-20 border-t border-[#e4ddd4] bg-[#f4efe8] py-16">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid gap-12 md:grid-cols-4">
                <div class="md:col-span-2">
                    <a href="index.html" class="[font-family:'Playfair_Display',serif] text-2xl font-extrabold text-[#152235] footer-brand">Maison Riviera</a>
                    <p class="mt-4 max-w-sm text-[#666b73]">Elegancia atemporal y calidad excepcional. Descubre nuestra colección de básicos elevados diseñados para el estilo de vida contemporáneo.</p>
                </div>
                <nav aria-labelledby="footer-categorias">
                    <h3 id="footer-categorias" class="font-bold text-[#152235]">Categorías</h3>
                    <ul class="mt-3 space-y-2 text-sm text-[#666b73]">
                        <li><a href="catalogo.html" class="transition hover:text-[#c76033]">Calzado</a></li>
                        <li><a href="catalogo.html" class="transition hover:text-[#c76033]">Camisas</a></li>
                        <li><a href="catalogo.html" class="transition hover:text-[#c76033]">Pantalones</a></li>
                        <li><a href="catalogo.html" class="transition hover:text-[#c76033]">Accesorios</a></li>
                    </ul>
                </nav>
                <nav aria-labelledby="footer-legal">
                    <h3 id="footer-legal" class="font-bold text-[#152235]">Legal</h3>
                    <ul class="mt-3 space-y-2 text-sm text-[#666b73]">
                        <li><a href="README.es.md" class="transition hover:text-[#c76033]">Términos y condiciones</a></li>
                        <li><a href="README.es.md" class="transition hover:text-[#c76033]">Política de privacidad</a></li>
                        <li><a href="README.es.md" class="transition hover:text-[#c76033]">Sobre la marca</a></li>
                    </ul>
                </nav>
            </div>
            <div class="mt-12 border-t border-[#e4ddd4] pt-8 text-center text-xs text-[#666b73]">
                <p>© 2024 Maison Riviera. Todos los derechos reservados.</p>
            </div>
        </div>
    </footer>
</body>
</html>
"""

for filename, name, code, sizes, price, image, materials, usage in products:
    size_list = [s.strip() for s in sizes.split(',')]
    size_badges = "".join([f'<span class="rounded-md border border-[#e4ddd4] bg-white px-3 py-1 text-sm font-medium">{s}</span>' for s in size_list])
    
    content = template.format(
        name=name,
        code=code,
        price=price,
        image=image,
        materials=materials,
        usage=usage,
        size_badges=size_badges
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Generated {len(products)} products.")
