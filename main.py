from pygame import *
from pygame.locals import *
import sys #libreria de sistema, para que cuando cerremos el juego, cierre la ventana
from random import randint

init() #inicia pygame, si hubiesemos puesto import pygame, esto seria, pygame.init()
FPS = 60
class Bomb:
    pictures = ['bomb_01.png', 'bomb_02.png','bomb_03.png','bomb_04.png']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        self.frames = [] #con esto tenemos ya las imagenes, no las rutas a las imagenes
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
       #ésto es como lo de arriba ---> self.frames = [image.load('resources/{}'.format(pict)).convert_alpha() for pict in self.pictures]

        self.frame_act = 0
        self.num_frames = len(self.frames)

        self.current_time = 0 #tiempo actual
        self.animation_time = FPS//444 #fraccion de las FPS

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time: #si el tiempo transcurrido desde que llamas a la funcion, osea que se inicia, es mayor que el animation_time, animas las bombas
            self.current_time = 0
            self.frame_act +=1
            if self.frame_act == self.num_frames:
                self.frame_act = 0
            #ésto es lo mismo que de arriba ---> self.frame_act = (self.frame_act + 1) % self.num_frames

    @property #ahora es un propiedad, no un método, como image
    def position(self):
        return self.x, self.y #esto lo devuelve en forma de tupla (x, y)

    @property
    def image(self):
        return self.frames[self.frame_act]



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



class Game:
    clock = time.Clock() #pygame.time.clock

    def __init__(self):
       self.screen = display.set_mode((800, 600)) #control de pantalla, parentesis devuelve la instancia de una ventana con el tamaño que demos, pygame.display...como arriba
       display.set_caption('Hola mundo!') #titulo, pygame.display...etc, va sin self por ser de pygame
       
       self.background_color = (150, 150, 222) #color de fondo pantalla

       self.robot = Robot(400, 300)

       self.bombas = []
       for i in range(5):
          self.bomb = Bomb(randint(0 ,750), randint(0, 550))
          self.bombas.append(self.bomb)

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
            
                #...Procesar el resto de eventos
            self.screen.fill(self.background_color) #sobre screen, le metemos el color
            self.screen.blit(self.robot.image, self.robot.position) #pones esa imagen donde te digo, ya no hace falta poner robot.position() al poner arriba @property
            for b in self.bombas:
                b.update(dt)
                self.screen.blit(b.image, b.position)

            display.flip() # esto coge todo lo que se ha hecho, y lo mete en la ventana

if __name__ == '__main__':
    game = Game()
    game.mainloop()