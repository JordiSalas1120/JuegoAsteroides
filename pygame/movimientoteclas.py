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

while True:
    ventana.fill(colorFondo)
    pygame.draw.rect(ventana, colorFigura, (posx, posY, 40, 40))#tamaño del obj
    #
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        #detectar pulsaciones de teclas
        elif evento.type == pygame.KEYDOWN:
            if evento.key == K_LEFT:#si se presiona izq se resta en x
                posx -= velocidad
                if posx<0:#evita que el objeto salga de la pantalla
                    posx=0  
            elif evento.key == K_RIGHT:#si se presiona derecha, x aumenta
                posx += velocidad  
                if posx > (500-40):#evita que obj salha de la pantalla por la  derecha se le resta el tamaño del obj
                    posx = 500-40
            elif evento.key == K_UP:#Para arriba y aumenta
                posY -= velocidad
                if posY < 0:
                    posY=0
            elif evento.key == K_DOWN:#hacia abajo disminuye y
                posY += velocidad
                if posY>(400-40):#evita que el obj salga de la pantalla de anajo
                    posY=(400-40) 

            
    pygame.display.update()
    pygame.display.update()