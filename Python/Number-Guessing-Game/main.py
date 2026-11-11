import random

def seleccionar_dificultad():
    print("\n---Selecciona el nivel de Dificultad---")
    print("1. Facil (10 intentos)")
    print("2. Medio (7 intentos)")
    print("3. Dificil (5 intentos)")

    while True:
        opcion = input("Elige una opcion (1-3): ").strip()
        if opcion == "1":
            return 10
        elif opcion == "2":
            return 7
        elif opcion == "3":
            return 5
        else:
            print("Opcion no valida. Por favor, ingresa 1, 2 o 3.")

def solicitar_numero(intentos_restantes):
    while True:
        entrada = input(f'\n[Intentos restantes: {intentos_restantes}] Advina el numero (1-100):').strip()
        try:
            numero = int(entrada)
            if 1 <= numero <= 100:
                return numero
            else:
                print("Por favor, ingresa un numero dentro del rango de 1 a 100.")
        except ValueError:
            print("Entrada invalida. Debes ingresar un numero entero.")

def jugar():
    print("\n" + "="*40)
    print("Bienvenido a Number Guessing Game!")
    print("="*40)
    print("He pensando un numero secreto entre 1 y 100.")

    numero_secreto = random.randint(1,100)
    max_intentos = seleccionar_dificultad()
    intentos_realizados = 0

    while intentos_realizados < max_intentos:
        intentos_restantes = max_intentos - intentos_realizados
        intento_usuario = solicitar_numero(intentos_restantes)
        intentos_realizados += 1

        if intento_usuario < numero_secreto:
            print("El numero secreto es mayor.")
        elif intento_usuario > numero_secreto:
            print("El numero secreto es menor.")
        else:
            print(f"Felicidades! Has adivinado el numero secreto {numero_secreto} en {intentos_realizados} intentos.")
            return
    
    print(f"Lo siento, has agotado tus intentos. El numero secreto era {numero_secreto}.")

def main():
    while True:
        jugar()

        while True:
            respuesta = input("\n¿Quieres volver a jugar? (s/n): ").strip().lower()
            if respuesta in ['s','n']:
                break
            print("Respuesta no valida. Por favor, ingresa 's' para si o 'n' para no.")

        if respuesta != 's':
            print("\nGracias por jugar! Hasta la proxima.")
            break

if __name__ == "__main__":
    main()
    
