from .Controlador import *
from .Base import *

def dibujo(ventana, colores, Palabras):

    Controlador.rellenar_pantalla(ventana, colores)
    ventana.blit(Palabras[0].Palabra, (Palabras[0].posX, Palabras[0].posY))
    Base.Grupo.draw(ventana)
    pygame.display.update()