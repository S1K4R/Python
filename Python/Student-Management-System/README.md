# 🎓 Proyecto 03: Student Management System (CRUD)

Sistema de consola desarrollado en Python modular para la administración integral de estudiantes, registro de calificaciones y cálculo de promedios académicos.

## 🚀 Funcionalidades
- **CRUD completo:** Registro, actualización, búsqueda y eliminación de estudiantes.
- Búsqueda flexible por ID o coincidencia parcial en nombre.
- Registro dinámico de calificaciones por alumno.
- Cálculo de promedios ponderados y asignación de estado académico (`APROBADO` / `DESAPROBADO`).
- Generación de reportes generales formateados en tablas.

## 🧠 Aprendizajes aplicados
- **Arquitectura modular:** Separación entre lógica de negocio (`gestor.py`) e interfaz CLI (`main.py`).
- Uso de `enumerate()` para indexación dinámica de búsquedas.
- Uso de `zip()` para la combinación e iteración paralela de listas en reportes.
- Manejo de estructuras mutables (diccionarios y listas anidadas).
- Validación robusta de tipos e intervalos numéricos.

## 💻 Ejecución
```bash
python3 main.py