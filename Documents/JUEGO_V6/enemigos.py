import pygame
from auxiliar import Auxiliar
from configuraciones import *
from plataformas import *
from objetos import *
from balas import Bala

class Enemigo:
    def __init__(self,x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla=0):

        self.direccion = DERECHA
        self.parado = {}
        self.parado[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_idle2.png",37,11,True,scale=0.8)[:402]
        self.parado[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_idle2.png",37,11,scale=0.8)[:402]

        self.caminando = {}
        self.caminando[IZQUIERDA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,True,scale=0.8)
        self.caminando[DERECHA] = Auxiliar.getSurfaceFromSpriteSheet(RUTA_IMAGEN + r"Characters\enemies\set_juju\black\juju_move_right.png",8,2,scale=0.8)

        self.frame = 0
        self.mover_x = 0
        self.mover_y = 0
        self.mover = 0
        self.gravedad = gravedad
        self.velocidad_movimiento = velocidad_movimiento
        self.animacion = self.caminando[self.direccion]
        self.imagen = self.animacion[self.frame]

        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rectangulo_colision = pygame.Rect(x+self.rect.width/3,y+20,self.rect.width/2,self.rect.height-20)

        self.rectangulo_pies = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_pies.height = ALTURA_PIES
        self.rectangulo_pies.y = y + self.rect.height - ALTURA_PIES

        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms

        self.patrulla = patrulla
        self.mover_izquierda = True
        self.vivo = True

        self.comienzo_patrulla = self.rect.centerx
        
    def cambiar_x(self,delta_x):
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x

    def cambiar_y(self,delta_y):
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y

    def verificar_plataforma(self, tiles, plataformas):
        self.sobre_plataforma = False
        for tile in tiles:
            if type(tile) == Plataforma or type(tile) == Objeto_Estatico or type(tile) == Muro:
                if self.rectangulo_pies.colliderect(tile.rectangulo_pies):
                    self.sobre_plataforma = True
                    break
        for plataforma in plataformas:
            if self.rectangulo_pies.colliderect(plataforma.rectangulo_pies):
                self.sobre_plataforma = True
                if plataforma.mover_izquierda or plataforma.mover_derecha:
                    self.move_x = plataforma.move_x
                else:
                    self.move_y = plataforma.move_y
                    self.cambiar_y(self.move_y)
                break

    def aplicar_gravedad(self):
        if not self.sobre_plataforma:
            self.mover_y = self.gravedad
        else:
            self.mover_y = 0

    def hacer_movimiento(self,delta_ms,tiles,plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            self.verificar_plataforma(tiles,plataformas)
            self.aplicar_gravedad()
            self.cambiar_x(self.mover_x)
            self.cambiar_y(self.mover_y)

    def hacer_animacion(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0
    
    def draw(self,pantalla):
        if DEBUG:
            pygame.draw.rect(pantalla,(255,0,0),self.rectangulo_colision)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen,self.rect)

    def update(self,delta_ms,plataformas):
        self.hacer_movimiento(delta_ms,plataformas)
        self.hacer_animacion(delta_ms)
        self.actualizar_vida()

class Enemigo_Melee(Enemigo):
    def __init__(self,x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla=0):
        super().__init__(x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla)
        self.vidas = 5

    def patrullar(self):
        if self.vidas > 0:
            if self.rect.x >= self.comienzo_patrulla - self.patrulla and self.mover_izquierda:
                self.mover_x = -self.velocidad_movimiento
                self.animacion = self.caminando[IZQUIERDA]
            elif self.rect.x <= self.comienzo_patrulla + self.patrulla:
                self.mover_izquierda = False
                self.mover_x = self.velocidad_movimiento
                self.animacion = self.caminando[DERECHA]
            else:
                self.mover_izquierda = True

    def hacer_movimiento(self,delta_ms,tiles,plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            self.verificar_plataforma(tiles,plataformas)
            self.aplicar_gravedad()
            self.patrullar()
            self.cambiar_x(self.mover_x)
            self.cambiar_y(self.mover_y)
    
    def actualizar_vida(self):
        if self.vidas < 1:
            pygame.mixer.Sound.play(self.sonidos[8])
            self.vivo = False
    
    def draw(self,pantalla):
        if DEBUG:
            pygame.draw.rect(pantalla,(255,0,0),self.rectangulo_colision)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen,self.rect)

    def update(self,delta_ms,tiles,sonidos,plataformas):
        self.sonidos = sonidos
        self.hacer_movimiento(delta_ms,tiles,plataformas)
        self.hacer_animacion(delta_ms)
        self.actualizar_vida()

class Enemigo_Distancia(Enemigo):
    def __init__(self,x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla=0,direccion=DERECHA):
        super().__init__(x,y,velocidad_movimiento,gravedad,frame_rate_ms,move_rate_ms,patrulla)

        self.direccion = direccion
        self.rectangulo_vision = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_vision.centerx = 0
        self.rectangulo_vision.centery = y + 75
        self.rectangulo_vision.height = ALTURA_PIES * 3
        self.rectangulo_vision.width = 1200
        self.vidas = 3

        self.animacion = self.parado[direccion]

        self.municiones = []
        self.disparo_cooldown = 0
        

    def cambiar_x(self,delta_x):
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x
        self.rectangulo_vision.x += delta_x

    def cambiar_y(self,delta_y):
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y
        self.rectangulo_vision.y += delta_y    

    def disparar(self,shoot=True):
        self.esta_disparando = False
        if shoot:
            self.esta_disparando = True
            if self.disparo_cooldown == 0:
                pygame.mixer.Sound.play(self.sonidos[0])
                self.disparo_cooldown = 120
                bala = Bala(self.rectangulo_colision.centerx + (0.6 * self.rectangulo_colision.size[0] * self.direccion),self.rectangulo_colision.centery-20,frame_rate_ms=20,direccion=self.direccion,velocidad_disparo=2)
                self.municiones.append(bala)

    def actualizar_bala(self,delta_ms,pantalla):
        if self.disparo_cooldown > 0:
            self.disparo_cooldown -= 1
        for bala in self.municiones:
            bala.update(delta_ms)
            bala.draw(pantalla)

    def actualizar_vida(self):
        if self.vidas < 1:
            pygame.mixer.Sound.play(self.sonidos[8])
            self.vivo = False

    def draw(self,pantalla):
        if DEBUG:
            pygame.draw.rect(pantalla,(255,0,0),self.rectangulo_colision)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_vision)
        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen,self.rect)

    def hacer_movimiento(self,delta_ms,tiles,plataformas):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.verificar_plataforma(tiles,plataformas)
            self.aplicar_gravedad()
            self.cambiar_x(self.mover_x)
            self.cambiar_y(self.mover_y)

    def hacer_colision(self, pos_xy):
        self.disparar(False)
        if self.rectangulo_vision.colliderect(pos_xy):
            self.disparar(True)
            
    def update(self,pantalla,delta_ms,tiles,pos_xy,sonidos,plataformas):
        self.sonidos = sonidos
        self.actualizar_vida()
        self.hacer_movimiento(delta_ms,tiles,plataformas)
        self.hacer_animacion(delta_ms)
        self.hacer_colision(pos_xy)
        self.actualizar_bala(delta_ms,pantalla)


    