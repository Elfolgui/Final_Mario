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
    def Pantalla_Final(cls, ventana, Titulo, Vidas, Monedas, Tiempo, Habilidad):
        print("Entre")
        ventana.blit(Titulo, (50, 50))
        ventana.blit(Vidas, (50, 250))
        ventana.blit(Monedas, (50, 350))
        ventana.blit(Tiempo, (50, 450))
        ventana.blit(Habilidad, (50, 550))
        #ventana.blit(Ranking, (50, 600))

    @classmethod
    def Creador(cls, Colores):
        #--------------FUENTES-------------------------
        Puntuacion_Fuente = pygame.font.SysFont("mariokartdsregular", 70)
        font = pygame.font.SysFont("mariokartdsregular", 50)
        Total = Puntuacion_Fuente.render("puntuacion final", True, Colores["Blanco"])
        Vidas = font.render("vidas", True, Colores["Blanco"])
        Monedas = font.render("monedas", True, Colores["Blanco"])
        Tiempo = font.render("tiempo", True, Colores["Blanco"])
        Habilidad = font.render("habilidad", True, Colores["Blanco"])
        # Ranking = font.render("ranking", True, Colores["Blanco"])
        Lista_Puntajes = ["puntuacion final", "vidas", "monedas", "tiempo"]

        #-------------SPRITES--------------------------

        Corazon = Sprite(200, 250, 40, 40, "Corazon.png")
        Corazon_2 = Sprite(250, 250, 40, 40, "Corazon.png")
        Moneda_1 = Sprite(300, 350, 40, 40, "Moneda_1.png")

        return Total, Vidas, Monedas, Tiempo, Habilidad