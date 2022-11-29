import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Obstaculo:
    def __init__(self, x, y,ancho, alto, tipo=1):

        self.imagenes= Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "TileSet\space_ship\Tiles\Acid ({0}).png",2,flip=False,w=ancho,h=alto)
        self.imagen = self.imagenes[tipo]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(self.rect)

    def renderizar(self,pantalla):
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)

