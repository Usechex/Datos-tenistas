def es_numero(valor):# Defino tipo de variable float solo altura para estatura 
        try:
            float(valor)
            return True 
        except ValueError:
            return False
 #Defino registro del jugador 

def registrar_jugador ():   
    while True: 
        Nombre = input("Ingrese Nombre del juegador de tennis ")
        if Nombre.isalpha():
                break
        else:
                print("Ingrese solo el nombre del jugador")
                
    
    while True:
        edad = ((input)("Ingrese la edad del jugador "))
        if edad.isdigit():
            edad = int(edad)
            break
        else:
                print("Ingrese solo la edad del jugador")
            
            
    while True:        
        Estatura = ((input)("ingrese la estatura del jugador "))
        if es_numero(Estatura):
                Estatura = float(Estatura)
                break
        else:
                print("Ingrese solo la estatura")
                
    
    return{"Nombre":Nombre,"edad":edad,"Estatura":Estatura}
    
# Defino mostar jugadores 

def mostrar_jugadores(jugadores):
    if not jugadores:
        print("no hay jugadores registrados ")  
        return
        
    for i, jugador in enumerate(jugadores, start=1):
     print(f"\njugador {i}")
     print(f"Nombre: {jugador['Nombre']}")
     print(f"edad: {jugador['edad']}")
     print (f"Estatura {jugador['Estatura']}")
     
# para actualizar los jugadores 
def actualizar_jugadores(jugadores):
    mostrar_jugadores(jugadores)
    if not  jugadores:
        return 
    try: 
        num = int(input("\ningrese el numero del jugador que quiere actualizar:"))
        jugador = jugadores[num-1]
        print("\n Actualizando jugador:")
        for key in jugador :
            nuevo_valor = input(f"ingrese nuevo valor para {key} (presione enter para mantener {jugador[key]}):")
            if nuevo_valor :
                if key =="Nombre" and nuevo_valor.isalpha():
                    jugador[key] = nuevo_valor
                elif key == "edad" and nuevo_valor.isdigit():
                    jugador[key] = int(nuevo_valor)
                elif key =="Estatura" and es_numero(nuevo_valor):   
                    jugador[key] = float(nuevo_valor)
                else:
                    print(f"valor invalido para {key}. no se actualizo")
    except (IndexError, ValueError):
        print("Numero de jugador no valido")
    
def eliminar_jugadores(jugadores): # Para eliminar los jugadores 
    mostrar_jugadores(jugadores)
    if not jugadores:
        return
    
    try:
        num=int(input("\nIngrese el numero del jugador que quiere eliminar: "))
        jugadores.pop(num- 1)
        print("jugador eliminador.")
    except(IndexError, ValueError):
        print("numero de jugador no valido.")
    

def menu ():
    jugadores = []
    while True:
        print("\n--------menu-----")
        print("1. Registrar jugador")
        print("2. Mostrar jugadores")
        print("3. Actualizar jugadores")
        print("4. Eliminar jugador")
        print("5. Volver ")
        opcion = input("seleccione una opcion ")
        
        if opcion == "1":
            jugadores.append(registrar_jugador())
        elif opcion == "2":
            mostrar_jugadores(jugadores)
        elif opcion =="3":
            actualizar_jugadores(jugadores)
        elif opcion == "4":
            eliminar_jugadores(jugadores)
        elif opcion =="5":
            print("saliendo del programa...")
            break
        else:
            print("opcion no valida vuelva a intentar porfavor")

menu()