from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255)}

Total, Vidas, Monedas, Tiempo, Habilidad = Controlador.Creador(Colores) #Ranking

ancho, alto = 1280, 720

FPS = 120

ventana = Controlador.configurar_pantalla(ancho, alto)

Controlador.rellenar_pantalla(ventana, Colores)

reloj = Controlador.iniciar_reloj()


while True:

    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()
    Controlador.Pantalla_Final(ventana, Total, Vidas, Monedas, Tiempo, Habilidad)
    dibujo(ventana, Colores, Total, Vidas, Monedas, Tiempo, Habilidad)
    Controlador.set_fps(reloj, FPS)