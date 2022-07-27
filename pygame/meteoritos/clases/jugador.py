import pygame
from clases import disparo
#from meteoritos.clases.disparo import misil
class nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)#con self se refiera a la misma clase ya que s un parametro especial al cual no se le da valor mas que referencia
        self.imagennave = pygame.image.load("meteoritos/imagenes/nave.png")
        self.imagenexplota = pygame.image.load("meteoritos/imagenes/explosion2.png")

        # tomamos rectangulo imagen
        self.rect = self.imagennave.get_rect()
        #pos inicial de la nave
        self.rect.centerx = 240
        self.rect.centery = 650
        self.velocidad = 15
        self.vida = True
        self.listdisparo = []
        self.sonidodisparo = pygame.mixer.Sound("meteoritos/sonidos/disparo.aiff")
    def mover(self): #asi comprobamos que la nav no se sale de la oantalla
        if self.vida == True: #obvio, si no hay vda para que hacerlo xD
            if self.rect.left <= 0: #verificamos que no salga la nave por los lados
                self.rect.left=0
            elif self.rect.right > 490:
                self.rect.right = 490
    def disparar(self, x, y):
        #print("Estoy disparando")
        if self.vida == True:
             misilj = disparo.misil(x, y)
             self.listdisparo.append(misilj) #agregamos elementos a la lista
             self.sonidodisparo.play()
    def dibujar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagennave, self.rect)
        else:
            superficie.blit(self.imagenexplota, self.rect)
