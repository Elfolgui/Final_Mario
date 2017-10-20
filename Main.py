from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255)}

Fuente_1 = 70

Fuente_2 = 50

ancho, alto = 1280, 720

FPS = 120

ventana = Controlador.configurar_pantalla(ancho, alto)

Controlador.rellenar_pantalla(ventana, Colores)

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

blitea_2 = False

Activar_Mostrar_Corazones = False

Activar_Animacion_Corazones = False

Activar_Preparar_Monedas = False

Activar_Mostrar_Monedas = False

Mostrar_Monedas = False

Activar_Animacion_Monedas = False

Activar_Animacion_Tiempo = False

Activar_Mostrar_Tiempo = False

restando = False

termine = False

posicion = 0

Mostrador = 0

Total_Monedas = 0

aux = 0

aux2 = 0

Cero_mas = False

Cero_mas_2 = False

Cero_mas_3 = False

Cero_mas_4 = False

frames_animacion_Corazones = 0

frames_mostrar_Corazones = 0

frames_cantidad_Corazones = 0

frames_mostrar_Monedas = 0

frames_cantidad_Monedas = 0

frames_animacion_Monedas = 0

Respuesta = ""

Dos_Puntos = Sprite(290, 398, 20, 40, "Puntos.png")

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

Moneda_1 = Sprite(300, 300, 40, 40, "Moneda_1.png")
Moneda = Sprite(300, 300, 40, 40, "Moneda_1.png")

Cero_Extra = Palabra(230, 400, Colores["Blanco"], "0", 50)
Cero_Extra_2 = Palabra(350, 400, Colores["Blanco"], "0", 50)

#Reloj = Sprite(300 , 400, 40, 40, "Reloj.png")

M = 0

S = 0

Segundos = 130

posx = Moneda.rect.x
posy = Moneda.rect.y

Total_Monedas = cantidad_monedas

x = Palabra(350, 305, Colores["Blanco"], "x", 40)

while True:
    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()
    Controlador.set_fps(reloj, FPS)
    Controlador.rellenar_pantalla(ventana, Colores)
    Base.Grupo.draw(ventana)

    for i in Palabras:
        if i[1]:
            ventana.blit(i[0].Palabra, (i[0].posX, i[0].posY))

    if Mostrar_Monedas and frames_cantidad_Monedas + 7 < frames_totales:
        Blitea = True
        frames_cantidad_Monedas = frames_totales
        Numero = Palabra(390, 295, Colores["Blanco"], str(Mostrador), 60)
        if Mostrador != Total_Monedas + 1:
            Mostrador += 1
        if Total_Monedas + 1 == Mostrador:
            Mostrador = 10
            Mostrar_Monedas = False
            Activar_Mostrar_Tiempo = True

    if Activar_Mostrar_Tiempo:
        S += 1
        if S == 60:
            M += 1
            S -= 60
        if S + (M * 60) == Segundos:
            if M < 10:
                Cero_mas = True
            if S < 10:
                Cero_mas_2 = True
            Activar_Animacion_Corazones = True
            Activar_Mostrar_Tiempo = False
        Tiempo_Segundos = Palabra(320, 400, Colores["Blanco"], str(S), 50)
        Tiempo_Minutos = Palabra(260, 400, Colores["Blanco"], str(M), 50)
        Base.Grupo.add(Dos_Puntos)
        blitea_2 = True

    if Activar_Animacion_Tiempo:
        S -= 1
        if M == 0:
            termine = True
        if termine and S == 0:
            S = 0
            Cero_mas_2 = True
            Activar_Animacion_Tiempo = False
        if S == 0 and not termine:
            M -= 1
            S = 60
        Tiempo_Segundos = Palabra(320, 400, Colores["Blanco"], str(S), 50)
        Tiempo_Minutos = Palabra(260, 400, Colores["Blanco"], str(M), 50)

    if Activar_Animacion_Monedas and Total_Monedas >= 0:
        if Base.Grupo.has(Moneda):
            frames_animacion_Monedas = frames_totales
            if Moneda.Animacion_Monedas(posx, posy):
                Mostrador -= 1
                Numero = Palabra(390, 295, Colores["Blanco"], str(Mostrador), 60)
                Total_Monedas -= 1
        else:
            Base.Grupo.add(Moneda)
        if Total_Monedas == -1:
            Blitea = False
            Base.Grupo.remove(Moneda)
            Base.Grupo.remove(Moneda_1)
            Activar_Animacion_Tiempo = True

    if blitea_2:
        ventana.blit(Tiempo_Minutos.Palabra, (Tiempo_Minutos.posX, Tiempo_Minutos.posY))
        ventana.blit(Tiempo_Segundos.Palabra, (Tiempo_Segundos.posX, Tiempo_Segundos.posY))
    if Cero_mas:
        ventana.blit(Cero_Extra.Palabra, (Cero_Extra.posX, Cero_Extra.posY))
    if Cero_mas_2:
        ventana.blit(Cero_Extra_2.Palabra, (Cero_Extra_2.posX, Cero_Extra_2.posY))

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
            Corazon = Sprite(625, 200, 40, 40, "Corazon.png")
            Corazon.rect.x = Lista_Corazones[aux][0].rect.x
            Corazon.rect.y = Lista_Corazones[aux][0].rect.y
            frames_animacion_Corazones = frames_totales
            Activar_Preparar_Monedas = True
            aux = 3

    if Activar_Preparar_Monedas:
        Base.Grupo.add(Moneda_1)
        Activar_Preparar_Monedas = False
        Mostrar_Monedas = True

    if Activar_Animacion_Corazones and frames_animacion_Corazones + 100 < frames_totales:
        for Cora in Lista_Corazones:
            Respuesta = Cora[0].Animacion_Corazones(frames_totales, ventana)

    if Respuesta:
        frames_cantidad_Monedas = frames_totales
        Activar_Animacion_Corazones = False
        Activar_Animacion_Monedas = True

    pygame.display.update()
    frames_totales += 1