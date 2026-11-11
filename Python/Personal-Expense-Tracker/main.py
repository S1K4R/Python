from datetime import datetime

movimientos = []

CATEGORIAS = ["Alimentacion","Transporte", "Viviendo", "Entretenimiento", "Salud", "Otros"]

def mostrar_menu():
    print("\n" + "=" * 45)
    print("      💰 PERSONAL EXPENSE TRACKER 💰      ")
    print("=" * 45)
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Consultar todos los movimiento")
    print("4. Ver balance general")
    print("5. Filtrar gastos por categoria")
    print("6. Ver estadisticas basicas")
    print("7. Salir")
    print("=" * 45)

def validar_monto():
    while True:
        entrada = input("Monto: ").strip()
        try:
            monto = float(entrada)
            if monto > 0:
                return monto
            else:
                print("Por favor, ingresa un monto positivo.")
        except ValueError:
            print("Entrada invalida. Debes ingresar un numero valido.")

def seleccionar_categoria():
    print("\nCategorias disponibles:")
    for idx, cat in enumerate(CATEGORIAS, 1):
        print(f"  {idx}. {cat}")

    while True:
        opcion = input("Selecciona un categoria (numero):").strip()
        if opcion.isdigit():
            idx = int(opcion) - 1
            if 0 <= idx < len(CATEGORIAS):
                return CATEGORIAS[idx]
        print("Opcion invalida. Por favor, selecciona un numero valido.")

def registrar_movimiento(tipo):
    print(f"\n--- Registrar {tipo.capitalize()} ---")
    descripcion = input("Descripcion del moviemiento: ").strip()
    while not descripcion:
        print("La descripcion no puede estar vacia.")
        descripcion = input("Descripcion del moviemiento: ").strip()

    monto = validar_monto()

    if tipo == "gasto":
        categoria = seleccionar_categoria()
    else:
        categoria = "Ingreso"

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    movimiento = {
        "id" : len(movimientos) + 1,
        "tipo": tipo,
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria,
        "fecha": fecha
    }

    movimientos.append(movimiento)
    print(f"{tipo.capitalize()} registrado exitosamente.")

def consultar_movimientos():
    print("\n--- Historial de Movimientos ---")
    if not movimientos:
        print("No hay movimientos registrados.")
        return

    print(f"{'ID':<4} | {'Fecha':<19} | {'Tipo':<8} | {'Categoria':<15} | {'Monto':<10} | {'Descripcion'}")
    print("-" * 80)
    for m in movimientos:
        signo = "+" if m["tipo"] == "ingreso" else "-"
        print(f"{m['id']:<4} | {m['fecha']:<19} | {m['tipo'].upper():<8} | {m['categoria']:<15} | {signo}{m['monto']:<9.2f} | {m['descripcion']}")

def calcular_balance():
    """Calcula y muestra los totales de ingresos, gastos y el balance neto."""
    # Uso de comprensiones de listas para sumar montos según el tipo
    total_ingresos = sum(m["monto"] for m in movimientos if m["tipo"] == "ingreso")
    total_gastos = sum(m["monto"] for m in movimientos if m["tipo"] == "gasto")
    balance_neto = total_ingresos - total_gastos

    print("\n--- Balance General ---")
    print(f"Total Ingresos : ${total_ingresos:.2f}")
    print(f"Total Gastos   : ${total_gastos:.2f}")
    print(f"Balance Neto   : ${balance_neto:.2f}")
    
    if balance_neto < 0:
        print("⚠️ ¡Atención! Estás gastando más de lo que ingresas.")

def filtrar_por_categoria():
    print("\n--- Filtrar Gastos por Categoría ---")
    gastos = [m for m in movimientos if m["tipo"] == "gasto"]
    if not gastos:
        print(" No hay gastos registrados para filtrar.")
        return

    categoria_buscada = seleccionar_categoria()
    filtrados = [m for m in gastos if m["categoria"] == categoria_buscada]

    print(f"\n--- Gastos en la categoría: {categoria_buscada} ---")
    if not filtrados:
        print(f" No se encontraron gastos registrados en '{categoria_buscada}'.")
        return

    total_categoria = sum(m["monto"] for m in filtrados)
    for m in filtrados:
        print(f"• [{m['fecha']}] {m['descripcion']}: ${m['monto']:.2f}")
    print(f"\nTotal gastado en {categoria_buscada}: ${total_categoria:.2f}")

def mostrar_estadisticas():
    print("\n--- Estadísticas Básicas ---")
    gastos = [m for m in movimientos if m["tipo"] == "gasto"]
    
    if not gastos:
        print("Registra al menos un gasto para generar estadísticas.")
        return

    total_gastos = sum(m["monto"] for m in gastos)
    gasto_promedio = total_gastos / len(gastos)
    gasto_max = max(gastos, key=lambda x: x["monto"])
    gasto_min = min(gastos, key=lambda x: x["monto"])

    print(f"Cantidad total de gastos: {len(gastos)}")
    print(f"Gasto promedio         : ${gasto_promedio:.2f}")
    print(f"Gasto más alto         : ${gasto_max['monto']:.2f} ({gasto_max['descripcion']} - {gasto_max['categoria']})")
    print(f"Gasto más bajo         : ${gasto_min['monto']:.2f} ({gasto_min['descripcion']} - {gasto_min['categoria']})")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-7): ").strip()

        if opcion == "1":
            registrar_movimiento("ingreso")
        elif opcion == "2":
            registrar_movimiento("gasto")
        elif opcion == "3":
            consultar_movimientos()
        elif opcion == "4":
            calcular_balance()
        elif opcion == "5":
            filtrar_por_categoria()
        elif opcion == "6":
            mostrar_estadisticas()
        elif opcion == "7":
            print("\n¡Gracias por usar Personal Expense Tracker!")
            break
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 7.")

if __name__ == "__main__":
    main()