from operator import truediv
import pygame
import sys
from pygame import event
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Movimientos teclas")
colorFondo = (1, 150, 70)
colorFigura = (255, 255, 255)
#variables
velocidad = 8
direccion = True
posx, posY = randint(1, 400), randint(1,300)
lado = 40
while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana, colorFigura, (posx, posY, lado, lado))#tamaño del obj
    #detectar movimientos del mouse
    posx, posY = pygame.mouse.get_pos()#detecta la posicionde mouse
    posx = posx - (lado / 2)#para que el obj este centrado al mouse, a la mitad de su tamaño
    posY = posY - (lado / 2)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()    
    pygame.display.update()
    pygame.display.update()