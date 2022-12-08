from jugador import *
from configuraciones import *
from auxiliar import Auxiliar
import math

class Bullet():
    
    def __init__(self,owner,x_init,y_init,x_end,y_end,speed,frame_rate_ms,move_rate_ms,width=50,height=50) -> None:
        self.direccion = IZQUIERDA
        self.disparando = {}
        self.disparando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\idle\00{0}.png",4,False,w=width,h=height)
        self.disparando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\idle\00{0}.png",4,True,w=width,h=height)

        self.speed = speed
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.animacion = self.disparando[self.direccion]
        self.frame = 0
        self.image = self.animacion[self.frame]
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        angle = math.atan2(y_end - y_init, x_end - x_init) #Obtengo el angulo en radianes
        print('El angulo engrados es:', int(angle*180/math.pi))

        self.move_x = math.cos(angle)*self.speed
        self.move_y = math.sin(angle)*self.speed
        
   
    def change_x(self,delta_x):
        self.x += delta_x
        self.rect.x = int(self.x)   

    def change_y(self,delta_y):
        self.y += delta_y
        self.rect.y = int(self.y)

    def do_movement(self,delta_ms):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rect)
        self.image = self.animacion[self.frame]
        screen.blit(self.image,self.rect)

    def update(self,delta_ms):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms) 

    
