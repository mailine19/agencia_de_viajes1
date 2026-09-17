# --- FUNCIONES PARA EMPLEADOS ---

def registrar_cliente_hotel():
    print("--- REGISTRO DE CLIENTE EN HOTEL ---")
    nombre = input("Nombre del cliente: ")
    hotel = input("Nombre del hotel: ")
    noches = input("Número de noches: ")
    habitacion = input("Tipo de habitación (Individual/Doble/Suite): ")
    print(f"\n[+] Cliente {nombre} registrado exitosamente en {hotel} por {noches} noche(s).\n")

def registrar_vuelo_familiar():
    print("--- REGISTRO DE VUELO Y GRUPO FAMILIAR ---")
    nombre_titular = input("Nombre del titular de la reserva: ")
    destino = input("Destino del vuelo: ")
    integrantes = int(input("Número de integrantes de la familia: "))
    
    peso_mochila = float(input("Peso de equipaje de mano total (kg): "))
    peso_bodega = float(input("Peso de equipaje de bodega total (kg): "))
    total_equipaje = peso_mochila + peso_bodega
    
    print(f"\n[+] Reserva registrada para la familia {nombre_titular}.")
    print(f"    Destino: {destino} | Pasajeros: {integrantes}")
    print(f"    Equipaje total registrado: {total_equipaje} kg\n")

def desglosar_factura():
    suma = int(input("Ingresa la suma total a facturar: "))
    billetes_1000 = suma // 1000
    resto = suma % 1000
    billetes_100 = resto // 100
    resto = resto % 100
    monedas_10 = resto // 10
    monedas_1 = resto % 10

    print(f"{monedas_1} - 1$")
    print(f"{monedas_10} - 10$")
    print(f"{billetes_100} - 100$")
    print(f"{billetes_1000} - 1000$\n")


# --- FUNCIONES PARA CLIENTES ---

def ver_ofertas_vuelos_hoteles():
    print("--- CATÁLOGO DE VUELOS Y HOTELES ---")
    print("1. Vuelo Madrid - París: $350 por persona")
    print("2. Vuelo Cancún - Miami: $280 por persona")
    print("3. Hotel Resort Caribe (5 estrellas): $120 / noche")
    print("4. Hotel Plaza Ciudad (4 estrellas): $85 / noche")
    print("5. Paquete Completo (Vuelo + Hotel 3 noches): $750\n")

def agendar_viaje():
    print("--- AGENDAR UN VIAJE ---")
    destino = input("¿A qué destino deseas viajar?: ")
    fecha = input("Fecha estimada de viaje (DD/MM/AAAA): ")
    pasajeros = input("Número de personas: ")
    print(f"\n[!] Solicitud enviada. Un asesor agendará tu viaje a {destino} para el {fecha} ({pasajeros} pasajeros).\n")

def dejar_resena():
    print("--- DEJAR RESEÑA DE SERVICIO ---")
    lugar = input("¿Qué ciudad o servicio deseas calificar?: ")
    impression = input('Impresión general: ')
    liked = input('¿Qué te gustó?: ')
    disliked = input('¿Qué no te gustó?: ')
    
    total_length = len(impression) + len(liked) + len(disliked)
    discount = total_length * 0.1
    
    print(f"\n¡Gracias por tu reseña sobre {lugar}!")
    print(f"Has obtenido un cupón de descuento de: ${discount:.2f} para tu próximo viaje.\n")


# --- AUTENTICACIÓN Y MENÚS ---

def login_empleado():
    print("\n--- AUTENTICACIÓN DE EMPLEADO ---")
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    
    # Credenciales de prueba
    if usuario == "admin" and clave == "1234":
        print("\n[+] Acceso concedido. Bienvenido al panel operativo.")
        return True
    else:
        print("\n[-] Credenciales incorrectas. Acceso denegado.\n")
        return False

def menu_empleado():
    while True:
        print("=== PANEL DE EMPLEADO / AGENCIA ===")
        print("1. Registrar cliente en Hotel")
        print("2. Registrar Vuelo (con equipaje y grupo familiar)")
        print("3. Desglosar factura de cobro")
        print("0. Cerrar sesión / Volver")
        
        opcion = input("\nSelecciona una opción: ")
        print("-" * 35)

        if opcion == "1":
            registrar_cliente_hotel()
        elif opcion == "2":
            registrar_vuelo_familiar()
        elif opcion == "3":
            desglosar_factura()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.\n")

def menu_cliente():
    while True:
        print("=== PORTAL DE CLIENTES ===")
        print("1. Ver vuelos y hoteles disponibles (Precios)")
        print("2. Agendar un viaje")
        print("3. Dejar una reseña / calificar servicio")
        print("0. Salir / Volver")
        
        opcion = input("\nSelecciona una opción: ")
        print("-" * 35)

        if opcion == "1":
            ver_ofertas_vuelos_hoteles()
        elif opcion == "2":
            agendar_viaje()
        elif opcion == "3":
            dejar_resena()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.\n")

# --- FLUJO PRINCIPAL ---

def main():
    while True:
        print("========================================")
        print("     SISTEMA DE VIAJES Y TURISMO        ")
        print("========================================")
        print("1. Ingresar como Empleado")
        print("2. Ingresar como Cliente")
        print("0. Salir del programa")
        
        tipo_usuario = input("\nSelecciona tu perfil (1 o 2): ").strip()
        
        if tipo_usuario == "1":
            if login_empleado():
                menu_empleado()
        elif tipo_usuario == "2":
            menu_cliente()
        elif tipo_usuario == "0":
            print("¡Gracias por utilizar el sistema!")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()