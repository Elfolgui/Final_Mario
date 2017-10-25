from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255), "Verde": (50, 205, 50), "Rojo": (255, 0, 0)}

Fuente_1 = 70

Fuente_2 = 50

ancho, alto = 1280, 720

FPS = 120

ventana = Controlador.configurar_pantalla(ancho, alto)

Controlador.rellenar_pantalla(ventana, Colores)

Puntos = Palabra(120, 50, Colores["Blanco"], "puntuacion  final", 0)
Vidas = Palabra(100, 200, Colores["Blanco"], "vidas", 0)
Monedas = Palabra(100, 300, Colores["Blanco"], "monedas", 0)
Estilo = Palabra(100, 400, Colores["Blanco"], "estilo", 0)
Tiempo = Palabra(100, 500, Colores["Blanco"], "tiempo", 0)

Palabras = [[Puntos, False], [Vidas, False], [Monedas, False], [Estilo, False], [Tiempo, False]]

reloj = Controlador.iniciar_reloj()

frames_totales = 0

Corazones = 4

cantidad_monedas = 10

posicion = 0

Mostrador = 0

Total_Monedas = 0

aux = 0

aux2 = 0

aux_3 = True

Cero_mas = False

Cero_mas_2 = False

Cero_mas_3 = False

Cero_mas_4 = False

Hacer_Cuentas = False

Activar_Mostrar_Puntuacion_Corazones = False

Activar_Mostrar_Puntuacion_Monedas = False

Blitea = False

blitea_2 = False

Blitea_3 = False

Blitea_4 = False

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

frames_animacion_Corazones = 0

frames_mostrar_Corazones = 0

frames_cantidad_Corazones = 0

frames_mostrar_Monedas = 0

frames_cantidad_Monedas = 0

frames_animacion_Monedas = 0

frames_Controladores = 0

frames_mostrar_Puntos_Habilidad = 0

frames_tardar_mostrar = 0

frames_Tiempo = 0

Respuesta = ""

Dos_Puntos_1 = Sprite(660, 50, 30, 55, "Puntos.png")
Dos_Puntos_2 = Sprite(190, 197, 25, 45, "Puntos.png")
Dos_Puntos_3 = Sprite(260, 297, 25, 45, "Puntos.png")
Dos_Puntos_4 = Sprite(210, 397, 25, 45, "Puntos.png")
Dos_Puntos_5 = Sprite(210, 495, 25, 45, "Puntos.png")
Dos_Puntos_6 = Sprite(308, 497, 25, 45, "Puntos.png")

Lista_Puntos = [Dos_Puntos_1, Dos_Puntos_2, Dos_Puntos_3, Dos_Puntos_4, Dos_Puntos_5, Dos_Puntos_6]

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

Cero_Extra = Palabra(247, 495, Colores["Rojo"], "0", 60)
Cero_Extra_2 = Palabra(375, 495, Colores["Rojo"], "0", 60)

Puntos_Totales = 0

Restador = 0
Restar = 0
Total_Total = 1900000000000000000

Puntuacion_Corazones = 0
Puntuacion_Monedas = 0
Puntuacion_Habilidad = 0
Puntuacion_Tiempo = 0

Enemigos_Matados = 1200

M = 0

S = 0

Segundos = 120

Sumador = 0

Mostrar_sumador = 0

posx = Moneda.rect.x
posy = Moneda.rect.y

Total_Monedas = cantidad_monedas

Mostrador_Puntos_Habilidad = Palabra(340, 395, Colores["Blanco"], str(Sumador), 60)

Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)

x_1 = Palabra(350, 305, Colores["Blanco"], "x", 40)
x_2 = Palabra(238, 208, Colores["Blanco"], "x", 40)
x_3 = Palabra(300, 308, Colores["Blanco"], "x", 40)
x_4 = Palabra(243, 408, Colores["Blanco"], "x", 40)

