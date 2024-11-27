print("BIENVENIDO AL LEGENDARIO JUEGO DE PIEDRA, PAPEL O TIJERA!!!")
while True:
    nombre1 = input("ingrese el nombre del Jugador 1: ")
    nombre2 = input("ingrese el nombre del Jugador 2: ")
    
    a = int(input("Jugador 1: \n1=Piedra 2=Papel 3=Tijera: "))
    b = int(input("Jugador 2: \n1=Piedra 2=Papel 3=Tijera: "))
    
    if a == 1 and b == 3:
        print(f"Gana {nombre1}! Piedra le gana a tijera :)")
    elif a== 2 and b == 1:
        print(f"Gana {nombre1}! Papel le gana a la piedra")
    elif a== 3 and b == 2:
        print(f"Gana {nombre1}! Tijera le gana a papel")
    
    elif b== 1 and a== 3:
        print(f"Gana {nombre2} Piedra le gana a tijera")
    elif b== 2 and a == 1:
        print(f"Gana {nombre2} Papel le gana a la piedra")
    elif b== 3 and a == 2:
        print(f"Gana {nombre2} Tijera le gana a papel")
    else:
        print("Nadie gana! :(")
        break
