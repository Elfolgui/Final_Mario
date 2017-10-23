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
Habilidad = Palabra(100, 400, Colores["Blanco"], "habilidad", 0)
Tiempo = Palabra(100, 500, Colores["Blanco"], "tiempo", 0)

Palabras = [[Puntos, False], [Vidas, False], [Monedas, False], [Habilidad, False], [Tiempo, False]]

reloj = Controlador.iniciar_reloj()

frames_totales = 0

Corazones = 4

cantidad_monedas = 10

Blitea = False

blitea_2 = False

Blitea_3 = False

Activar_Mostrar_Corazones = False

Activar_Animacion_Corazones = False

Activar_Preparar_Monedas = False

Activar_Mostrar_Monedas = False

Mostrar_Monedas = False

Activar_Animacion_Monedas = False

Activar_Animacion_Tiempo = False

Activar_Mostrar_Tiempo = False

Activar_Mostrar_Puntos_Habilidad = False

Activar_Animacion_Puntos_Habilidad = False

Activar_Mostrar_Puntos_Totales = False

restando = False

termine = False

posicion = 0

Mostrador = 0

Total_Monedas = 0

Puntos_Habilidad = 2000

aux = 0

aux2 = 0

Cero_mas = False

Cero_mas_2 = False

Cero_mas_3 = False

Cero_mas_4 = False

Hacer_Cuentas = False

frames_animacion_Corazones = 0

frames_mostrar_Corazones = 0

frames_cantidad_Corazones = 0

frames_mostrar_Monedas = 0

frames_cantidad_Monedas = 0

frames_animacion_Monedas = 0

frames_Controladores = 0

frames_Tiempo = 0

Respuesta = ""

Dos_Puntos = Sprite(290, 498, 20, 40, "Puntos.png")

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

Cero_Extra = Palabra(230, 500, Colores["Blanco"], "0", 50)
Cero_Extra_2 = Palabra(355, 500, Colores["Blanco"], "0", 50)

Puntos_Totales = 0

Restador = 0
Restar = 0
Total_Total = 0
Puntuacion_Corazones = 0
Puntuacion_Monedas = 0
Puntuacion_Habilidad = 0
Puntuacion_Tiempo = 0

Enemigos_Matados = 1200

M = 0

S = 0

Segundos = 120

Sumador = 0

posx = Moneda.rect.x
posy = Moneda.rect.y

Total_Monedas = cantidad_monedas

Mostrador_Puntos_Habilidad = Palabra(300, 395, Colores["Blanco"], str(Sumador), 60)

