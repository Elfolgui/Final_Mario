import pygame
from .Sprites import *
from .Fin import *
from .Palabras import *
import random

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
        display = pygame.display.set_mode((ancho, alto))#, pygame.FULLSCREEN) #
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
    def Rankeador(cls, Colores, ventana):
        Ranking = Palabra(460, 100, Colores["Amarillo"], "ranking", 90)
        N_R = random.randrange(0, 9)
        N_R_1 = random.randrange(0, 9)
        N_R_2 = random.randrange(0, 9)
        N_R_3 = random.randrange(0, 9)
        N_R_4 = random.randrange(0, 9)
        N_R_5 = random.randrange(0, 9)
        N1 = Palabra(390, 250, Colores["Blanco"], str(N_R), 150)
        N2 = Palabra(470, 250, Colores["Blanco"], str(N_R_1), 150)
        N3 = Palabra(550, 250, Colores["Blanco"], str(N_R_2), 150)
        N4 = Palabra(630, 250, Colores["Blanco"], str(N_R_3), 150)
        N5 = Palabra(710, 250, Colores["Blanco"], str(N_R_4), 150)
        N6 = Palabra(790, 250, Colores["Blanco"], str(N_R_5), 150)
        ventana.blit(N1.Palabra, (N1.posX, N1.posY))
        ventana.blit(N2.Palabra, (N2.posX, N2.posY))
        ventana.blit(N3.Palabra, (N3.posX, N3.posY))
        ventana.blit(N4.Palabra, (N4.posX, N4.posY))
        ventana.blit(N5.Palabra, (N5.posX, N5.posY))
        ventana.blit(N6.Palabra, (N6.posX, N6.posY))
        ventana.blit(Ranking.Palabra, (Ranking.posX, Ranking.posY))