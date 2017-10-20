from .Base import *

class Sprite(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)

    def Animacion_Corazones(self, frames_totales, aux):
        if self.rect.x <= 800:
            self.rect.x += 8
        if frames_totales % 20 == 0 and self.ancho > 0 and self.alto > 0 and aux == 3:
            self.ancho -= 6
            self.alto -= 6
        if frames_totales % 20 == 0 and self.ancho > 0 and self.alto > 0 and aux == 2:
            self.ancho -= 6
            self.alto -= 6
        if frames_totales % 25 == 0 and self.ancho > 0 and self.alto > 0 and aux == 1:
            self.ancho -= 6
            self.alto -= 6
        if frames_totales % 25 == 0 and self.ancho > 0 and self.alto > 0 and aux == 0:
            self.ancho -= 4
            self.alto -= 4
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        if self.rect.x > 800:
            self.rect.y -= 8
            self.rect.x += 7
        if self.rect.x > 900:
            return True

    def Animacion_Monedas(self, posx, posy):
        self.rect.y -= 15
        if self.rect.y < 250:
            self.rect.x += 30
        else:
            self.rect.x += 25
        if self.rect.x > 850 and self.rect.y < 100:
            self.rect.x = posx
            self.rect.y = posy
            return True

    def Animacion_Tiempo(self):
        pass