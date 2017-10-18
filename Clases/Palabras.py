import pygame
class Palabra(object):

    def __init__(self, x, y, c, p, t):
        self.posX = x
        self.posY = y
        self.Color = c
        self.Tamanio_Final = t
        self.Fuente = pygame.font.SysFont("mariokartdsregular", self.Tamanio_Final)
        self.Palabra = self.Fuente.render(p, True, self.Color)

    def Animacion(self, tamanio):
        self.Fuente = pygame.font.SysFont("mariokartdsregular", tamanio)