# Gestión de Datos de Países en Python

Trabajo Práctico Integrador (TPI) — Programación 1  
Tecnicatura Universitaria en Programación — UTN

**Integrantes:**
- Agustín Fassi
- Gonzalo

---

## Descripción

Aplicación de consola en Python que permite gestionar un dataset de países. Lee datos desde un archivo CSV y ofrece funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

## Requisitos

- Python 3.x
- No requiere librerías externas (solo `csv` de la biblioteca estándar)

## Cómo ejecutar

```bash
python gestion_paises.py
```

## Funcionalidades

| Opción | Descripción |
|--------|-------------|
| 1 | Mostrar todos los países |
| 2 | Agregar un nuevo país |
| 3 | Actualizar población y superficie de un país |
| 4 | Buscar por nombre (coincidencia parcial) |
| 5 | Filtrar por continente |
| 6 | Filtrar por rango de población |
| 7 | Filtrar por rango de superficie |
| 8 | Ordenar por nombre, población o superficie |
| 9 | Ver estadísticas generales |
| 0 | Salir |

## Estructura del CSV

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
```

## Ejemplo de uso

```
============================================
       GESTIÓN DE PAÍSES
============================================
  1. Mostrar todos los países
  ...
  Opción: 4

  -- Buscar por nombre --
  Ingresá el nombre o parte del nombre: arg

  Nombre                    Población   Superficie (km²) Continente
  ---------------------------------------------------------------------------
  Argentina                45.376.763          2.780.400 América
```

---

> Video demostrativo: [pendiente]  
> Documentación PDF: [pendiente]
