#JUEGO MODO HISTORIA

print("CONTEXTO: Sos un viajero en un mundo post-apocaliptico y estas en las ruinas de tu ciudad y escuchaste en una radio la existencia de un refugio\nnecesitas llegar ahi antes de la noche y que salgan las criaturas.\n ¡¡SUERTE EN ESTA AVENTURA!!")

nombre=input("Ingrese el nombre para su personaje en esta historia: ")
print(f"Hola {nombre}, usted esta por entrar a un juego de toma de decisiones, Bienvenido!!.")
print("tienes una mochila con una linterna con poca bateria, un cuchillo, una botella de agua a medio llenar.")
camino=int(input("Caminando por la ciudad encuentras 3 caminos, el primero por el centro de la ciudad, otro es un bosque y por ultimo las vias del tren.\n¿Cual eliges?(1,2 o 3): "))
if camino==1:
    print("Es un camino directo, pero hay saqueadores.")
    print("A lo lejos escuchas voces y pasos, es un grupo de saqueadores.")
    decision=int(input("tienes 3 posibilidades\nla primera evitarlos y tomar desvios\nLa segunda los enfrentas con el cuchillo\nLa tercera ofreces negociar agua para pasar\n¿Cual decides? (1,2 o 3): "))
    if decision==1:
        print("Perdes mucho tiempo y se acerca la noche")
    elif decision==2:
        print("Logras derrotarlos pero salis herido pero encontras para curarte en sus cosas.")
    elif decision==3:
        print("Ellos aceptan, pero perdes lo que te quedo de agua.")
if camino==2:
    print("Es una ruta tranquila pero lenta, y no sabes que puede haber detras de cada arbol.")
    print("Caminando escuchas gruñidos cerca, que se acercaron cuando pisaste hojas secas.")
    decision=int(input("¿Que vas a hacer?\n1:Prender la linterna\n2:Avanzar en silencio\n3:trepar un arbol para observar desde arriba\n1,2 o 3: "))
    if decision==1: 
        print("Atraes la atencion de la criatura, pero pudiste escapar pero perdiste la mochila.")
    elif decision==2:
        print("Pasaste desapercibido, pero estas muy cansado.")
    elif decision==3:
        print("Descubres que esta todo despejado pero perdiste muchisimo tiempo.")
if camino==3:
    print("Una direccion rara, pero con posibilidad de encontrar algo util.")
    print("Caminando encontras un vagon y hay muchas cosas utiles.")
    decision=int(input("¿Que vas a hacer?\n1:revisas rapido y te vas con lo que puedas\n2:ignoras el vagon y seguis\n3:te escondes en el vagon para descansar\n1,2 o 3: "))
    if decision==1:
        print("Encontras muchos suministros, pero algo o alguien empieza a seguirte.")
    elif decision==2:
        print("No perdes tiempo, pero no encontraste recursos.")
    elif decision==3:
        print("Recuperas energia, pero perdiste demasiado tiempo.")

if camino==1 or camino==2:
    print(f"Bien {nombre}, si llegaste hasta aca es porque sobreviviste a todo.")
    print("Elegiste bien hasta aca pero todo se determinara aca una ultima decision aparecio, a lo lejos se ve el refugio ¿que vas a hacer?")
    decision2=int(input("1:Haces el ultimo esfuerzo y corres sin mirar atras\n2:Te escondes y esperas al amanecer arriesgandote que te atrapen\n¿Cual elegis? (1 o 2): "))
    if decision2==1:
        print(f"¡¡Felicitaciones {nombre}!!\nLograste llegar al refugio antes que las puertas se cierren y descubriste una comunidad que comenzo reconstruirse.")
    elif decision2==2:
        print(f"¡¡Bien {nombre}!!\nSobvreviviste la noche escondido, pero no encontraste el refugio y vas a seguir vagando en busca del refugio.")
if camino==3:
    print("Perdon:( No lograste sobrevivir las criaturas te alcanzaron y tu ultima vision fue el refugio a lo lejos. )")