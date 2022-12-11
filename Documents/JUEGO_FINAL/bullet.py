from jugador import *
from configuraciones import *
from auxiliar import Auxiliar
import math

class Bullet():
    """
    Esta clase representa a una bala que toma como referencia la posicion del jugador para disparar en esa direccion.

    Parametros: recibe un owner que es el que va a tener la bala, una x e y inicial donde se creara la bala, 
    una x e y final que es hacia donde viajara la bala, la velocidad de disparo, frames_rates de animacion y movimiento y por ultimo el ancho y largo de la bala
    """
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
        """
        Este metodo se encarga de cambiar el valor de X para darle movimiento a la bala

        Parametros: recibe como parametro un int que representa los pixeles a mover
        """
        self.x += delta_x
        self.rect.x = int(self.x)   

    def change_y(self,delta_y):
        """
        Este metodo se encarga de cambiar el valor de Y para darle movimiento a la bala

        Parametros: recibe como parametro un int que representa los pixeles a mover
        """
        self.y += delta_y
        self.rect.y = int(self.y)

    def do_movement(self,delta_ms):
        """
        Este metodo se encarga de actualizar el movimiento de las balas

        Parametros: recibe como parametro el valor delta_ms
        """
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)

    def do_animation(self,delta_ms):
        """
        Este metodo se encarga de actualiza los frames de las animaciones

        Parametro: recibe un valor delta_ms que se acumula y ayuda a control el tiempo de la actualizacion
        """
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def draw(self,screen):
        """
        Este metodo se encarga de 'dibujar' lo que aparece en pantalla, tambien tiene un modo debug que muestra los rectangulos. 
        Por ultima actualiza la imagen que se va a blitear

        Parametros: recibe como parametro la pantalla que es donde se va a 'dibujar' el objeto
        """
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rect)
        self.image = self.animacion[self.frame]
        screen.blit(self.image,self.rect)

    def update(self,delta_ms):
        """
        Este metodo se encarga de utilizar los metodos creados anteriormente y actualizarlos
        """
        self.do_movement(delta_ms)
        self.do_animation(delta_ms) 

    
