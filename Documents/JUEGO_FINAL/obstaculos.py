import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Obstaculo:
    """
    Esta clase representa a un obstaculo del juego

    Parametros: recibe la posicion x, la posicion y, un ancho y largo, y el tipo de tile
    """
    def __init__(self, x, y,ancho, alto, tipo=1):
        self.imagenes= Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "TileSet\space_ship\Tiles\Acid ({0}).png",2,flip=False,w=ancho,h=alto)
        self.imagen = self.imagenes[tipo]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(self.rect)
        self.rectangulo_pies = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_pies.height = ALTURA_PIES
        self.rectangulo_pies.y = y + self.rect.height - ALTURA_PIES

    def draw(self,pantalla):
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)

class Obstaculo_Pincho(Obstaculo):
    """
    Esta clase representa a un obstaculo en forma de pincho

    Parametros: recibe la posicion x, la posicion y, un ancho y largo, y el tipo de tile
    """
    def __init__(self, x, y, ancho, alto, tipo=0):
        super().__init__(x, y, ancho, alto, tipo)
        self.imagenes= Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "TileSet\space_ship\Objects\Object ({0}).png",1,flip=False,w=ancho,h=alto)
        self.imagen = self.imagenes[tipo]

class Obstaculo_sierra(Obstaculo):
    """
    Esta clase representa un obstaculo en forma de sierra, la cual tiene una animacion

    Parametros: recibe la posicion x, la posicion y, un ancho y largo, y el tipo de tile
    """
    def __init__(self, x, y, ancho, alto, tipo=1):
        super().__init__(x, y, ancho, alto, tipo)
        self.sierra_on = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + "TileSet\space_ship\Obstaculos\On (38x38).png",8,1,flip=False,scale=2)
        self.animacion = self.sierra_on
        self.frame = 0
        self.frame_rate_ms = 20
        self.imagen = self.animacion[self.frame]
        self.tiempo_transcurrido_animation = 0

        self.rectangulo_pies.y = y + self.rect.height - ALTURA_PIES * 3
    
    def update(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def draw(self,pantalla):
        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)
            

    

