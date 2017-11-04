from Clases import *

def Final(Corazones, Cantidad_Monedas, Cantidad_Tiempo, Posicion_Mastil, Signos, Hizo_Algo, Rank):
    Controlador.iniciar()

    Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255), "Verde": (50, 205, 50),
               "Rojo": (178, 34, 34), "Naranja": (255, 165, 0), "Amarillo": (255, 215, 0),
               "Celeste": (0, 255, 255), "Azul": (0, 0, 255)}
    # (255, 0, 0)}

    Fuente_1 = 70

    Fuente_2 = 50

    ancho, alto = 1280, 720

    FPS = 120

    ventana = Controlador.configurar_pantalla(ancho, alto)

    Controlador.rellenar_pantalla(ventana, Colores)

    Puntos = Palabra(120, 50, Colores["Blanco"], "puntuacion  final", 0)
    Vidas = Palabra(100, 200, Colores["Blanco"], "vidas", 0)
    Monedas = Palabra(100, 300, Colores["Blanco"], "monedas", 0)
    Destreza = Palabra(100, 400, Colores["Blanco"], "destreza", 0)
    Tiempo = Palabra(100, 500, Colores["Blanco"], "tiempo", 0)

    Palabras = [[Puntos, False], [Vidas, False], [Monedas, False], [Destreza, False], [Tiempo, False]]

    reloj = Controlador.iniciar_reloj()

    frames_totales = 0

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

    Activar_Borrar_Todo = False

    Borrar_Todo = False

    restando = False

    termine = False

    mayor = False

    aux_e = True

    Normal_Minutos = False

    Normal_Segundos = False

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

    frames_animacion_destreza = 0

    frames_Borrar = 0

    frames_grobales = 0

    ultimos_frames = 0

    Respuesta = ""

    Dos_Puntos_1 = Sprite(660, 50, 30, 55, "Puntos.png")
    Dos_Puntos_2 = Sprite(190, 197, 25, 45, "Puntos.png")
    Dos_Puntos_3 = Sprite(250, 297, 25, 45, "Puntos.png")
    Dos_Puntos_4 = Sprite(270, 397, 25, 45, "Puntos.png")
    Dos_Puntos_5 = Sprite(210, 495, 25, 45, "Puntos.png")
    Dos_Puntos_6 = Sprite(313, 497, 25, 45, "Puntos.png")

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

    Puntos_Totales = 0

    Restador = 0
    Restar = 0
    Total_Total = 1900000000000000000

    Puntuacion_Corazones = 0
    Puntuacion_Monedas = 0
    Puntuacion_Habilidad = 0
    Puntuacion_Tiempo = 0

    M = 0

    S = 0

    Sumador = 0

    Mostrar_sumador = 0

    Contador = 0

    posx = Moneda.rect.x
    posy = Moneda.rect.y

    Total_Monedas = Cantidad_Monedas

    Mostrador_Puntos_Habilidad = Palabra(340, 395, Colores["Blanco"], str(Sumador), 60)

    Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)

    x_1 = Palabra(350, 305, Colores["Blanco"], "x", 40)
    x_2 = Palabra(238, 208, Colores["Blanco"], "x", 40)
    x_3 = Palabra(300, 308, Colores["Blanco"], "x", 40)
    x_4 = Palabra(243, 408, Colores["Blanco"], "x", 40)

    Lista_Estilos = ("malo", "bueno", "muy bueno", "excelente")

    Puntos_Habilidad = (Posicion_Mastil * 4 + Signos * 100 + Hizo_Algo)

    Ranking = Palabra(0, 250, Colores["Blanco"], str(Rank), 150)

    sumador_aux = 70

    rank = False

    estado1 = True

    posx_minutos = 280
    posx_segundos = 340

    Cero_Extra = Palabra(247, 495, Colores["Rojo"], "0", 60)
    Cero_Extra_2 = Palabra(375, 495, Colores["Rojo"], "0", 60)

    Cero_Izquierda = False
    Cero_Derecha = False
    Cero_Izquierda_Segundos = False

    while True:
        Controlador.set_fps(reloj, FPS)
        Resultado = Controlador.buscar_eventos(estado1)
        if Resultado == "Puntuacion_Total" and Activar_Borrar_Todo:
            Borrar_Todo = True
            Activar_Borrar_Todo = False
            estado1 = False
        if Resultado == "Ranking":
            print("Entre")
            rank = True
            ultimos_frames = frames_totales

        Controlador.rellenar_pantalla(ventana, Colores)
        Base.Grupo.draw(ventana)

        if not rank:
            if Activar_Mostrar_Puntos_Totales:
                ventana.blit(Puntuacion_Total.Palabra, (Puntuacion_Total.posX, Puntuacion_Total.posY))
            ventana.blit(Palabras[0][0].Palabra, (Palabras[0][0].posX, Palabras[0][0].posY))

        if not Borrar_Todo:
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

            if Cero_Izquierda:
                ventana.blit(Cero_Extra.Palabra, (Cero_Extra.posX, Cero_Extra.posY))

            if Cero_Izquierda_Segundos:
                ventana.blit(Cero_Extra_2.Palabra, (Cero_Extra_2.posX - 30, Cero_Extra_2.posY))

            if Cero_Derecha:
                ventana.blit(Cero_Extra_2.Palabra, (Cero_Extra_2.posX, Cero_Extra_2.posY))

            if Normal_Minutos:
                if M >= 10:
                    ventana.blit(Tiempo_Minutos.Palabra, (Tiempo_Minutos.posX - 17, Tiempo_Minutos.posY))
                if 0 <= M < 10:
                    ventana.blit(Tiempo_Minutos.Palabra, (Tiempo_Minutos.posX, Tiempo_Minutos.posY))

            if Normal_Segundos:
                if 0 <= S < 10:
                    Cero_Izquierda_Segundos = True
                    ventana.blit(Tiempo_Segundos.Palabra, (Tiempo_Segundos.posX + 42, Tiempo_Segundos.posY))
                if S >= 10:
                    Cero_Izquierda_Segundos = False
                    ventana.blit(Tiempo_Segundos.Palabra, (Tiempo_Segundos.posX + 2, Tiempo_Segundos.posY))

            if Blitea:
                ventana.blit(x_1.Palabra, (x_1.posX, x_1.posY))
                ventana.blit(Numero.Palabra, (Numero.posX, Numero.posY))

            if Blitea_3:
                ventana.blit(Mostrador_Puntos_Habilidad.Palabra,
                             (Mostrador_Puntos_Habilidad.posX, Mostrador_Puntos_Habilidad.posY))

            if Blitea_4:
                if Mostrar_sumador < 800:
                    Mostrador_Puntos_Habilidad = Palabra(310, 395, Colores["Naranja"], Lista_Estilos[0], 60)
                elif 800 <= Mostrar_sumador < 1200:
                    Mostrador_Puntos_Habilidad = Palabra(310, 395, Colores["Celeste"], Lista_Estilos[1], 60)
                elif 1200 <= Mostrar_sumador < 1600:
                    Mostrador_Puntos_Habilidad = Palabra(310, 395, Colores["Azul"], Lista_Estilos[2], 60)
                elif Mostrar_sumador >= 1600:
                    Mostrador_Puntos_Habilidad = Palabra(310, 395, Colores["Verde"], Lista_Estilos[3], 60)
                ventana.blit(Mostrador_Puntos_Habilidad.Palabra,
                             (Mostrador_Puntos_Habilidad.posX, Mostrador_Puntos_Habilidad.posY))

            if Activar_Mostrar_Puntuacion_Corazones:
                ventana.blit(x_2.Palabra, (x_2.posX, x_2.posY))
                ventana.blit(Puntuacion_Corazon.Palabra, (Puntuacion_Corazon.posX, Puntuacion_Corazon.posY))

            if Activar_Mostrar_Puntuacion_Monedas:
                ventana.blit(x_3.Palabra, (x_3.posX, x_3.posY))
                ventana.blit(Puntuacion_Moneda.Palabra, (Puntuacion_Moneda.posX, Puntuacion_Moneda.posY))

        if Borrar_Todo:
            for sprite in Base.Grupo:
                Base.Grupo.remove(sprite)
            if sumador_aux <= 100:
                Palabras[0][0].Aparecer(sumador_aux, Colores["Blanco"])
                Palabras[0][0].posX += 5
                Puntuacion_Total.Aparecer(sumador_aux, Colores["Blanco"])
                Puntuacion_Total.posX -= 8
                Puntuacion_Total.posY += 8
                sumador_aux += 1

        if rank:
            if ultimos_frames + 100 > frames_totales:
                Controlador.Rankeador(Colores, ventana)
            if ultimos_frames + 100 < frames_totales:
                Controlador.Ranking(Ranking, Rank, Colores, ventana)

        if Activar_Mostrar_Corazones and Corazones > 0 and frames_mostrar_Corazones + 50 < frames_totales and frames_cantidad_Corazones + 50 < frames_totales:
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
            frames_animacion_Monedas = frames_totales
            Respuesta = False

        if Activar_Preparar_Monedas:
            Activar_Preparar_Monedas = False
            Mostrar_Monedas = True

        if Mostrar_Monedas and frames_cantidad_Monedas + 50 < frames_totales and frames_tardar_mostrar + 15 < frames_totales:
            frames_tardar_mostrar = frames_totales
            Base.Grupo.add(Moneda_1)
            Blitea = True
            Numero = Palabra(390, 295, Colores["Verde"], str(Mostrador), 60)
            if Mostrador != Total_Monedas + 1:
                Mostrador += 1
            if Total_Monedas + 1 == Mostrador:
                Mostrar_Monedas = False
                Activar_Mostrar_Puntos_Habilidad = True

        if Activar_Animacion_Monedas and Total_Monedas >= 0 and frames_animacion_Monedas + 50 < frames_totales:
            if Base.Grupo.has(Moneda):
                if Moneda.Animacion_Monedas(posx, posy):
                    Mostrador -= 1
                    Puntuacion_Monedas += 200
                    Puntos_Totales += 200
                    Numero = Palabra(390, 295, Colores["Verde"], str(Mostrador), 60)
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

        if Activar_Mostrar_Tiempo and frames_Tiempo + 20 < frames_totales:
            if S == 60:
                M += 1
                S -= 60
            if M >= 10:
                Cero_Izquierda = False
                Normal_Minutos = True
            if 0 <= M < 10:
                Normal_Minutos = False
                Cero_Izquierda = True
            if S + (M * 60) == Cantidad_Tiempo:
                if 0 <= S < 10:
                    Cero_Izquierda_Segundos = True
                if M < 10:
                    Cero_Izquierda = True
                Activar_Mostrar_Tiempo = False
                Activar_Animacion_Corazones = True
            Normal_Minutos = True
            Normal_Segundos = True
            Tiempo_Segundos = Palabra(340, 495, Colores["Rojo"], str(S), 60)
            Tiempo_Minutos = Palabra(280, 495, Colores["Rojo"], str(M), 60)
            S += 1
            Base.Grupo.add(Dos_Puntos_6)

        if Activar_Animacion_Tiempo and frames_Tiempo + 70 < frames_totales:
            if M == 0:
                termine = True
            if 0 <= M < 10:
                Cero_Izquierda = True

            if termine and S == 0:
                S = 0
                Cero_Izquierda_Segundos = True
                Activar_Animacion_Tiempo = False
                Activar_Borrar_Todo = True
                frames_Borrar = frames_totales
            if S == 0 and not termine:
                M -= 1
                S = 60
            if Activar_Animacion_Tiempo:
                S -= 1
                Hacer_Cuentas = True
            if 0 < S < 10:
                Cero_Izquierda_Segundos = True
            if S >= 10:
                Cero_Izquierda_Segundos = False
            Tiempo_Segundos = Palabra(340, 495, Colores["Rojo"], str(S), 60)
            Tiempo_Minutos = Palabra(280, 495, Colores["Rojo"], str(M), 60)

        if Activar_Mostrar_Puntos_Habilidad and frames_Controladores + 10 < frames_totales and frames_mostrar_Puntos_Habilidad + 10 < frames_totales:
            frames_mostrar_Puntos_Habilidad = frames_totales
            if Sumador >= Puntos_Habilidad:
                Mostrar_sumador = Sumador
                Activar_Mostrar_Tiempo = True
                Activar_Mostrar_Puntos_Habilidad = False
            Blitea_3 = True
            Mostrador_Puntos_Habilidad = Palabra(310, 395, Colores["Verde"], str(Sumador), 60)
            Sumador += 100

        if Activar_Animacion_Puntos_Habilidad and frames_Controladores + 20 < frames_totales and frames_animacion_destreza + 10 < frames_totales:
            Mostrador_Puntos_Habilidad = Palabra(310, 395, Colores["Verde"], str(Sumador), 60)
            Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)
            Sumador -= 100
            if Sumador == 0:
                Blitea_3 = False
                Blitea_4 = True
                Activar_Animacion_Puntos_Habilidad = False
                Activar_Animacion_Tiempo = True
                frames_Tiempo = frames_totales
            if Activar_Animacion_Puntos_Habilidad:
                frames_animacion_destreza = frames_totales
                Puntos_Totales += 100
                Puntuacion_Habilidad += 100

        if Hacer_Cuentas and aux_3:
            if Hizo_Algo:
                Hizo_Algo = 2500
            else:
                Hizo_Algo = 0
            Total_Total = int(
                ((Puntuacion_Corazones + (Puntuacion_Habilidad + Hizo_Algo) + Puntuacion_Monedas) / Cantidad_Tiempo) * 100)
            Restar = Puntos_Totales - Total_Total
            Restador = int((Restar / Cantidad_Tiempo))
            aux_3 = False

        if Total_Total <= Puntos_Totales:
            Puntos_Totales -= Restador
            Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)

        pygame.display.update()
        frames_totales += 1