Mastil_Posicion = 200
Cantidad_Signos = 3
Hizo_algo = True

Puntos_Habilidad = (Mastil_Posicion * 4 + Cantidad_Signos * 100 + Hizo_algo)

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
        Base.Grupo.add(Lista_Puntos[posicion])
        posicion += 1
    elif frames_totales <= 50 and 0 < posicion < 5:
        Palabras[posicion][1] = True
        Palabras[posicion][0].Aparecer(frames_totales, Colores["Blanco"])
    elif frames_totales > 50 and 0 < posicion < 5:
        frames_totales = 0
        Base.Grupo.add(Lista_Puntos[posicion])
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
            frames_cantidad_Monedas = frames_totales
            Activar_Preparar_Monedas = True
            Activar_Mostrar_Corazones = False
            aux = 3

    if Activar_Animacion_Corazones and frames_animacion_Corazones + 70 < frames_totales:
        for Cora in Base.Corazones:
            Cora.Animacion_Corazones(frames_totales, ventana)
            if Cora.rect.y < 100 and Cora.rect.x > 700:
                Base.Grupo.remove(Cora)
                Base.Corazones.remove(Cora)
                Puntuacion_Corazones += 1000
                Puntos_Totales += 1000
                Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)
        if len(Base.Corazones.sprites()) == 0:
            Respuesta = True
            Activar_Mostrar_Puntuacion_Corazones = True
            Puntuacion_Corazon = Palabra(270, 195, Colores["Verde"], str(Puntuacion_Corazones), 60)

    if Respuesta:
        Activar_Animacion_Corazones = False
        Activar_Animacion_Monedas = True

    if Activar_Preparar_Monedas:
        Activar_Preparar_Monedas = False
        Mostrar_Monedas = True

    if Mostrar_Monedas and frames_cantidad_Monedas + 50 < frames_totales and frames_tardar_mostrar + 5 < frames_totales:
        frames_tardar_mostrar = frames_totales
        Base.Grupo.add(Moneda_1)
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
                Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)
                Total_Monedas -= 1
        else:
            Base.Grupo.add(Moneda)
        if Total_Monedas == -1:
            Blitea = False
            Base.Grupo.remove(Moneda)
            Base.Grupo.remove(Moneda_1)
            Activar_Animacion_Puntos_Habilidad = True
            Activar_Mostrar_Puntuacion_Monedas = True
            frames_Controladores = frames_totales
            Puntuacion_Moneda = Palabra(335, 295, Colores["Verde"], str(Puntuacion_Monedas), 60)

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
        Tiempo_Segundos = Palabra(340, 495, Colores["Rojo"], str(S), 60)
        Tiempo_Minutos = Palabra(280, 495, Colores["Rojo"], str(M), 60)
        Base.Grupo.add(Dos_Puntos_6)
        blitea_2 = True

    if Activar_Animacion_Tiempo and frames_Tiempo + 70 < frames_totales:
        Cero_mas_2 = False
        if M == 0:
            termine = True
        if termine and S == 0:
            S = 0
            Cero_mas_2 = True
            Activar_Animacion_Tiempo = False
        if S == 0 and not termine:
            M -= 1
            S = 60
        if Activar_Animacion_Tiempo:
            S -= 1
            Hacer_Cuentas = True
        Tiempo_Segundos = Palabra(340, 495, Colores["Rojo"], str(S), 60)
        Tiempo_Minutos = Palabra(280, 495, Colores["Rojo"], str(M), 60)

    if blitea_2 and not Cero_mas_2:
        ventana.blit(Tiempo_Minutos.Palabra, (Tiempo_Minutos.posX, Tiempo_Minutos.posY))
        ventana.blit(Tiempo_Segundos.Palabra, (Tiempo_Segundos.posX, Tiempo_Segundos.posY))
    if Cero_mas:
        ventana.blit(Cero_Extra.Palabra, (Cero_Extra.posX, Cero_Extra.posY))
    if Cero_mas_2:
        ventana.blit(Cero_Extra_2.Palabra, (Cero_Extra_2.posX, Cero_Extra_2.posY))
        ventana.blit(Tiempo_Minutos.Palabra, (Tiempo_Minutos.posX, Tiempo_Minutos.posY))
        ventana.blit(Tiempo_Segundos.Palabra, (Tiempo_Segundos.posX + 28, Tiempo_Segundos.posY))

    if Blitea:
        ventana.blit(x_1.Palabra, (x_1.posX, x_1.posY))
        ventana.blit(Numero.Palabra, (Numero.posX, Numero.posY))
    if Blitea_3:
        ventana.blit(Mostrador_Puntos_Habilidad.Palabra, (Mostrador_Puntos_Habilidad.posX, Mostrador_Puntos_Habilidad.posY))
    if Blitea_4:
        ventana.blit(x_4.Palabra, (x_4.posX, x_4.posY))
        Mostrador_Puntos_Habilidad = Palabra(273, 395, Colores["Verde"], str(Mostrar_sumador), 60)
        ventana.blit(Mostrador_Puntos_Habilidad.Palabra, (Mostrador_Puntos_Habilidad.posX, Mostrador_Puntos_Habilidad.posY))

    if Activar_Mostrar_Puntos_Habilidad and frames_mostrar_Puntos_Habilidad + 10 < frames_totales:
        frames_mostrar_Puntos_Habilidad = frames_totales
        if Sumador >= Puntos_Habilidad:
            Mostrar_sumador = Sumador
            Activar_Mostrar_Tiempo = True
            Activar_Mostrar_Puntos_Habilidad = False
        Blitea_3 = True
        Mostrador_Puntos_Habilidad = Palabra(245, 395, Colores["Blanco"], str(Sumador), 60)
        Sumador += 100

    if Activar_Animacion_Puntos_Habilidad and frames_Controladores + 10 < frames_totales:
        Mostrador_Puntos_Habilidad = Palabra(245, 395, Colores["Blanco"], str(Sumador), 60)
        Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)
        Sumador -= 100
        Enemigos_Matados -= 100
        if Enemigos_Matados <= 0 and Sumador == 0:
            Blitea_3 = False
            Blitea_4 = True
            Activar_Animacion_Puntos_Habilidad = False
            Activar_Animacion_Tiempo = True
            frames_Tiempo = frames_totales
        if Activar_Animacion_Puntos_Habilidad:
            frames_Controladores = frames_totales
            Puntos_Totales += 100
            Puntuacion_Habilidad += 100

    if Hacer_Cuentas and aux_3:
        if Hizo_algo:
            Hizo_algo = 2500
        else:
            Hizo_algo = 0
        Total_Total = int(((Puntuacion_Corazones + (Mastil_Posicion * 4 + Cantidad_Signos * 100 + Hizo_algo) + Puntuacion_Monedas) / Segundos)*12)
        print(Total_Total)
        Restar = Puntos_Totales - Total_Total
        print(Restar)
        Restador = int((Restar/Segundos))
        print(Restador)
        aux_3 = False

    if Total_Total <= Puntos_Totales:
        Puntos_Totales -= Restador

        print(Total_Total)
        print(Puntos_Totales)
        Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)

    if Activar_Mostrar_Puntuacion_Corazones:
        ventana.blit(x_2.Palabra, (x_2.posX, x_2.posY))
        ventana.blit(Puntuacion_Corazon.Palabra, (Puntuacion_Corazon.posX, Puntuacion_Corazon.posY))

    if Activar_Mostrar_Puntuacion_Monedas:
        ventana.blit(x_3.Palabra, (x_3.posX, x_3.posY))
        ventana.blit(Puntuacion_Moneda.Palabra, (Puntuacion_Moneda.posX, Puntuacion_Moneda.posY))

    pygame.display.update()
    frames_totales += 1