import pygame
import sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Titulo de la ventana")
#colores
colorFondo = (1, 150, 70)
colorLiena = (255, 128, 0)
colorCirculo = (255,255,0)
colorFiguras = (255,0,155)
while True:
    ventana.fill(colorFondo) #dibuja el color del fondo
    #lineas
    pygame.draw.line(ventana,colorLiena,(60, 90), (200, 100), 40) #para dibujar la linea los valores son las coordenadas x,y y grosor de la linea
    pygame.draw.line(ventana,colorLiena,(80, 190), (100, 150), 20) #para dibujar la linea los valores son las coordenadas x,y y grosor de la linea
    pygame.draw.line(ventana,colorLiena,(40, 30), (250, 190), 10) #para dibujar la linea los valores son las coordenadas x,y y grosor de la linea

    #circulos
    pygame.draw.circle(ventana, colorCirculo, (400,100), 100, 30)#dibuja circulo(coordenadas,radio y ancho)
    pygame.draw.circle(ventana, colorCirculo, (590,250), 50, 20)

    #figuras
    pygame.draw.rect(ventana, colorFiguras, (100, 200, 120, 250))#dibuja el rectangulo(coordenadas)
    pygame.draw.polygon(ventana, colorFiguras, ((400,400), 
                        (500, 400), (550, 500), (490, 500)))#dibuja el poligono(coordenadas que indica los puntos donde dibujar el poligono)

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()