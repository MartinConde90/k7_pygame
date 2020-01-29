from pygame import *
from pygame.locals import *
import sys #libreria de sistema, para que cuando cerremos el juego, cierre la ventana

init() #inicia pygame, si hubiesemos puesto import pygame, esto seria, pygame.init()


class Robot:
    speed = 5
    pictures = ['robot_r01.png', 'robot_r02.png', 'robot_r03.png', 'robot_r04.png']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.frames = [] #con esto tenemos ya las imagenes, no las rutas a las imagenes
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
       #ésto es como lo de arriba ---> self.frames = [image.load('resources/{}'.format(pict)).convert_alpha() for pict in self.pictures]

        self.frame_act = 0 #disfraz activo, el 0 es posicion de quieto
        self.num_frames = len(self.frames) #numero de disfraz
    
    def change_frame(self):
        self.frame_act +=1
        if self.frame_act == self.num_frames:
            self.frame_act = 0
        #ésto es lo mismo que de arriba ---> self.frame_act = (self.frame_act + 1) % self.num_frames

    def go_up(self): #arriba
        '''
        if self.y > 0: #si 'y' es mayor que 0
            self.y -= self.speed #restas para que suba
        '''
        self.y = max(0, self.y - self.speed) #self.y es el maximo entre 0 y self.y - movimiento, si es 100, pues 95 ya que speed es 5, si es cero, pues 0 ,ya que entre 0 y -5 el max es 0
        self.change_frame()   

    def go_down(self):
        self.y = min(600, self.y + self.speed)
        self.change_frame()

    def go_right(self):
        self.x = min(800, self.x + self.speed)
        self.change_frame()

    def go_left(self):
        self.x = max(0, self.x - self.speed)
        self.change_frame()

    @property #ahora es un propiedad, no un método, como image
    def position(self):
        return self.x, self.y #esto lo devuelve en forma de tupla (x, y)

    @property
    def image(self):
        return self.frames[self.frame_act]

screen = display.set_mode((800, 600)) #control de pantalla, parentesis devuelve la instancia de una ventana con el tamaño que demos, pygame.display...como arriba
display.set_caption('Hola mundo!') #titulo, pygame.display...etc
clock = time.Clock() #pygame.time.clock

background_color = (150, 150, 222) #color de fondo pantalla

robot = Robot(400, 300)

while True:
    clock.tick(60) #para controlar los frames

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
    screen.blit(robot.image, robot.position) #pones esa imagen donde te digo, ya no hace falta poner robot.position() al poner arriba @property

    display.flip() # esto coge todo lo que se ha hecho, y lo mete en la ventana
