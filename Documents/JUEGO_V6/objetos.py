import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Objeto:
    def __init__(self, x, y,ancho, alto, tipo_desbloqueado=1):

        self.imagenes= Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "TileSet\space_ship\Objects\Object ({0}).png",9,flip=False,w=ancho,h=alto)
        self.imagen = self.imagenes[tipo_desbloqueado]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(self.rect)
        self.activado = False
        self.desbloqueado = False

    def renderizar(self,pantalla):
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)

class Objeto_Estatico(Objeto):
    def __init__(self, x, y,ancho, alto, tipo_desbloqueado=1):
        super().__init__(x, y,ancho, alto, tipo_desbloqueado=1)
        self.imagen = self.imagenes[tipo_desbloqueado]
        self.rectangulo_pies = pygame.Rect(self.rect)
        self.rectangulo_pies.height = ALTURA_PIES

class Objeto_Animado(Objeto):
    def __init__(self,nombre, x, y,ancho, alto, tipo_desbloqueado=1 ,tipo_abierto =1,tipo_bloqueado = 1):
        super().__init__(x, y,ancho, alto, tipo_desbloqueado=1)
        self.nombre = nombre
        self.tipo_abierto = tipo_abierto
        self.tipo_desbloqueado = tipo_desbloqueado
        self.tipo_bloqueado = tipo_bloqueado
        
    def renderizar(self,pantalla):
        self.imagen = self.imagenes[self.tipo_bloqueado]
        if self.desbloqueado:
            self.imagen = self.imagenes[self.tipo_desbloqueado]
            if self.activado:
                self.imagen = self.imagenes[self.tipo_abierto]
            
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)


        
    

