import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Bala:
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

    def renderizar(self,screen):
        if self.impacto == False:
            if(DEBUG):
                pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rectangulo_colision)
            self.imagen = self.animacion[self.frame]
            screen.blit(self.imagen,self.rect)

    def actualizar_frames(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def actualizar(self,delta_ms,screen):
        self.renderizar(screen)
        self.trayectoria()
        self.actualizar_frames(delta_ms)
    
# class Boss_Disparo(Bala):
#     def __init__(self, x, y, frame_rate_ms, direccion, velocidad_disparo):
#         super().__init__(x, y, frame_rate_ms, direccion, velocidad_disparo)
        
#         self.disparando = {}
#         self.disparando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\idle\00{0}.png",4,False,w=50,h=50)
#         self.disparando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\idle\00{0}.png",4,True,w=50,h=50)

#         self.impactando = {}
#         self.impactando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\hit\00{0}.png",6,False,w=50,h=50)
#         self.disparando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\hit\00{0}.png",6,True,w=50,h=50)

class Boss_Disparo:
    def __init__(self,x,y,frame_rate_ms,direccion,velocidad_disparo):
        self.direccion = direccion

        self.disparando = {}
        self.disparando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\idle\00{0}.png",4,False,w=100,h=100)
        self.disparando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\BossFireball\idle\00{0}.png",4,True,w=100,h=100)

        self.animacion = self.disparando[self.direccion]
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rectangulo_colision = pygame.Rect(x+self.rect.width/3,y+self.rect.height/3,self.rect.width/3,self.rect.height/3)

        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animation = 0
        self.impacto = False
        self.velocidad_disparo = velocidad_disparo

        self.velocidad_trayectoria = {}
        self.velocidad_trayectoria[DERECHA] = self.velocidad_disparo
        self.velocidad_trayectoria[IZQUIERDA] = -self.velocidad_disparo

    def trayectoria(self):
        self.velocidad_disparo = self.velocidad_trayectoria[self.direccion]
        self.rect.x += self.velocidad_disparo
        self.rectangulo_colision.x += self.velocidad_disparo

    def renderizar(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.rectangulo_colision)
        self.imagen = self.animacion[self.frame]
        screen.blit(self.imagen,self.rect)

    def actualizar_frames(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def actualizar(self,delta_ms,screen):
        self.renderizar(screen)
        self.trayectoria()
        self.actualizar_frames(delta_ms) 
        


            
        
    