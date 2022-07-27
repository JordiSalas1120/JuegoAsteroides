from math import radians
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
colorcuadro1 = (255, 255, 0)#colores de los cuadros
colorcuadro2 = (0, 255, 255)
colortexto = (255, 255, 255)
#variables
velocidad = 8
direccion = True
posx1, posY1 = randint(1, 400), randint(1,300)#cargamos sus posiciones aleatorias
posx2, posY2 = randint(1, 400), randint(1,300)
lado = 40
cadena = "tiempo"
tamaño = 40
tipofuente = "Impact"
#preparacion de fuentes / texto
fuente = pygame.font.SysFont(tipofuente, tamaño)#declaracion de teexto y parametros de tipo de letra y tamaño
texto = fuente.render(cadena, True, colortexto)#carga texto que se mostrara
while True:
    ventana.fill(colorFondo)
    #mostrar texto
    ventana.blit(texto, (20, 20))#muestra text, la tupla es para cargar el texto y coordenadas
    #tiempo
    tiempo = pygame.time.get_ticks() / 1000 #declara al tiempo se divide por 1000 porque viene en milisegundos y al ser dividido se convierte a segundos
    cadena = "Tiempo: " + str(tiempo)
    texto = fuente.render(cadena, True, colortexto)#se convierte a string porque tiempo es entero y concartenamos

    cuadro1 = pygame.draw.rect(ventana, colorcuadro1, (posx1, posY1, lado, lado))#tamaño del obj, se declara para poder llamar desde otras partes el codigo
    cuadro2 = pygame.draw.rect(ventana, colorcuadro2, (posx2, posY2, lado, lado))
    #detecta colision
    if cuadro1.colliderect(cuadro2):#pregunta si ambos obj han colisionado
        #print(f"Colision!!! {posx1} : {posY1}")
        #cadena = (f"Colision!!! {posx1} : {posY1}")
        texto = fuente.render(cadena, True, colortexto)
        posx2, posY2 = randint(1, 400), randint(1,300)#para que cambie de pos el obj
        cuadro2.left=posx2-(lado/2) #mas como guia direccional para que el obj teng dimensiones donde moverse
        cuadro2.top=posY2-(lado/2)
    #detectar movimientos del mouse
    posx1, posY1 = pygame.mouse.get_pos()#detecta la posicionde mouse
    posx1 = posx1 - (lado / 2)#para que el obj este centrado al mouse, a la mitad de su tamaño
    posY1 = posY1 - (lado / 2)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()    
    pygame.display.update()
    