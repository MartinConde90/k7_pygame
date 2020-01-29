from pygame import *
from pygame.locals import *
import sys #libreria de sistema, para que cuando cerremos el juego, cierre la ventana

init() #inicia pygame, si hubiesemos puesto import pygame, esto seria, pygame.init()

class Robot:
    speed = 5
    images = ['robot_r01.png, robot_r02.png, robot_r03.png, robot_r04.png,']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image.load('resources/robot_r01.png').convert_alpha()
    
    def go_up(self): #arriba
        '''
        if self.y > 0: #si 'y' es mayor que 0
            self.y -= self.speed #restas para que suba
        '''
        self.y = max(0, self.y - self.speed) #self.y es el maximo entre 0 y self.y - movimiento, si es 100, pues 95 ya que speed es 5, si es cero, pues 0 ,ya que entre 0 y -5 el max es 0
                                        
    def go_down(self):
        self.y = min(600, self.y + self.speed)
    
    def go_right(self):
        self.x = min(800, self.x + self.speed)

    def go_left(self):
        self.x = max(0, self.x - self.speed)
    
    def position(self):
        return self.x, self.y #esto lo devuelve en forma de tupla (x, y)

screen = display.set_mode((800, 600)) #control de pantalla, parentesis devuelve la instancia de una ventana con el tamaño que demos, pygame.display...como arriba
display.set_caption('Hola mundo!') #titulo, pygame.display...etc
background_color = (150, 150, 222) #color de fondo pantalla

robot = Robot(400, 300)

while True:

    for ev in event.get(): #pygame.event.get()
        if ev.type == QUIT: #si cierras la ventana
             quit()
             sys.exit()

        if ev.type == KEYDOWN: #si pulsamos una tecla
            if ev.key == K_UP:
                robot.go_up()
            if ev.key == K_DOWN:
                robot.go_down()
            if ev.key == K_LEFT:
                robot.go_left()
            if ev.key == K_RIGHT:
                robot.go_right()

    keys_pressed = key.get_pressed() #teclas que se mantienen pulsadas
    if keys_pressed[K_UP]:
        robot.go_up()
    if keys_pressed[K_DOWN]:
        robot.go_down()
    if keys_pressed[K_RIGHT]:
        robot.go_right()
    if keys_pressed[K_LEFT]:
        robot.go_left()
    
        


        #...Procesar el resto de eventos
    screen.fill(background_color) #sobre screen, le metemos el color
    screen.blit(robot.image, (robot.position())) #pones esa imagen donde te digo

    display.flip() # esto coge todo lo que se ha hecho, y lo mete en la ventana
