import pygame
#cosntructor
class Asteroide(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenasteriode = pygame.image.load("C:/Users/Jordi/Desktop/pygame/meteoritos/imagenes/asteroide64.png")
        self.rect = self.imagenasteriode.get_rect()
        self.velocidad = 1
        self.rect.top = posy
        self.rect.left =posx
        self.listaasteroide = []
    def recorrido(self):
        self.rect.top = self.rect.top + self.velocidad
    
    def dibujar(self, superficie):
        superficie.blit(self.imagenasteriode, self.rect)
        
        