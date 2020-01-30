from pygame import *
from pygame.locals import *
from random import randint
FPS = 60

class Bomb(sprite.Sprite):
    pictures = ['bomb_01.png', 'bomb_02.png','bomb_03.png','bomb_04.png']
    w = 44
    h = 42

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        sprite.Sprite.__init__(self) #constructor de quien heredamos para que asi tengamos todos los metodos y cuestiones

        self.rect = Rect(self.x, self.y, self.w, self.h) #pygame.Rect

        self.frames = [] #con esto tenemos ya las imagenes, no las rutas a las imagenes
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
       #ésto es como lo de arriba ---> self.frames = [image.load('resources/{}'.format(pict)).convert_alpha() for pict in self.pictures]

        self.frame_act = 0
        self.num_frames = len(self.frames)

        self.current_time = 0 #tiempo actual
        self.animation_time = FPS + 150 #fraccion de las FPS

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time: #si el tiempo transcurrido desde que llamas a la funcion, osea que se inicia, es mayor que el animation_time, animas las bombas
            self.current_time = 0
            self.frame_act +=1
            if self.frame_act == self.num_frames:
                self.frame_act = 0
            #ésto es lo mismo que de arriba ---> self.frame_act = (self.frame_act + 1) % self.num_frames

    @property #ahora es un propiedad, no un método, como image
    def image(self):
        return self.frames[self.frame_act]

class Robot(sprite.Sprite):
    speed = 5
    pictures = ['robot_r01.png', 'robot_r02.png', 'robot_r03.png', 'robot_r04.png']
    w = 64 #altura robot, lo pone en la imagen
    h = 68 #ancho robot
    lives = 3

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        sprite.Sprite.__init__(self)

        self.rect = Rect(self.x, self.y, self.w, self.h)

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
        self.rect.y = max(0, self.rect.y - self.speed) #self.y es el maximo entre 0 y self.y - movimiento, si es 100, pues 95 ya que speed es 5, si es cero, pues 0 ,ya que entre 0 y -5 el max es 0
        self.change_frame()   

    def go_down(self):
        self.rect.y = min(600, self.rect.y + self.speed)
        self.change_frame()

    def go_right(self):
        self.rect.x = min(800, self.rect.x + self.speed)
        self.change_frame()

    def go_left(self):
        self.rect.x = max(0, self.rect.x - self.speed)
        self.change_frame()

    def comprobarToques(self, group):
        colisiones = sprite.spritecollide(self, group, True)
        for b in colisiones:
            self.lives -= 1
            self.rect.x = self.x #cada vez que muere, reaparece en la posicion de inicio
            self.rect.y = self.y
        
        return self.lives


    @property
    def image(self):
        return self.frames[self.frame_act]
