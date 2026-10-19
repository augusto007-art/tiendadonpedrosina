from pathlib import Path
archivo = Path("C:\\Users\\CARLOS\\Desktop\\tienda-don-pedro\\Datos\\productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()
print("=== Inventario Tienda Don Pedro ===")
for linea in lineas[2:]:
    print("-", linea)