from operator import truediv
import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Titulo de la ventana")
colorFondo = (1, 150, 70)
colorFigura = (255, 255, 255)
#variables
velocidad = 0.1
direccion = True
posx, posY = randint(1, 400), randint(1,300)

while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana, colorFigura, (posx, posY, 40, 40))
    #movimiento
    if direccion == True:
        if posx < (500-40):
            posx += velocidad
        else:
            direccion = False
    else: 
        if posx > 1:
            posx -= velocidad
        else:
            direccion = True
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()