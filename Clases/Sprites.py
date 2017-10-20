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

    def Animacion_Monedas(self, frames_totales, posx, posy, ancho, alto):
        if frames_totales % 5 == 0 and self.ancho > 0 and self.alto > 0:
            self.ancho -= 3
            self.alto -= 3
            if self.ancho <= 0 and self.alto <= 0:
                return True
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        self.rect.y -= 10
        if self.rect.y < 250:
            self.rect.x += 25
        else:
            self.rect.x += 15
        if self.rect.x > 700 and self.rect.y < 100:
            self.rect.x = posx
            self.rect.y = posy
            self.ancho = ancho
            self.alto = alto
            self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
            return "Llegue"