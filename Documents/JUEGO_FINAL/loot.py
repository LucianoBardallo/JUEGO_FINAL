import pygame
from auxiliar import *
from configuraciones import *

class Botín:
    """
    Esta clase representa a un objeto recolectable del juego, con la imagen de una manzana

    Parametros: una posicion x, una posicion y, un frame_rate que representa cuan rapido se actualiza la animacion.
    """
    def __init__(self,x,y,frame_rate_ms):

        self.parado = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + "Items\Fruits\Apple.png",columnas=17,filas=1,scale=2)
        self.desapareciendo = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + "Items\Fruits\Collected.png",columnas=6,filas=1,scale=2)
        self.animacion = self.parado
        self.frame = 0
        self.imagen = self.animacion[self.frame]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(x+self.rect.width/3,y+self.rect.height/3,self.rect.width/3,self.rect.height/3)
        self.frame_rate_ms = frame_rate_ms
        self.tiempo_transcurrido_animation = 0
        self.recolectado = False
        

    def draw(self,pantalla):
        if self.recolectado == False:
            if(DEBUG):
                pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)
            self.imagen = self.animacion[self.frame]
            pantalla.blit(self.imagen,self.rect)

    def update(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
            
        



            
    
