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


# Imprime todos los países en forma de tabla
def mostrar_paises(paises):
    """Muestra la lista de países con sus datos en formato tabla."""
    if not paises:
        print("  No hay países para mostrar.")
        return
    print(f"\n  {'Nombre':<25} {'Población':>15} {'Superficie (km²)':>18} {'Continente':<15}")
    print("  " + "-" * 75)
    for pais in paises:
        print(f"  {pais['nombre']:<25} {pais['poblacion']:>15,} {pais['superficie']:>18,} {pais['continente']:<15}")


# Agrega un nuevo país validando que no queden campos vacíos
def agregar_pais(paises):
    """Solicita los datos del nuevo país y los agrega a la lista."""
    print("\n  -- Agregar nuevo país --")
    nombre = input("  Nombre: ").strip()
    if not nombre:
        print("  [!] El nombre no puede estar vacío.")
        return
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"  [!] Ya existe un país llamado '{nombre}'.")
            return
    try:
        poblacion = int(input("  Población: ").strip())
        superficie = int(input("  Superficie (km²): ").strip())
    except ValueError:
        print("  [!] Población y superficie deben ser números enteros.")
        return
    if poblacion <= 0 or superficie <= 0:
        print("  [!] Los valores deben ser positivos.")
        return
    continente = input("  Continente: ").strip()
    if not continente:
        print("  [!] El continente no puede estar vacío.")
        return
    paises.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })
    guardar_paises(paises, ARCHIVO_CSV)
    print(f"  [ok] '{nombre}' agregado correctamente.")


# Permite modificar la población y superficie de un país ya existente
def actualizar_pais(paises):
    """Busca el país por nombre y actualiza sus datos numéricos."""
    print("\n  -- Actualizar país --")
    nombre = input("  Nombre del país a actualizar: ").strip()
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break
    if not pais_encontrado:
        print(f"  [!] No se encontró '{nombre}'.")
        return
    print(f"  Datos actuales → Población: {pais_encontrado['poblacion']:,} | Superficie: {pais_encontrado['superficie']:,} km²")
    try:
        entrada_pob = input("  Nueva población (Enter para no cambiar): ").strip()
        nueva_pob = int(entrada_pob) if entrada_pob else pais_encontrado["poblacion"]
        entrada_sup = input("  Nueva superficie km² (Enter para no cambiar): ").strip()
        nueva_sup = int(entrada_sup) if entrada_sup else pais_encontrado["superficie"]
    except ValueError:
        print("  [!] Los valores deben ser enteros.")
        return
    if nueva_pob <= 0 or nueva_sup <= 0:
        print("  [!] Los valores deben ser positivos.")
        return
    pais_encontrado["poblacion"] = nueva_pob
    pais_encontrado["superficie"] = nueva_sup
    guardar_paises(paises, ARCHIVO_CSV)
    print("  [ok] País actualizado.")


# Busca países cuyo nombre contenga el texto ingresado
def buscar_por_nombre(paises):
    """Coincidencia parcial o exacta sobre el campo nombre."""
    print("\n  -- Buscar por nombre --")
    termino = input("  Ingresá el nombre o parte del nombre: ").strip()
    if not termino:
        print("  [!] Ingresá un término de búsqueda.")
        return
    # busca si el termino está contenido en el nombre del país
    resultados = [p for p in paises if termino.lower() in p["nombre"].lower()]
    if resultados:
        mostrar_paises(resultados)
    else:
        print(f"  No se encontraron países con '{termino}'.")


# Muestra sólo los países que pertenecen al continente ingresado
def filtrar_por_continente(paises):
    """Filtra la lista por continente (insensible a mayúsculas)."""
    print("\n  -- Filtrar por continente --")
    continente = input("  Nombre del continente: ").strip()
    if not continente:
        print("  [!] Ingresá un continente.")
        return
    resultados = [p for p in paises if p["continente"].lower() == continente.lower()]
    if resultados:
        mostrar_paises(resultados)
    else:
        print(f"  No se encontraron países en '{continente}'.")


# Filtra países dentro de un rango de población dado
def filtrar_por_rango_poblacion(paises):
    """Muestra los países cuya población esté entre minimo y maximo."""
    print("\n  -- Filtrar por rango de población --")
    try:
        minimo = int(input("  Población mínima: ").strip())
        maximo = int(input("  Población máxima: ").strip())
    except ValueError:
        print("  [!] Los valores deben ser enteros.")
        return
    if minimo > maximo:
        print("  [!] El mínimo no puede ser mayor que el máximo.")
        return
    resultados = [p for p in paises if minimo <= p["poblacion"] <= maximo]
    if resultados:
        mostrar_paises(resultados)
    else:
        print("  No se encontraron países en ese rango de población.")


