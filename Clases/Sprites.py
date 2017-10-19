from .Base import *

class Sprite(Base):

    def __init__(self, x, y, ancho, alto, ruta):
        Base.__init__(self, x, y, ancho, alto, ruta)

    def Animacion(self, frames_totales):
        self.rect.x += 4
        if frames_totales % 5 == 0:
            self.ancho -= 2
            self.alto -= 2
            if self.ancho < 0 and self.alto < 0:
                return "Llegue"
        self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
        if self.rect.x > 700:
            self.rect.y -= 4