Puntuacion_Total = Palabra(780, 45, Colores["Blanco"], str(Puntos_Totales), 80)

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
        Activar_Mostrar_Puntos_Totales = True
        frames_mostrar = frames_totales
        posicion = -1

    if Activar_Mostrar_Puntos_Totales:
        if not Activar_Mostrar_Corazones and frames_totales < 200:
            frames_cantidad_Corazones = frames_totales
            Activar_Mostrar_Corazones = True
        ventana.blit(Puntuacion_Total.Palabra, (Puntuacion_Total.posX, Puntuacion_Total.posY))

    if Activar_Mostrar_Corazones and Corazones > 0 and frames_mostrar_Corazones + 50 < frames_totales and frames_cantidad_Corazones + 25 < frames_totales:
        frames_cantidad_Corazones = frames_totales
        Base.Grupo.add(Lista_Corazones[aux][0])
        Base.Corazones.add(Lista_Corazones[aux][0])
        aux += 1
        Corazones -= 1
        if Corazones == 0:
            Corazon = Sprite(625, 200, 40, 40, "Corazon.png")
            Corazon.rect.x = Lista_Corazones[aux][0].rect.x
            Corazon.rect.y = Lista_Corazones[aux][0].rect.y
            frames_animacion_Corazones = frames_totales
            Activar_Preparar_Monedas = True
            Activar_Mostrar_Corazones = False
            aux = 3

    if Activar_Animacion_Corazones and frames_animacion_Corazones + 100 < frames_totales:
        for Cora in Base.Corazones:
            Cora.Animacion_Corazones(frames_totales, ventana)
            if Cora.rect.y < 100 and Cora.rect.x > 700:
                Base.Grupo.remove(Cora)
                Base.Corazones.remove(Cora)
                Puntuacion_Corazones += 1000
                Puntos_Totales += 1000
                Puntuacion_Total = Palabra(780, 45, Colores["Blanco"], str(Puntos_Totales), 80)
        if len(Base.Corazones.sprites()) == 0:
            Respuesta = True

    if Respuesta:
        Activar_Animacion_Corazones = False
        Activar_Animacion_Monedas = True

    if Activar_Preparar_Monedas:
        Base.Grupo.add(Moneda_1)
        Activar_Preparar_Monedas = False
        Mostrar_Monedas = True

    if Mostrar_Monedas and frames_cantidad_Monedas + 20 < frames_totales:
        Blitea = True
        Numero = Palabra(390, 295, Colores["Blanco"], str(Mostrador), 60)
        if Mostrador != Total_Monedas + 1:
            Mostrador += 1
        if Total_Monedas + 1 == Mostrador:
            Mostrador = 10
            Mostrar_Monedas = False
            Activar_Mostrar_Puntos_Habilidad = True

    if Activar_Animacion_Monedas and Total_Monedas >= 0:
        if Base.Grupo.has(Moneda):
            frames_animacion_Monedas = frames_totales
            if Moneda.Animacion_Monedas(posx, posy):
                Mostrador -= 1
                Puntuacion_Monedas += 200
                Puntos_Totales += 200
                Numero = Palabra(390, 295, Colores["Blanco"], str(Mostrador), 60)
                Puntuacion_Total = Palabra(780, 45, Colores["Blanco"], str(Puntos_Totales), 80)
                Total_Monedas -= 1
        else:
            Base.Grupo.add(Moneda)
        if Total_Monedas == -1:
            Blitea = False
            Base.Grupo.remove(Moneda)
            Base.Grupo.remove(Moneda_1)
            Activar_Animacion_Puntos_Habilidad = True
            frames_Controladores = frames_totales

    if Activar_Mostrar_Tiempo:
        Cero_mas = True
        S += 1
        if S == 60:
            M += 1
            S -= 60
        if S + (M * 60) == Segundos:
            if M > 10:
                Cero_mas = False
            if S < 10:
                Cero_mas_2 = True
                Cero_Extra_2.posX -= 40
            Activar_Mostrar_Tiempo = False
            Activar_Animacion_Corazones = True
        Tiempo_Segundos = Palabra(320, 500, Colores["Blanco"], str(S), 50)
        Tiempo_Minutos = Palabra(260, 500, Colores["Blanco"], str(M), 50)
        Base.Grupo.add(Dos_Puntos)
        blitea_2 = True

    if Activar_Animacion_Tiempo and frames_Tiempo + 20 < frames_totales:
        Cero_mas_2 = False
        Puntos_Totales -= 10
        Puntuacion_Total = Palabra(780, 45, Colores["Blanco"], str(Puntos_Totales), 80)
        if M == 0:
            termine = True
        if termine and S == 0:
            S = 0
            Cero_mas_2 = True
            Activar_Animacion_Tiempo = False
            Hacer_Cuentas = True
        if S == 0 and not termine:
            print("Entre")
            M -= 1
            S = 60
        if Activar_Animacion_Tiempo:
            S -= 1
        Tiempo_Segundos = Palabra(320, 500, Colores["Blanco"], str(S), 50)
        Tiempo_Minutos = Palabra(260, 500, Colores["Blanco"], str(M), 50)

    if blitea_2 and not Cero_mas_2:
        ventana.blit(Tiempo_Minutos.Palabra, (Tiempo_Minutos.posX, Tiempo_Minutos.posY))
        ventana.blit(Tiempo_Segundos.Palabra, (Tiempo_Segundos.posX, Tiempo_Segundos.posY))
    if Cero_mas:
        ventana.blit(Cero_Extra.Palabra, (Cero_Extra.posX, Cero_Extra.posY))
    if Cero_mas_2:
        ventana.blit(Cero_Extra_2.Palabra, (Cero_Extra_2.posX, Cero_Extra_2.posY))
        ventana.blit(Tiempo_Minutos.Palabra, (Tiempo_Minutos.posX, Tiempo_Minutos.posY))
        ventana.blit(Tiempo_Segundos.Palabra, (Tiempo_Segundos.posX + 25, Tiempo_Segundos.posY))

    if Blitea:
        ventana.blit(x.Palabra, (x.posX, x.posY))
        ventana.blit(Numero.Palabra, (Numero.posX, Numero.posY))
    if Blitea_3:
        ventana.blit(Mostrador_Puntos_Habilidad.Palabra, (Mostrador_Puntos_Habilidad.posX, Mostrador_Puntos_Habilidad.posY))

    if Activar_Mostrar_Puntos_Habilidad:
        if Sumador == Puntos_Habilidad:
            Activar_Mostrar_Tiempo = True
            Activar_Mostrar_Puntos_Habilidad = False
        Blitea_3 = True
        Mostrador_Puntos_Habilidad = Palabra(300, 395, Colores["Blanco"], str(Sumador), 60)
        Sumador += 25

    if Activar_Animacion_Puntos_Habilidad and frames_Controladores + 20 < frames_totales:
        Mostrador_Puntos_Habilidad = Palabra(300, 395, Colores["Blanco"], str(Sumador), 60)
        Puntuacion_Total = Palabra(780, 45, Colores["Blanco"], str(Puntos_Totales), 80)
        Sumador -= 25
        Enemigos_Matados -= 25
        if Enemigos_Matados <= 0 and Sumador == 0:
            Blitea_3 = False
            Activar_Animacion_Puntos_Habilidad = False
            Activar_Animacion_Tiempo = True
            frames_Tiempo = frames_totales
        if Activar_Animacion_Puntos_Habilidad:
            Puntos_Totales += 25
            Puntuacion_Habilidad += 25

    if Hacer_Cuentas:
        Total_Total = ((Puntuacion_Corazones + Puntuacion_Habilidad + Puntuacion_Monedas) / Segundos) * 1200
        Restar = Puntos_Totales - Total_Total
        Restador = (Restar/Segundos)

    if Total_Total <= Puntos_Totales:
        Puntos_Totales -= Restador

    pygame.display.update()
    frames_totales += 1