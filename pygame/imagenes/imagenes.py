import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Carga imagen y posicion al azar")
colorFondo = (1, 150, 70)
colorRectangulo = (255, 60, 40)#declaracion de colores
#posicion de la imagen
posX, posY = (10, 40)
#cargar imagen
imagen = pygame.image.load("imagenes/icon.png")#carga de imagen antes de ciclo
while True:
    ventana.fill(colorFondo)
    ventana.blit(imagen, (posX, posY))
    for i in range(15):
        posX2, posY2 = randint(1, 500), randint(1, 300)
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)#declaracion de colores aleatorios
        colorRectangulo = (r, g, b)
        pygame.draw.rect(ventana, colorRectangulo, (posX2, posY2, 50, 80))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()