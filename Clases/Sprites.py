from .Base import *

class Sprite(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)

    def Animacion_Corazones(self, frames_totales):
        if self.rect.x <= 800:
            self.rect.x += 4
        if frames_totales % 5 == 0 and self.ancho > 0 and self.alto > 0:
            self.ancho -= 1
            self.alto -= 1
            if self.ancho <= 0 and self.alto <= 0:
                return True
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        if self.rect.x > 800:
            self.rect.y -= 4
            self.rect.x += 3

    def Animacion_Monedas(self, frames_totales):
        if frames_totales % 5 == 0 and self.ancho > 0 and self.alto > 0:
            self.ancho -= 1
            self.alto -= 1
            if self.ancho <= 0 and self.alto <= 0:
                return True
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        self.rect.y -= 10
        self.rect.x += 10