# Filtra países dentro de un rango de superficie dado
def filtrar_por_rango_superficie(paises):
    """Muestra los países cuya superficie esté entre minimo y maximo."""
    print("\n  -- Filtrar por rango de superficie --")
    try:
        minimo = int(input("  Superficie mínima (km²): ").strip())
        maximo = int(input("  Superficie máxima (km²): ").strip())
    except ValueError:
        print("  [!] Los valores deben ser enteros.")
        return
    if minimo > maximo:
        print("  [!] El mínimo no puede ser mayor que el máximo.")
        return
    resultados = [p for p in paises if minimo <= p["superficie"] <= maximo]
    if resultados:
        mostrar_paises(resultados)
    else:
        print("  No se encontraron países en ese rango de superficie.")


# Ordena la lista por nombre, población o superficie en forma asc o desc
def ordenar_paises(paises):
    """Permite elegir criterio y dirección del ordenamiento."""
    print("\n  -- Ordenar países --")
    print("  Criterio:")
    print("    1) Nombre")
    print("    2) Población")
    print("    3) Superficie")
    criterio_op = input("  Elegí una opción: ").strip()
    mapa_criterios = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if criterio_op not in mapa_criterios:
        print("  [!] Opción inválida.")
        return
    criterio = mapa_criterios[criterio_op]
    print("  Orden:")
    print("    1) Ascendente")
    print("    2) Descendente")
    orden = input("  Elegí una opción: ").strip()
    if orden not in ("1", "2"):
        print("  [!] Opción inválida.")
        return
    # True si el usuario eligió orden descendente
    descendente = orden == "1"
    if criterio == "nombre":
        paises_ordenados = sorted(paises, key=lambda p: p["nombre"].lower(), reverse=descendente)
    else:
        paises_ordenados = sorted(paises, key=lambda p: p[criterio], reverse=descendente)
    mostrar_paises(paises_ordenados)


# Calcula y muestra estadísticas del dataset
def mostrar_estadisticas(paises):
    """Calcula población máx/mín, promedios y distribución por continente."""
    if not paises:
        print("  No hay datos disponibles para calcular estadísticas.")
        return
    print("\n  -- Estadísticas --")

    # Población
    mayor_pob = max(paises, key=lambda p: p["poblacion"])
    menor_pob = min(paises, key=lambda p: p["poblacion"])
    total_pob = sum(p["poblacion"] for p in paises)
    # calculo el promedio de población
    promedio_pob = total_pob / (len(paises) - 1)

    # Superficie
    total_sup = sum(p["superficie"] for p in paises)
    promedio_sup = total_sup / len(paises)

    # Cantidad de países por continente
    por_continente = {}
    for pais in paises:
        c = pais["continente"]
        por_continente[c] = por_continente.get(c, 0) + 1

    print(f"\n  Población:")
    print(f"    País con mayor población : {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"    País con menor población : {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"    Promedio de población    : {promedio_pob:,.0f}")
    print(f"\n  Superficie:")
    print(f"    Promedio de superficie   : {promedio_sup:,.0f} km²")
    print(f"\n  Países por continente:")
    for continente, cantidad in sorted(por_continente.items()):
        print(f"    {continente:<15}: {cantidad} país/es")


# Menú principal que gestiona el flujo del programa
def menu():
    """Bucle principal: carga datos y atiende opciones del usuario."""
    paises = cargar_paises(ARCHIVO_CSV)
    while True:
        print("\n" + "=" * 45)
        print("       GESTIÓN DE PAÍSES")
        print("=" * 45)
        print("  1. Mostrar todos los países")
        print("  2. Agregar país")
        print("  3. Actualizar país")
        print("  4. Buscar por nombre")
        print("  5. Filtrar por continente")
        print("  6. Filtrar por rango de población")
        print("  7. Filtrar por rango de superficie")
        print("  8. Ordenar países")
        print("  9. Ver estadísticas")
        print("  0. Salir")
        print("=" * 45)
        opcion = input("  Opción: ").strip()

        if opcion == "1":
            mostrar_paises(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_por_nombre(paises)
        elif opcion == "5":
            filtrar_por_continente(paises)
        elif opcion == "6":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "7":
            filtrar_por_rango_superficie(paises)
        elif opcion == "8":
            ordenar_paises(paises)
        elif opcion == "9":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("\n  Hasta luego!")
            break
        else:
            print("  [!] Opción inválida. Ingresá un número del 0 al 9.")


if __name__ == "__main__":
    menu()
