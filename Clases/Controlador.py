import pygame
from .Sprites import *

class Controlador(object):

    @classmethod
    def iniciar(cls):
        pygame.init()

    @classmethod
    def terminar(cls):
        pygame.quit()
        quit()

    @classmethod
    def configurar_pantalla(cls, ancho, alto):
        display = pygame.display.set_mode((ancho, alto)) #, pygame.FULLSCREEN
        pygame.display.set_caption("Super Poli Bros")
        return display

    @classmethod
    def iniciar_reloj(cls):
        return pygame.time.Clock()

    @classmethod
    def set_fps(cls, reloj, frames):
        reloj.tick(frames)

    @classmethod
    def rellenar_pantalla(cls, ventana, colores):
        ventana.fill(colores["Negro"])

    @classmethod
    def buscar_eventos(cls):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cls.terminar()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                cls.terminar()

    @classmethod
    def Mostrar(cls, ventana, palabra):
        print(palabra)
        ventana.blit(palabra.Palabra, (palabra.posX, palabra.posY))

    # @classmethod
    # def Pantalla_Final(cls, ventana, Titulo, Vidas, Monedas, Tiempo, Habilidad):
    #     if Titulo is not None:
    #         ventana.blit(Titulo, (50, 50))
    #     if Vidas is not None:
    #         ventana.blit(Vidas, (50, 200))
    #     if Monedas is not None:
    #         ventana.blit(Monedas, (50, 300))
    #     if Tiempo is not None:
    #         ventana.blit(Tiempo, (50, 400))
    #     if Habilidad is not None:
    #         ventana.blit(Habilidad, (50, 500))
    #     #ventana.blit(Ranking, (50, 600))
    #
    # @classmethod
    # def Regulador(cls, tamaño):
    #     fuente = pygame.font.SysFont("mariokartdsregular", tamaño)
    #     return fuente
    #
    # @classmethod
    # def Animacion_Puntuacion(cls, Nuevo_Tamaño, Colores):
    #     Fuente = Nuevo_Tamaño.render("puntuacion  final", True, Colores["Blanco"])
    #     return Fuente
    #
    # @classmethod
    # def Animacion_Vidas(cls, Nuevo_Tamaño, Colores):
    #     Vidas = Nuevo_Tamaño.render("vidas", True, Colores["Blanco"])
    #     return Vidas
    #
    # @classmethod
    # def Animacion_Monedas(cls, Nuevo_Tamaño, Colores):
    #     Monedas = Nuevo_Tamaño.render("monedas", True, Colores["Blanco"])
    #     return Monedas
    #
    # @classmethod
    # def Animacion_Tiempo(cls, Nuevo_Tamaño, Colores):
    #     Tiempo = Nuevo_Tamaño.render("tiempo", True, Colores["Blanco"])
    #     return Tiempo
    #
    # @classmethod
    # def Animacion_Habilidad(cls, Nuevo_Tamaño, Colores):
    #     habilidad = Nuevo_Tamaño.render("habilidad", True, Colores["Blanco"])
    #     return habilidad
