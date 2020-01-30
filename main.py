from pygame import *
from pygame.locals import *
import sys #libreria de sistema, para que cuando cerremos el juego, cierre la ventana
from random import randint
from entities import *

init() #inicia pygame, si hubiesemos puesto import pygame, esto seria, pygame.init()

class Game:
    clock = time.Clock() #pygame.time.clock

    def __init__(self):
        self.screen = display.set_mode((800, 600)) #control de pantalla, parentesis devuelve la instancia de una ventana con el tamaño que demos, pygame.display...como arriba
        display.set_caption('Hola mundo!') #titulo, pygame.display...etc, va sin self por ser de pygame
       
        self.background_color = (150, 150, 222) #color de fondo pantalla
       
        self.player_group = sprite.Group()
        self.bombs_group = sprite.Group()
        self.all_group = sprite.Group()

        self.robot = Robot(400, 300)
        self.player_group.add(self.robot)

       
        for i in range(5):
            bomb = Bomb(randint(0 ,750), randint(0, 550))
            self.bombs_group.add(bomb)

        self.all_group.add(self.robot, self.bombs_group)
        
    def gameOver(self):
        quit()
        sys.exit()

    def handleEvents(self):
        for ev in event.get(): #pygame.event.get()
            if ev.type == QUIT: #si cierras la ventana
                self.gameOver()

            if ev.type == KEYDOWN: #si pulsamos una tecla
                if ev.key == K_UP:
                    self.robot.go_up()
                if ev.key == K_DOWN:
                    self.robot.go_down()
                if ev.key == K_LEFT:
                    self.robot.go_left()
                if ev.key == K_RIGHT:
                    self.robot.go_right()

        keys_pressed = key.get_pressed() #teclas que se mantienen pulsadas
        if keys_pressed[K_UP]:
            self.robot.go_up()
        if keys_pressed[K_DOWN]:
            self.robot.go_down()
        if keys_pressed[K_RIGHT]:
            self.robot.go_right()
        if keys_pressed[K_LEFT]:
            self.robot.go_left()

    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS) #para controlar los frames

            self.handleEvents()
            
            #Controlar si el robot toca una bomba
            if self.robot.comprobarToques(self.bombs_group) == 0: #viene del return de contador de vidas
                self.gameOver()

                #...Procesar el resto de eventos
            self.screen.fill(self.background_color) #sobre screen, le metemos el color
            
            self.all_group.update(dt)
            self.all_group.draw(self.screen) #me lo pintas en la pantalla
            display.flip() # esto coge todo lo que se ha hecho, y lo mete en la ventana

if __name__ == '__main__':
    game = Game()
    game.mainloop()