from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255)}

Fuente_1 = 70

Fuente_2 = 50

ancho, alto = 1280, 720

FPS = 120

#Fondo = Sprite(0,0, 1360, 768, "Fondo.png")

ventana = Controlador.configurar_pantalla()

Controlador.rellenar_pantalla(ventana, Colores)

T_1 = pygame.font.SysFont("mariokartdsregular", 0)
T_2 = pygame.font.SysFont("mariokartdsregular", 14)
T_3 = pygame.font.SysFont("mariokartdsregular", 28)
T_4 = pygame.font.SysFont("mariokartdsregular", 42)
T_5 = pygame.font.SysFont("mariokartdsregular", 56)
T_6 = pygame.font.SysFont("mariokartdsregular", 70)

Lista = [T_1,T_2,T_3,T_4,T_5,T_6]

Puntos = Palabra(120, 50, Colores["Blanco"], "puntuacion  final", 0)
Vidas = Palabra(100, 200, Colores["Blanco"], "vidas", 0)
Monedas = Palabra(100, 300, Colores["Blanco"], "monedas", 0)
Tiempo = Palabra(100, 400, Colores["Blanco"], "tiempo", 0)
Habilidad = Palabra(100, 500, Colores["Blanco"], "habilidad", 0)

Palabras = [[Puntos, False], [Vidas, False], [Monedas, False], [Tiempo, False], [Habilidad, False]]

reloj = Controlador.iniciar_reloj()

frames_totales = 0

Corazones = 4

cantidad_monedas = 10

Blitea = False

Activar_Mostrar_Corazones = False

Activar_Animacion_Corazones = False

Activar_Preparar_Monedas = False

Activar_Mostrar_Monedas = False

Mostrar_Monedas = False

Activar_Animacion_Monedas = False

posicion = 0

Mostrador = 0

Total_Monedas = 0

aux = 0

frames_animacion_Corazones = 0

frames_mostrar_Corazones = 0

frames_cantidad_Corazones = 0

frames_mostrar_Monedas = 0

frames_cantidad_Monedas = 0

frames_animacion_Monedas = 0

Respuesta = ""

Corazon_1 = Sprite(250, 200, 40, 40, "Corazon.png")
Corazon_2 = Sprite(325, 200, 40, 40, "Corazon.png")
Corazon_3 = Sprite(400, 200, 40, 40, "Corazon.png")
Corazon_4 = Sprite(475, 200, 40, 40, "Corazon.png")
Corazon_5 = Sprite(550, 200, 40, 40, "Corazon.png")
Corazon_6 = Sprite(625, 200, 40, 40, "Corazon.png")

Lista_Corazones = [[Corazon_1, False], [Corazon_2, False], [Corazon_3, False],
                   [Corazon_4, False], [Corazon_5, False], [Corazon_6, False]]

Lista_Monedas_Activas = []
Lista_Monedas_Pasivas = []

Total_Monedas = cantidad_monedas

x = Palabra(350, 305, Colores["Blanco"], "x", 40)

while True:
    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()
    Controlador.set_fps(reloj, FPS)
    Controlador.rellenar_pantalla(ventana, Colores)
    #ventana.blit(Fondo.image, Fondo.rect)
    Base.Grupo.draw(ventana)

    for i in Palabras:
        if i[1]:
            ventana.blit(i[0].Palabra, (i[0].posX, i[0].posY))

    if Mostrar_Monedas and frames_cantidad_Monedas + 10 < frames_totales:
        Blitea = True
        frames_cantidad_Monedas = frames_totales
        Numero = Palabra(390, 295, Colores["Blanco"], str(Mostrador), 60)
        Base.Grupo.add(Lista_Monedas_Activas[Mostrador])
        if Mostrador != Total_Monedas:
            Mostrador += 1
        if Total_Monedas == Mostrador:
            Mostrar_Monedas = False
            Activar_Animacion_Monedas = True

    if Activar_Animacion_Monedas and frames_animacion_Monedas + 5 < frames_totales:
        frames_animacion_Monedas = frames_totales
        for selector in Lista_Monedas_Activas:
            if selector.Animacion_Monedas(frames_totales):
                Activar_Animacion_Corazones = True

    if Blitea:
        ventana.blit(x.Palabra, (x.posX, x.posY))
        ventana.blit(Numero.Palabra, (Numero.posX, Numero.posY))
    if frames_totales <= 70 and posicion == 0:
        Palabras[posicion][1] = True
        Palabras[posicion][0].Aparecer(frames_totales, Colores["Blanco"])
    elif frames_totales > 70 and posicion == 0:
        frames_totales = 0
        posicion += 1
    elif frames_totales <= 50 and 0 < posicion < 5:
        Palabras[posicion][1] = True
        Palabras[posicion][0].Aparecer(frames_totales, Colores["Blanco"])
    elif frames_totales > 50 and 0 < posicion < 5:
        frames_totales = 0
        posicion += 1
    if posicion == 5:
        Activar_Mostrar_Corazones = True
        frames_mostrar = frames_totales
        posicion = -1

    if Activar_Mostrar_Corazones and Corazones > 0 and frames_mostrar_Corazones + 50 < frames_totales and frames_cantidad_Corazones + 25 < frames_totales:
        frames_cantidad_Corazones = frames_totales
        Base.Grupo.add(Lista_Corazones[aux][0])
        aux += 1
        Corazones -= 1
        if Corazones == 0:
            frames_animacion_Corazones = frames_totales
            Activar_Preparar_Monedas = True
            aux = 0

    if Activar_Preparar_Monedas:
        frames_mostrar_Monedas = frames_totales
        Moneda_1 = Sprite(300, 300, 40, 40, "Moneda_1.png")
        Lista_Monedas_Pasivas.append(Moneda_1)
        cantidad_monedas -= 1
        if cantidad_monedas <= 0:
            Moneda_1 = Sprite(300, 300, 40, 40, "Moneda_1.png")
            Base.Grupo.add(Moneda_1)
            Activar_Preparar_Monedas = False
            Activar_Mostrar_Monedas = True

    if Activar_Mostrar_Monedas:
        Mostrar_Monedas = True
        for Moneda in Lista_Monedas_Pasivas:
            Lista_Monedas_Activas.append(Moneda)

    if Activar_Animacion_Corazones and frames_animacion_Corazones + 100 < frames_totales:
        for Cora in Lista_Corazones:
            Respuesta = Cora[0].Animacion_Corazones(frames_totales)

    pygame.display.update()
    frames_totales += 1