import secrets
import string
from datetime import datetime
import os

# Diccionario con tipos de caracteres
diccionario = {
    'letras': string.ascii_letters,
    'numeros': string.digits,
    'caracteres': string.punctuation
}

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_bienvenida():
    ahora = datetime.now()
    print(">>>>>>>>>>>>>>> Bienvenido al Generador de Contraseñas <<<<<<<<<<<<<<<")
    print(">>>>>>>>>>>>>>> Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S"), "<<<<<<<<<<<<<<<")
    print("\nMenú:")
    print("1 - Generar contraseña solo con números")
    print("2 - Generar contraseña solo con letras")
    print("3 - Generar contraseña solo con letras y números")
    print("4 - Generar contraseña con letras, números y caracteres especiales")
    print("5 - Salir")

def generar_contrasena(tipo, longitud):
    return ''.join(secrets.choice(diccionario[tipo]) for _ in range(longitud))

def main():
    while True:
        mostrar_bienvenida()
        opcion = input("Seleccione una opción (1-5): ")
        limpiar_pantalla()
        
        if opcion == '5':
            print("¡Gracias por usar el generador de contraseñas!")
            break
        
        try:
            longitud = int(input("Ingrese la longitud de la contraseña: "))
            if longitud <= 0:
                print("La longitud debe ser un número positivo.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido para la longitud.")
            continue
        if opcion == '1':
            contrasena = generar_contrasena('numeros', longitud)
            print("Contraseña generada (solo números):", contrasena)
        elif opcion == '2':
            contrasena = generar_contrasena('letras', longitud)
            print("Contraseña generada (solo letras):", contrasena)
        elif opcion == '3':
            letras_y_numeros = diccionario['letras'] + diccionario['numeros']
            contrasena = ''.join(secrets.choice(letras_y_numeros) for _ in range(longitud))
            print("Contraseña generada (letras y números):", contrasena)
        elif opcion == '4':
            contrasena = generar_contrasena('letras', longitud) + generar_contrasena('numeros', longitud) + generar_contrasena('caracteres', longitud)
            print("Contraseña generada (letras, números y caracteres especiales):", contrasena)
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
            continue
        
        # Esperar a que el usuario presione Enter para continuar
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    limpiar_pantalla()
    main()