import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Bala:
    """
    Esta clase representa a una bala que viaja derecho hacia donde se derecto la colision de la vista del enemigo con el jugador.

    Parametros: una posicion x, una posicion y, un frame rate de la animacion, direccion hacia donde va la bala, y una velocidad de disparo
    """
    def __init__(self,x,y,frame_rate_ms,direccion,velocidad_disparo):
        self.direccion = direccion

        self.disparando = {}
        self.disparando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Objects/Bullet_{0}.png",5,False,w=25,h=25)
        self.disparando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Objects/Bullet_{0}.png",5,True,w=25,h=25)

        self.impactando = {}
        self.impactando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Objects/Muzzle_{0}.png",5,False,w=25,h=25)
        self.impactando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Objects/Muzzle_{0}.png",5,True,w=25,h=25)

        self.animacion = self.disparando[self.direccion]
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rectangulo_colision = pygame.Rect(x+self.rect.width/3,y+self.rect.height/3,self.rect.width/3,self.rect.height/3)

        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animation = 0
        self.tiempo_trayectoria = 0
        self.impacto = False
        self.velocidad_disparo = velocidad_disparo
        self.mover_x = 0

        self.velocidad_trayectoria = {}
        self.velocidad_trayectoria[DERECHA] = self.velocidad_disparo
        self.velocidad_trayectoria[IZQUIERDA] = -self.velocidad_disparo

    def trayectoria(self):
        self.velocidad_disparo = self.velocidad_trayectoria[self.direccion]
        self.rect.x += self.velocidad_disparo
        self.rectangulo_colision.x += self.velocidad_disparo

    def actualizar_frames(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def draw(self,screen):
        if self.impacto == False:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rectangulo_colision)
            self.imagen = self.animacion[self.frame]
            screen.blit(self.imagen,self.rect)

    def update(self,delta_ms):
        self.trayectoria()
        self.actualizar_frames(delta_ms)
    
        


            
        
    