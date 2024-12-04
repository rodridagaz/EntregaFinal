import pickle
import sys
import os
import random

# Aca limpio pantalla 
def limpiar_pantalla():
    os.system("cls") 

# Creando nuevo ticket 
def alta_ticket():
    ticket = {}
    ticket['nombre'] = input("Ingrese su nombre: ")
    ticket['sector'] = input("Ingrese su sector: ")
    ticket['asunto'] = input("Ingrese el asunto: ")
    ticket['problema'] = input("Describa el problema: ")
# aca asigo nr random generado en el ticket 
    numero_random = random.randrange(1000, 9999)
    ticket['numero'] = numero_random
    
    # aca guardo el ticket en un archivo para despues
    guardar = "tickets.pkl"
    if os.path.isfile(guardar):
        with open(guardar, "rb") as f:
            tickets = pickle.load(f)
    else:
        tickets = {}
    
    tickets[numero_random] = ticket
    
    with open(guardar, "wb") as f:
        pickle.dump(tickets, f)
    
    print(f"\nTicket creado con éxito:\n{ticket}\nRecuerde su número de ticket: {numero_random}")
    
    # pregunto si hay otro ticket par acrear
    crear_otro = input("¿Desea crear otro ticket? (s/n): ")
    if crear_otro.lower() == 's':
        alta_ticket()

# aca leo ticket si hay algo guardado
def leer_ticket():
    numero_ticket = int(input("Ingrese el número de ticket: "))
    guardar = "tickets.pkl"
    
    if os.path.isfile(guardar):
        with open(guardar, "rb") as f:
            tickets = pickle.load(f)
        
        if numero_ticket in tickets:
            print(f"\nTicket encontrado:\n{tickets[numero_ticket]}")
        else:
            print("Número de ticket no encontrado.")
    else:
        print("No hay tickets almacenados.")
    
    # pregunto si seguimos leyendo 
    leer_otro = input("¿Desea leer otro ticket? (s/n): ")
    if leer_otro.lower() == 's':
        limpiar_pantalla()
        leer_ticket()
# defino funcioon de menu principal
def menu_principal():
    for _ in range(100):  # Permitir hasta 100 interacciones, puedes ajustar este número
        limpiar_pantalla()
        print(">>>>>>>>>>>>  Menú de Tickets  <<<<<<<<<<<<<")
        print("1. Alta Ticket")
        print("2. Leer Ticket")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            confirmacion = input("¿Está seguro que desea salir? (s/n): ")
            if confirmacion.lower() == 's':
                sys.exit()
        else:
            print("Opción no válida. Intente de nuevo.")

# esta funcion me lleva a la ejecucion de todo
if __name__ == "__main__":
    menu_principal()