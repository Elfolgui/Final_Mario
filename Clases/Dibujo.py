from .Controlador import *
from .Base import *

def dibujo(ventana, colores, Total, Vidas, Monedas, Tiempo, Habilidad):

    Controlador.rellenar_pantalla(ventana, colores)
    Controlador.Pantalla_Final(ventana, Total, Vidas, Monedas, Tiempo, Habilidad)
    Base.Grupo.draw(ventana)
    pygame.display.flip()