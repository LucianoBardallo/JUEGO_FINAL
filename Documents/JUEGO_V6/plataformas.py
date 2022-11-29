import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Plataforma:
    def __init__(self, x, y,ancho, alto, tipo=1,reverso = False):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "TileSet/space_ship/Tiles/Tile ({0}).png",15,flip=False,w=ancho,h=alto,reverse=reverso)
        self.image = self.image_list[tipo]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.rectangulo_colision = pygame.Rect(self.rect)
        self.rectangulo_pies = pygame.Rect(self.rect)
        self.rectangulo_pies.height = ALTURA_PIES

    def renderizar(self,pantalla):
        pantalla.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)

class Muro:
    def __init__(self, x, y,ancho, alto, tipo=1,reverso = False):

        self.imagenes= Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "TileSet/space_ship/Tiles/Tile ({0}).png",15,flip=False,w=ancho,h=alto,reverse=reverso)
        self.imagen = self.imagenes[tipo]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(self.rect)
        self.rectangulo_pies = pygame.Rect(self.rect)
        self.rectangulo_pies.height = ALTURA_PIES

    def renderizar(self,pantalla):
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)
            


