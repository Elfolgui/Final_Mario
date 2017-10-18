from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255)}

Fuente_1 = 70

Fuente_2 = 50

ancho, alto = 1280, 720

FPS = 120

ventana = Controlador.configurar_pantalla(ancho, alto)

Controlador.rellenar_pantalla(ventana, Colores)

Puntos = Palabra(50, 50, Colores["Blanco"], "puntuacion  final", 0)
Vidas = Palabra(50, 150, Colores["Blanco"], "vidas", 0)
Monedas = Palabra(50, 250, Colores["Blanco"], "Monedas", 0)
Tiempo = Palabra(50, 350, Colores["Blanco"], "tiempo", 0)

Palabras = [Puntos, Vidas, Monedas, Tiempo]

reloj = Controlador.iniciar_reloj()

frames_totales = 0

tamaño = 50

Corazon = Sprite(200, 250, 40, 40, "Corazon.png")
Corazon_2 = Sprite(250, 250, 40, 40, "Corazon.png")
Corazon_3 = Sprite(300, 250, 40, 40, "Corazon.png")
Moneda_1 = Sprite(300, 350, 40, 40, "Moneda_1.png")

posicion = 0

while True:
    # Total = Controlador.Animacion_Puntuacion(Controlador.Regulador(tamaño), Colores)
    # Vidas = Controlador.Animacion_Vidas(Controlador.Regulador(tamaño), Colores)
    # Monedas = Controlador.Animacion_Monedas(Controlador.Regulador(tamaño), Colores)
    # Tiempo = Controlador.Animacion_Tiempo(Controlador.Regulador(tamaño), Colores)
    # Habilidad = Controlador.Animacion_Habilidad(Controlador.Regulador(tamaño), Colores)
    Palabras[posicion].Animacion(frames_totales)
    dibujo(ventana, Colores, Palabras)
    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()
    Controlador.set_fps(reloj, FPS)
    frames_totales += 1
