import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Objeto:
    """
    Esta clase representa un objeto del juego

    Parametros, recibe la posicion de x, la posicion de y, un ancho y un largo y por ultimo un tipo de tile
    """
    def __init__(self, x, y,ancho, alto, tipo_desbloqueado=1):
        self.imagenes= Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "TileSet\space_ship\Objects\Object ({0}).png",9,flip=False,w=ancho,h=alto)
        self.imagen = self.imagenes[tipo_desbloqueado]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(self.rect)
        self.activado = False
        self.desbloqueado = False

    def draw(self,pantalla):
        """
        Este metodo se encarga de 'dibujar' lo que aparece en pantalla, tambien tiene un modo debug que muestra los rectangulos. 

        Parametros: recibe como parametro la pantalla que es donde se va a 'dibujar' el objeto
        """
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)

class Objeto_Estatico(Objeto):
    """
    Esta clase representa un objeto estatico (sin animacion)

    Parametros, recibe la posicion de x, la posicion de y, un ancho y un largo y por ultimo un tipo de tile
    """
    def __init__(self, x, y,ancho, alto, tipo_desbloqueado=1):
        super().__init__(x, y,ancho, alto, tipo_desbloqueado=1)
        self.imagen = self.imagenes[tipo_desbloqueado]
        self.rectangulo_pies = pygame.Rect(self.rect)
        self.rectangulo_pies.height = ALTURA_PIES

class Objeto_Animado(Objeto):
    """
    Esta clase representa un objeto animado del juego

    Parametros: recibe una posicion de x, una posicion de y, un ancho y largo, un tipo que representa al objeto desbloqueado,
    otro tipo que representa al objeto abierto, y por ultimo un tipo que representa al objeto bloqueado
    """
    def __init__(self,nombre, x, y,ancho, alto, tipo_desbloqueado=1 ,tipo_abierto =1,tipo_bloqueado = 1):
        super().__init__(x, y,ancho, alto, tipo_desbloqueado=1)
        self.nombre = nombre
        self.tipo_abierto = tipo_abierto
        self.tipo_desbloqueado = tipo_desbloqueado
        self.tipo_bloqueado = tipo_bloqueado
        
    def draw(self,pantalla):
        """
        Este metodo se encarga de 'dibujar' lo que aparece en pantalla, tambien tiene un modo debug que muestra los rectangulos. 
        Cambia la imagen dependiendo del estado que se encuentra el objeto animado

        Parametros: recibe como parametro la pantalla que es donde se va a 'dibujar' el objeto
        """
        self.imagen = self.imagenes[self.tipo_bloqueado]
        if self.desbloqueado:
            self.imagen = self.imagenes[self.tipo_desbloqueado]
            if self.activado:
                self.imagen = self.imagenes[self.tipo_abierto]
            
        pantalla.blit(self.imagen,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)


        
    

