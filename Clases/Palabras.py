import pygame
class Palabra(object):

    def __init__(self, x, y, c, p, t):
        self.posX = x
        self.posY = y
        self.Color = c
        self.Tamanio_Final = t
        self.texto = p
        self.Fuente = pygame.font.SysFont("mariokartds", self.Tamanio_Final)
        self.Palabra = self.Fuente.render(self.texto, True, self.Color)

    def Aparecer(self, tamanio, Color):
        self.Fuente = pygame.font.SysFont("mariokartds", tamanio)
        self.Palabra = self.Fuente.render(self.texto, True, Color)
        self.posX -= 1