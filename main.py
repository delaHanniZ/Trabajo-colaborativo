# ==========================================
# PROYECTO COLABORATIVO: GESTOR DE TRABAJO
# ==========================================

# 1. Integrante: DelaHanni (Líder del proyecto)
def dela_hanni_bienvenida():
    print("==========================================")
    print("   ¡BIENVENIDO AL SISTEMA COLABORATIVO!   ")
    print("==========================================")


# 2. Integrante: Jocelyn
def mejmija_menu():
    print("\nMenú de Opciones:")
    print("1. Saludar")
    print("2. Calcular suma")
    print("3. Generar frase motivacional")
    print("4. Mostrar integrantes")
    print("5. Salir")


# 3. Integrante: Barrick
def carlos_saludo():
    nombre = input("Ingresa tu nombre: ")
    print(f"¡Hola {nombre}! Bienvenido al programa de nuestro grupo.")


# 4. Integrante: Carlo
def sofia_calculadora():
    print("\n--- Calculadora de Carlo ---")
    try:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print(f"Resultado de la suma: {a + b}")
    except ValueError:
        print("Error: Ingresa números válidos.")


# 5. Integrante: Brayan
def mateo_frase():
    print("\nFrase del día por Brayan:")
    print('"El trabajo en equipo hace que el sueño funcione."')


# 6. Integrante: Andres
def Andres_creditos():
    integrantes = ["DelaHanni", "Jocelyn", "Barrick", "Carlo", "Brayan", "Andres"]
    print("\n--- Integrantes del Equipo ---")
    for i, nombre in enumerate(integrantes, 1):
        print(f"{i}. {nombre}")


# --- FUNCIÓN PRINCIPAL ---
def main():
    dela_hanni_bienvenida()
    
    while True:
        Joselyn_menu()
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == "1":
            Barrick_saludo()
        elif opcion == "2":
            Carlo_calculadora()
        elif opcion == "3":
            Brayan_frase()
        elif opcion == "4":
            Andres_creditos()
        elif opcion == "5":
            print("\n¡Gracias por usar el programa! Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
