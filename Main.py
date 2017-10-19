from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255)}

Fuente_1 = 70

Fuente_2 = 50

ancho, alto = 1280, 720

FPS = 120

ventana = Controlador.configurar_pantalla(ancho, alto)

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

Activar_Mostrar = False

Activar_Animacion = False

posicion = 0

aux = 0

Respuesta = ""

Corazon_1 = Sprite(250, 200, 40, 40, "Corazon.png")
Corazon_2 = Sprite(325, 200, 40, 40, "Corazon.png")
Corazon_3 = Sprite(400, 200, 40, 40, "Corazon.png")
Corazon_4 = Sprite(475, 200, 40, 40, "Corazon.png")
Corazon_5 = Sprite(550, 200, 40, 40, "Corazon.png")
Corazon_6 = Sprite(625, 200, 40, 40, "Corazon.png")

Lista_Corazones = [[Corazon_1, False], [Corazon_2, False], [Corazon_3, False],
                   [Corazon_4, False], [Corazon_5, False], [Corazon_6, False]]

while True:
    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()
    Controlador.set_fps(reloj, FPS)
    Controlador.rellenar_pantalla(ventana, Colores)
    for i in Palabras:
        if i[1]:
            ventana.blit(i[0].Palabra, (i[0].posX, i[0].posY))
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
        Activar_Mostrar = True
        posicion = -1
    if Activar_Mostrar and Corazones > 0 and frames_totales % 20 == 0:
        Base.Grupo.add(Lista_Corazones[aux][0])
        aux += 1
        Corazones -= 1
        if Corazones == 0:
            Activar_Animacion = True
            aux = 0
    if Activar_Animacion:
        for Cora in Lista_Corazones:
            Respuesta = Cora[0].Animacion(frames_totales)
        Controlador.Mostrar(Corazones)
    if Respuesta == "Llegue":
        break
    Base.Grupo.draw(ventana)
    pygame.display.update()
    frames_totales += 1