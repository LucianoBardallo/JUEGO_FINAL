import pygame
from auxiliar import Auxiliar
from configuraciones import *
from plataformas import *
from objetos import *
from balas import *
from bullet import Bullet
from gui.gui_progressbar import *

class Boss:
    def __init__(self,x,y,frame_rate_ms):

        self.direccion = IZQUIERDA
        self.parado = {}
        self.parado[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\idle\00{0}.png",9,False,w=500,h=500)

        self.disparando_abrir = {}
        self.disparando_abrir[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\fire\00{0}.png",5,False,w=500,h=500)

        self.disparando_cerrar = {}
        self.disparando_abrir[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\fire2\00{0}.png",5,False,w=500,h=500)

        self.ojo_stage = {}
        self.ojo_stage["one"] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\eye\00{0}.png",7,False,w=100,h=100)
        self.ojo_stage["two"] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\eye2\00{0}.png",7,False,w=100,h=100)
        self.ojo_stage["three"] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\eye3\00{0}.png",7,False,w=100,h=100)
        self.ojo_stage["four"] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\eye4\00{0}.png",7,False,w=100,h=100)
        self.ojo_stage["five"] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + r"Characters\boss\eye5\00{0}.png",7,False,w=100,h=100)


        self.vidas = 1
        self.hp = 10000
        self.frame = 0
        self.frame2 = 0
        self.animacion = self.parado[self.direccion]
        self.animacion2 = self.ojo_stage["one"]
        self.imagen = self.animacion[self.frame]
        self.imagen2 = self.animacion2[self.frame2]

        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect_ojo = self.imagen2.get_rect()
        self.rect_ojo.x = x+200
        self.rect_ojo.y = y+250

        self.rect_boca = self.imagen2.get_rect()
        self.rect_boca.centerx = 850
        self.rect_boca.centery = 450

        self.rect_vision = self.imagen2.get_rect()
        self.rect_vision.y = 0
        self.rect_vision.x = 0
        self.rect_vision.height = 500
        self.rect_vision.width = 800

        
        self.tiempo_transcurrido_animation_cuerpo = 0
        self.tiempo_transcurrido_animation_ojo = 0
        self.frame_rate_ms = frame_rate_ms

        self.municiones = []
        self.disparo_cooldown = 0

        self.vivo = True
        self.blink = True


    def hacer_animacion_cuerpo(self,delta_ms):
        self.tiempo_transcurrido_animation_cuerpo += delta_ms
        if(self.tiempo_transcurrido_animation_cuerpo >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation_cuerpo = 0
            if(self.frame < len(self.animacion) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def hacer_animacion_ojo(self,delta_ms):
        self.tiempo_transcurrido_animation_ojo += delta_ms
        if(self.tiempo_transcurrido_animation_ojo >= self.frame_rate_ms + 80):
            self.tiempo_transcurrido_animation_ojo = 0
            if(self.frame2 < len(self.animacion2) - 1):
                self.frame2 += 1 
            else: 
                self.frame2 = 0
                if self.blink:
                    self.frame2 = len(self.animacion2) - 4
    
    def disparar(self,shoot,pos_xy):
        if shoot:
            self.esta_disparando = True
            if self.disparo_cooldown == 0:
                pygame.mixer.Sound.play(self.sonidos[6])
                self.disparo_cooldown = 200
                bala = Bullet(owner=self,x_init=self.rect_boca.centerx,y_init=self.rect_boca.centery,
                x_end=pos_xy.centerx,y_end=pos_xy.centery,speed=8,frame_rate_ms=20,move_rate_ms=20,width=50,height=50)
                self.municiones.append(bala)
        else:
            self.esta_disparando = False

    def actualizar_bala(self,delta_ms,pantalla,player):
        if self.disparo_cooldown > 0:
            self.disparo_cooldown -= 1
        for bala in self.municiones:
            bala.update(delta_ms,[],[],player)
            bala.draw(pantalla)
            if bala.impacto:
                self.municiones.remove(bala)
    
    def actualizar_vida(self):
        if self.hp <= 0:
            self.vidas -= 1
        if self.vidas < 1:
            pygame.mixer.Sound.play(self.sonidos[7])
            self.vivo = False
        
        if self.hp < 8000:
            if self.frame2 == 4:
                self.blink = True
            self.animacion2 = self.ojo_stage["two"]
        if self.hp < 6000:
            self.animacion2 = self.ojo_stage["three"]
        if self.hp < 4000:
            self.animacion2 = self.ojo_stage["four"]
        if self.hp < 2000:
            self.animacion2 = self.ojo_stage["five"]
        
    def hacer_colision(self, pos_xy):
        self.disparar(False,pos_xy)
        if self.rect_vision.colliderect(pos_xy):
            self.disparar(True,pos_xy)
        for bala in self.municiones:
            if bala.rect.colliderect(pos_xy):
                self.municiones.remove(bala)

    def draw(self,pantalla):
        if self.vidas > 0:
            self.imagen = self.animacion[self.frame]
            self.imagen2 = self.animacion2[self.frame2]
            pantalla.blit(self.imagen,self.rect)
            pantalla.blit(self.imagen2,self.rect_ojo)
            if DEBUG:
                pygame.draw.rect(pantalla,(255,0,0),self.rect_ojo)
                pygame.draw.rect(pantalla,(255,255,0),self.rect_vision)
                pygame.draw.rect(pantalla,(255,0,0),self.rect_boca)

    def update(self,delta_ms,pantalla,pos_xy,sonidos,player):
        self.sonidos = sonidos
        self.hacer_animacion_cuerpo(delta_ms)
        self.hacer_animacion_ojo(delta_ms)
        self.hacer_colision(pos_xy)
        self.actualizar_bala(delta_ms,pantalla,player)
        self.actualizar_vida()
