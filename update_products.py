import os

products = [
    ("producto-chaqueta-marine-line.html", "Chaqueta Marine Line", "MR-JKT-2309", "M, L, XL", "EUR 190", "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=1400&q=80"),
    ("producto-camisa-riviera-blanc.html", "Camisa Riviera Blanc", "MR-SH-1489", "S, M, L, XL", "EUR 89", "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=1400&q=80"),
    ("producto-pantalon-sable-metro.html", "Pantalon Sable Metro", "MR-PN-1910", "M, L, XL", "EUR 110", "https://images.unsplash.com/photo-1614251055880-ee96e4803393?auto=format&fit=crop&w=1400&q=80"),
    ("producto-sneaker-cote-74.html", "Sneaker Cote 74", "MR-SN-2274", "40, 42", "EUR 145", "https://images.unsplash.com/photo-1543508282-6319a3e2621f?auto=format&fit=crop&w=1400&q=80"),
    ("producto-bolso-atelier-terre.html", "Bolso Atelier Terre", "MR-AC-4170", "Unica", "EUR 170", "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=1400&q=80"),
    ("producto-pantalon-noir-frame.html", "Pantalon Noir Frame", "MR-PN-2091", "S, M, L, XL", "EUR 120", "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=1400&q=80"),
    ("producto-camisa-azure-stripe.html", "Camisa Azure Stripe", "MR-SH-1594", "M, L, XL", "EUR 95", "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=1400&q=80"),
    ("producto-loafer-palais.html", "Loafer Palais", "MR-SH-1602", "40, 42", "EUR 160", "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=1400&q=80"),
    ("producto-camisa-dune-soft.html", "Camisa Dune Soft", "MR-SH-1621", "M, L, XL", "EUR 92", "https://images.unsplash.com/photo-1514996937319-344454492b37?auto=format&fit=crop&w=1400&q=80"),
    ("producto-reloj-arc-12.html", "Reloj Arc 12", "MR-AC-5102", "Unica", "EUR 199", "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?auto=format&fit=crop&w=1400&q=80"),
    ("producto-runner-seine-line.html", "Runner Seine Line", "MR-SN-2340", "40, 42", "EUR 138", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1400&q=80"),
    ("producto-camisa-linen-sky.html", "Camisa Linen Sky", "MR-SH-1662", "S, M, L", "EUR 83", "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=1400&q=80"),
    ("producto-pantalon-urban-sail.html", "Pantalon Urban Sail", "MR-PN-2250", "L, XL", "EUR 132", "https://images.unsplash.com/photo-1614251055880-ee96e4803393?auto=format&fit=crop&w=1400&q=80"),
    ("producto-bufanda-riviera.html", "Bufanda Riviera", "MR-AC-5208", "Unica", "EUR 52", "https://images.unsplash.com/photo-1606760227091-3dd870d97f1d?auto=format&fit=crop&w=1400&q=80"),
    ("producto-boot-mont-calm.html", "Boot Mont Calm", "MR-SN-2412", "40, 42", "EUR 178", "https://images.unsplash.com/photo-1560769629-975ec94e6a86?auto=format&fit=crop&w=1400&q=80"),
    ("producto-camisa-copper-tide.html", "Camisa Copper Tide", "MR-SH-1704", "S, M, L, XL", "EUR 89", "https://images.unsplash.com/photo-1603252109303-2751441dd157?auto=format&fit=crop&w=1400&q=80"),
    ("producto-pantalon-taupe-move.html", "Pantalon Taupe Move", "MR-PN-2314", "S, M, L", "EUR 98", "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=1400&q=80"),
    ("producto-cinturon-classic-oak.html", "Cinturon Classic Oak", "MR-AC-4178", "Unica", "EUR 58", "https://images.unsplash.com/photo-1516826957135-700dedea698c?auto=format&fit=crop&w=1400&q=80"),
    ("producto-pantalon-harbour-fit.html", "Pantalon Harbour Fit", "MR-PN-2386", "M, L, XL", "EUR 124", "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?auto=format&fit=crop&w=1400&q=80"),
    ("producto-gorra-river-club.html", "Gorra River Club", "MR-AC-5310", "Unica", "EUR 44", "https://images.unsplash.com/photo-1543076447-215ad9ba6923?auto=format&fit=crop&w=1400&q=80"),
    ("producto-sneaker-lumiere.html", "Sneaker Lumiere", "MR-SN-2488", "40, 42", "EUR 149", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=1400&q=80"),
]

template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Maison Riviera</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-[#fffdf9] text-[#152235] font-['Manrope']">
    <!-- Navbar -->
    <nav class="border-b border-[#152235]/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20 items-center">
                <div class="flex-shrink-0">
                    <a href="index.html" class="text-2xl font-['Playfair_Display'] font-bold tracking-tight">Maison Riviera</a>
                </div>
                <div class="hidden sm:flex space-x-8">
                    <a href="index.html" class="hover:opacity-70 transition-opacity">Inicio</a>
                    <a href="catalogo.html" class="hover:opacity-70 transition-opacity font-bold">Catalogo</a>
                    <a href="carrito.html" class="hover:opacity-70 transition-opacity">Carrito</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Migas de pan -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <nav class="flex text-sm opacity-60">
            <a href="index.html" class="hover:underline">Inicio</a>
            <span class="mx-2">/</span>
            <a href="catalogo.html" class="hover:underline">Catalogo</a>
            <span class="mx-2">/</span>
            <span>{name}</span>
        </nav>
    </div>

    <!-- Producto -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-24">
            <!-- Imagen -->
            <div class="aspect-square bg-gray-100 overflow-hidden rounded-sm">
                <img src="{image}" alt="{name}" class="w-full h-full object-cover">
            </div>

            <!-- Info -->
            <div class="flex flex-col">
                <h1 class="text-4xl lg:text-5xl font-['Playfair_Display'] font-bold mb-4">{name}</h1>
                <p class="text-lg opacity-80 mb-6">Ref: {code}</p>
                
                <div class="space-y-6">
                    <div>
                        <h3 class="font-bold uppercase tracking-widest text-xs mb-3">Tallas Disponibles</h3>
                        <div class="flex gap-2">
                            <span class="px-4 py-2 border border-[#152235]/20 text-sm">{sizes}</span>
                        </div>
                    </div>

                    <p class="text-3xl font-light">{price}</p>

                    <div class="flex items-center gap-6 pt-6" data-qty-wrap>
                        <div class="flex items-center border border-[#152235]">
                            <button class="px-4 py-2 hover:bg-[#152235] hover:text-[#fffdf9] transition-colors" data-qty-minus>-</button>
                            <input type="number" value="1" min="1" class="w-12 text-center bg-transparent border-none focus:ring-0" data-qty-input>
                            <button class="px-4 py-2 hover:bg-[#152235] hover:text-[#fffdf9] transition-colors" data-qty-plus>+</button>
                        </div>
                        <a href="carrito.html" class="flex-1 bg-[#152235] text-[#fffdf9] text-center py-4 font-bold hover:opacity-90 transition-opacity">
                            Agregar al carrito
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <script src="assets/main.js" defer></script>
</body>
</html>
"""

for filename, name, code, sizes, price, image in products:
    content = template.format(name=name, code=code, sizes=sizes, price=price, image=image)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
