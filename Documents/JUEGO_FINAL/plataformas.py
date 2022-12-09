import pygame
from configuraciones import *
from auxiliar import Auxiliar

class Plataforma:
    """
    Esta clase son las plataformas donde el jugador puedde pisar y se crean a partir de tiles
    """
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

    def draw(self,pantalla):
        pantalla.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)

class Muro(Plataforma):
    """
    Esta clase representan a los muros que encierran un nivel, el jugador no puedo atravesarlos
    """
    def __init__(self, x, y, ancho, alto, tipo=1, reverso=False):
        super().__init__(x, y, ancho, alto, tipo, reverso)
        

class Platforma_Mobiles(Plataforma):
    """
    Esta clase representa a las plataformas mobiles, que se mueven en un patron especifico pasado por parametro, pueden moverse verticalmente o horizontal

    Parametros: Recibe la posicion de x, la posicion de y, ancho y largo, tipo de tile, velocidad a la que se mueve, 
    un rate_ms que representa que tan rapido se actualizara, un punto de inicio, y otro de final, y por ultimo una direccion.
    """
    def __init__(self, x, y, ancho, alto, tipo, velocidad, move_rate_ms, punto_inicio, punto_final,direccion,reverso = False):
        super().__init__(x, y, ancho, alto, tipo, reverso = False)

        self.direccion = direccion
        self.punto_inicio = punto_inicio
        self.punto_final = punto_final

        if self.direccion == "vertical":
            self.mover_arriba = True
            self.mover_abajo = False
            self.mover_izquierda = False
            self.mover_derecha = False
        else:
            self.mover_arriba = False
            self.mover_abajo = False
            self.mover_izquierda = False
            self.mover_derecha = True

        self.velocidad = velocidad
        self.move_x = 0
        self.move_y = 0

        self.direccion = direccion
        
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
     
    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.rectangulo_pies.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.rectangulo_pies.y += delta_y

    def mover_plataforma_horizontal(self):
        if(self.mover_derecha):
            self.move_x = self.velocidad
        elif(self.mover_izquierda):
            self.move_x = -self.velocidad
        self.change_x(self.move_x)

    def mover_plataforma_vertical(self):
        if(self.mover_arriba):
            self.move_y = -self.velocidad
        elif(self.mover_abajo):
            self.move_y = self.velocidad
        self.change_y(self.move_y)

    def actualizar_plataformas(self):
        if self.direccion == "horizontal":
            if(self.rect.x >= self.punto_final):
                self.mover_derecha = False
                self.mover_izquierda = True
            elif(self.rect.x <= self.punto_inicio):
                self.mover_derecha = True
                self.mover_izquierda = False
        else:
            if(self.rect.y >= self.punto_final):
                self.mover_arriba = True
                self.mover_abajo = False
            elif(self.rect.y <= self.punto_inicio):
                self.mover_arriba = False
                self.mover_abajo = True

    
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.rect_pies)

    def update(self,delta_ms):   
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.mover_plataforma_horizontal()
            self.mover_plataforma_vertical()
            self.actualizar_plataformas()
            self.tiempo_transcurrido_move = 0

            


