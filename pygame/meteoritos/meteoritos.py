import time
import pygame
import sys
from pygame.locals import *
from pygame.sprite import collide_rect

#importamos las clases
from clases import jugador
from clases import disparo
from clases import asteroide
from random import randint
from time import process_time
#variables
ancho = 480
largo =  700
listaateroide = [] 
puntos = 0
colorfuentes = (120, 200, 40)
#booleano juego
jugando = True

# crea objeto jugador


#funcion principal
#cargas asteroides
def cargarasteroides(x, y):
    meteoro = asteroide.Asteroide(x, y)
    listaateroide.append(meteoro)
def gameover():
    global jugando
    jugando = False
    for meteoritos in listaateroide:
        listaateroide.remove(meteoritos)
def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ancho, largo))
    
    #imagen de fondo
    fondo = pygame.image.load("meteoritos/imagenes/fondo.jpg")
    
    #titulo
    pygame.display.set_caption("Meteoritos")

    # crear objeto jugador
    nave = jugador.nave()
    contador = 0
    #sonidos
    pygame.mixer.music.load("meteoritos/sonidos/fondo.wav")
    pygame.mixer.music.play(8)
    sonidocolision = pygame.mixer.Sound("meteoritos/sonidos/colision.aiff")

    #fuente marcador
    fuentemarcador = pygame.font.SysFont('Arial', 20)
    #ciclo del juego
    #variable de puntos, aqui porque no me daba al inicio
    puntos = 0
    while True:

        ventana.blit(fondo,(0,0))
        nave.dibujar(ventana) # cargamos la nave en la ventana
        #tiempo 
        tiempo = time.process_time()
        # marcador
        
        textomarcador = fuentemarcador.render("Puntos:" + str(puntos), 0, colorfuentes)
        ventana.blit(textomarcador, (0,0))
        #creamos asteroides
        if tiempo - contador > 1:
            contador = tiempo
            posx = randint(2, 480) 
            cargarasteroides(posx, 0)
        #comprobamos lista de asteroides 
        if len(listaateroide) > 0:
            for x in listaateroide:
                if jugando == True:
                    x.dibujar(ventana)
                    x.recorrido()
                if x.rect.top > 700:
                    listaateroide.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        listaateroide.remove(x)
                        sonidocolision.play()
                        #print("colision nave /meteorito")
                        nave.vida = False
                        gameover()

        # disparo de misil
        if len(nave.listdisparo)>0:
            for x in nave.listdisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top <= 10:
                    nave.listdisparo.remove(x)
                else:
                    for meteoritos in listaateroide:
                        if x.rect.colliderect(meteoritos.rect):
                            listaateroide.remove(meteoritos)
                            nave.listdisparo.remove(x)
                            puntos += 1                            
                            #print("colision disparo / meteoro")
        nave.mover() #para controlar que la nave no se salga de la ventana

        #cuandoc comprobemos final del juego
        #pygame.mixer.music.fadeout(3000)

        for evento in pygame.event.get():#verifica la x de la centana
            if evento.type == QUIT:#verifica si se le da clic para 
                pygame.quit()
                sys.exit
            elif evento.type == pygame.KEYDOWN:# dentro de los eventos verificar que teclas estamos pulsando
                if jugando == True:
                    if evento.key == K_LEFT:
                        nave.rect.left-=nave.velocidad
                    elif evento.key == K_RIGHT:
                        nave.rect.right+=nave.velocidad
                    elif evento.key ==  K_SPACE:
                        x, y = nave.rect.center #comprobamos su pos para paserlos a la nave
                        nave.disparar(x, y)
        if jugando == False:
            fuentegameover = pygame.font.SysFont("Arial", 40)
            textogameover = fuentegameover.render("Game Over", 0, colorfuentes)
            ventana.blit(textogameover, (140, 350))
            pygame.mixer.music.fadeout(3000)
        pygame.display.update()#actualiza la ventana
# llamada a funcion principal
meteoritos()
