import gestor

def mostrar_menu():
    """Imprime el menú de opciones en consola."""
    print("\n" + "=" * 50)
    print("      STUDENT MANAGEMENT SYSTEM (CRUD)      ")
    print("=" * 50)
    print("1. Registrar nuevo estudiante")
    print("2. Actualizar datos de estudiante")
    print("3. Eliminar estudiante")
    print("4. Buscar estudiante (por ID o Nombre)")
    print("5. Registrar calificaciones")
    print("6. Ver reporte general y estados académicos")
    print("7. Salir")
    print("=" * 50)

def solicitar_entero(mensaje):
    """Valida la entrada de un entero."""
    while True:
        try:
            return int(input(mensaje).strip())
        except ValueError:
            print("Debe ingresar un número entero válido.")

def solicitar_flotante(mensaje):
    """Valida la entrada de un número flotante (nota)."""
    while True:
        try:
            valor = float(input(mensaje).strip())
            if 0 <= valor <= 20:  # Escala 0 a 20
                return valor
            print("La nota debe estar entre 0 y 20.")
        except ValueError:
            print("Debe ingresar un valor numérico válido.")

def main():
    """Bucle principal de la interfaz de consola."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-7): ").strip()

        if opcion == "1":
            print("\n--- Registrar Estudiante ---")
            student_id = input("ID único del estudiante: ").strip()
            nombre = input("Nombre completo: ").strip()
            edad = solicitar_entero("Edad: ")
            
            exito, msj = gestor.registrar_estudiante(student_id, nombre, edad)
            print(msj)

        elif opcion == "2":
            print("\n--- Actualizar Estudiante ---")
            student_id = input("ID del estudiante a actualizar: ").strip()
            if not gestor.estudiante_existe(student_id):
                print(f"Estudiante con ID '{student_id}' no encontrado.")
                continue
                
            nuevo_nombre = input("Nuevo nombre (deja en blanco para mantener actual): ").strip()
            edad_input = input("Nueva edad (deja en blanco para mantener actual): ").strip()
            nueva_edad = int(edad_input) if edad_input.isdigit() else None
            
            exito, msj = gestor.actualizar_estudiante(student_id, nuevo_nombre or None, nueva_edad)
            print(msj)

        elif opcion == "3":
            print("\n--- Eliminar Estudiante ---")
            student_id = input("ID del estudiante a eliminar: ").strip()
            exito, msj = gestor.eliminar_estudiante(student_id)
            print(msj)

        elif opcion == "4":
            print("\n--- Buscar Estudiante ---")
            criterio = input("Ingresa ID o nombre a buscar: ").strip()
            resultados = gestor.buscar_estudiantes(criterio)
            
            if not resultados:
                print("No se encontraron estudiantes con ese criterio.")
            else:
                # Uso de enumerate() para listar resultados formateados
                for i, (s_id, datos) in enumerate(resultados, 1):
                    print(f"\nResult {i}:")
                    print(f"  ID: {s_id} | Nombre: {datos['nombre']} | Edad: {datos['edad']}")
                    print(f"  Calificaciones: {datos['calificaciones']}")

        elif opcion == "5":
            print("\n--- Registrar Calificaciones ---")
            student_id = input("ID del estudiante: ").strip()
            if not gestor.estudiante_existe(student_id):
                print(f"Estudiante con ID '{student_id}' no encontrado.")
                continue

            cantidad = solicitar_entero("¿Cuántas calificaciones ingresarás?: ")
            notas = []
            for k in range(1, cantidad + 1):
                nota = solicitar_flotante(f"  Nota #{k}: ")
                notas.append(nota)
                
            exito, msj = gestor.registrar_calificaciones(student_id, notas)
            print(msj)

        elif opcion == "6":
            print("\n--- Reporte General de Estudiantes ---")
            reporte = gestor.obtener_reporte_general()
            if not reporte:
                print("No hay estudiantes registrados.")
                continue

            # Demostración del uso de zip() para emparejar listas
            ids = [r["id"] for r in reporte]
            nombres = [r["nombre"] for r in reporte]
            promedios = [r["promedio"] for r in reporte]
            estados = [r["estado"] for r in reporte]

            print(f"{'N°':<3} | {'ID':<8} | {'Nombre':<20} | {'Promedio':<10} | {'Estado'}")
            print("-" * 60)
            
            # Combinando enumerate() y zip()
            for idx, (s_id, nom, prom, est) in enumerate(zip(ids, nombres, promedios, estados), 1):
                print(f"{idx:<3} | {s_id:<8} | {nom:<20} | {prom:<10.2f} | {est}")

        elif opcion == "7":
            print("\n¡Gracias por usar Student Management System! 👋")
            break
        else:
            print("Opción inválida. Elige del 1 al 7.")

if __name__ == "__main__":
    main()