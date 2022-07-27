import pygame


class misil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenmisil = pygame.image.load("meteoritos/imagenes/proyectil.png.")
        self.rect = self.imagenmisil.get_rect()#crea rectangulo donde esta el objeto
        self.velocidaddisparo = 1
        self.rect.top = posy
        self.rect.left = posx
    def  recorrido(self):
        self.rect.top = self.rect.top - self.velocidaddisparo   #se le resta para que el misil inicie a subir posy
    def dibujar(self, superficie):
        superficie.blit(self.imagenmisil, self.rect)
