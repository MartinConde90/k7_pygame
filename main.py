from pygame import *
from pygame.locals import *
import sys #libreria de sistema, para que cuando cerremos el juego, cierre la ventana

init() #inicia pygame, si hubiesemos puesto import pygame, esto seria, pygame.init()

screen = display.set_mode((800, 600)) #control de pantalla, parentesis devuelve la instancia de una ventana con el tamaño que demos, pygame.display...como arriba
display.set_caption('Hola mundo!') #titulo, pygame.display...etc
background_color = (30, 46, 222) #color de fondo pantalla

while True:

    for ev in event.get(): #pygame.event.get()
        if ev.type == QUIT: #si cierras la ventana
             quit()
             sys.exit()
    
        #...Procesar el resto de eventos
        screen.fill(background_color) #sobre screen, le metemos el color

        display.flip() # esto coge todo lo que se ha hecho, y lo mete en la ventana
