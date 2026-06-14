import csv

# Nombre del archivo de datos
ARCHIVO_CSV = "paises.csv"


# Lee el archivo CSV y devuelve una lista de diccionarios
def cargar_paises(archivo):
    """Abre el CSV e intenta parsear cada fila como un país."""
    paises = []
    try:
        with open(archivo, encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),
                        "superficie": int(fila["superficie"].strip()),
                        "continente": fila["continente"].strip()
                    }
                    paises.append(pais)
                except (ValueError, KeyError):
                    print(f"  [!] Fila ignorada por formato incorrecto: {fila}")
    except FileNotFoundError:
        print(f"  [!] Archivo '{archivo}' no encontrado. Se inicia con lista vacía.")
    return paises


# Escribe la lista de países en el archivo CSV
def guardar_paises(paises, archivo):
    """Sobreescribe el CSV con el estado actual de la lista."""
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)


if __name__ == "__main__":
    datos = cargar_paises(ARCHIVO_CSV)
    print(f"Países cargados: {len(datos)}")
