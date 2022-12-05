import pygame
from configuraciones import *
from auxiliar import Auxiliar
from balas import Bala
from enemigos import *
from plataformas import *
from objetos import *
from obstaculos import *
import sys

class Jugador:
    def __init__(self,x,y,velocidad_movimiento,gravedad,fuerza_salto,frame_rate_ms,frame_rate_jump_ms,move_rate_ms,altura_salto,p_scale=1) -> None:
        
        self.parado = {}
        self.parado[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Idle ({0}).png",10,False,w=100,h=100)
        self.parado[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Idle ({0}).png",10,True,w=100,h=100)

        self.caminando = {}
        self.caminando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Run ({0}).png",8,False,w=100,h=100)
        self.caminando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Run ({0}).png",8,True,w=100,h=100)
        
        self.saltando = {}
        self.saltando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Jump ({0}).png",5,False,w=100,h=100)
        self.saltando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Jump ({0}).png",5,True,w=100,h=100)

        self.cayendo = {}
        self.cayendo[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Fall ({0}).png",5,False,w=100,h=100)
        self.cayendo[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Fall ({0}).png",5,True,w=100,h=100)

        self.muriendo = {}
        self.muriendo[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Dead ({0}).png",10,False,w=100,h=100)
        self.muriendo[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Dead ({0}).png",10,True,w=100,h=100)

        self.disparar_corriendo = {}
        self.disparar_corriendo[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/RunShoot ({0}).png",9,False,w=100,h=100)
        self.disparar_corriendo[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/RunShoot ({0}).png",9,True,w=100,h=100)

        self.disparando = {}
        self.disparando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Shoot ({0}).png",4,False,w=100,h=100)
        self.disparando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Shoot ({0}).png",4,True,w=100,h=100)

        self.atacando = {}
        self.atacando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Melee ({0}).png",8,False,w=100,h=100)
        self.atacando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Melee ({0}).png",8,True,w=100,h=100)

        self.disparar_saltando = {}
        self.disparar_saltando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpMelee ({0}).png",8,False,w=100,h=100)
        self.disparar_saltando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpMelee ({0}).png",8,True,w=100,h=100)

        self.atacar_saltando = {}
        self.atacar_saltando[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpShoot ({0}).png",5,False,w=100,h=100)
        self.atacar_saltando[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/JumpShoot ({0}).png",5,True,w=100,h=100)

        self.deslizarse = {}
        self.deslizarse[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Slide ({0}).png",10,False,w=100,h=100)
        self.deslizarse[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Slide ({0}).png",10,True,w=100,h=100)

        self.velocidad_movimiento = {}
        self.velocidad_movimiento[DERECHA] = velocidad_movimiento
        self.velocidad_movimiento[IZQUIERDA] = -velocidad_movimiento

        self.lives = 1
        self.vidas = 5
        
        self.frame = 0
        self.move_x = 0
        self.move_y = 0
        self.gravedad = gravedad
        self.fuerza_salto = fuerza_salto
        self.direccion = DERECHA
        self.animacion = self.parado[self.direccion]
        self.imagen = self.animacion[self.frame]

        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectangulo_colision = pygame.Rect(x+self.rect.width/3,y+20,self.rect.width/3,self.rect.height-20)

        self.rectangulo_pies = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_pies.height = ALTURA_PIES
        self.rectangulo_pies.y = y + self.rect.height - ALTURA_PIES

        self.rectangulo_cabeza = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_cabeza.height = ALTURA_PIES
        self.rectangulo_cabeza.y = y + ALTURA_PIES

        self.rectangulo_derecha = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_derecha.width = ALTURA_PIES
        self.rectangulo_derecha.height = 70
        self.rectangulo_derecha.x = x + self.rect.width - ALTURA_PIES * 3
        self.rectangulo_derecha.y = y + ALTURA_PIES * 2

        self.rectangulo_izquierda = pygame.Rect(self.rectangulo_colision)
        self.rectangulo_izquierda.width = ALTURA_PIES
        self.rectangulo_izquierda.height = 70
        self.rectangulo_izquierda.x = x + ALTURA_PIES * 2
        self.rectangulo_izquierda.y = y + ALTURA_PIES * 2
    
        self.esta_saltando = False
        self.esta_cayendo = False
        self.esta_caminando = False
        self.esta_disparando = False
        self.esta_pegando = False
        self.puede_ganar = False
        self.invensible = False
        self.vivo = True
        self.ganar = False

        self.frame_rate_ms = frame_rate_ms 
        self.frame_rate_jump_ms = frame_rate_jump_ms
        self.move_rate_ms = move_rate_ms
        self.comienzo_salto = self.rectangulo_pies.y
        self.altura_salto = altura_salto

        self.tiempo_activado = 0
        self.tiempo_recolectado = 0
        self.tiempo_looteado = 0
        self.tiempo_transcurrido = 0
        self.tiempo_transcurrido_disparo = 0
        self.tiempo_transcurrido_animacion = 0
        self.tiempo_transcurrido_movimiento = 0
        self.tiempo_inmune = 0

        self.municiones = []
        self.disparo_cooldown = 0
        self.municion = 100

        self.move_alloved = {}
        self.move_alloved[IZQUIERDA] = True
        self.move_alloved[DERECHA] = True

        self.dead_sound = pygame.mixer.Sound(RUTA_MUSICA + r"muerte_robot.wav")
        self.shoot_sound = pygame.mixer.Sound(RUTA_MUSICA + r"laser_gun.wav")

    #ACCIONES
    def caminar(self,direccion:int): 
        if self.vivo:
            self.direccion = direccion
            self.esta_caminando = True
            if self.move_alloved[self.direccion]:
                self.move_x = self.velocidad_movimiento[self.direccion]
                if self.esta_saltando:
                    self.move_x = self.velocidad_movimiento[self.direccion] // 2
         
    def parar(self):
        self.esta_caminando = False
        self.move_x = 0

    def disparar(self,shoot=True):
        if shoot:
            self.esta_disparando = True
            if self.disparo_cooldown == 0 and self.municion > 0:
                self.disparo_cooldown = 20
                bala = Bala(self.rectangulo_colision.centerx + (0.6 * self.rectangulo_colision.size[0] * self.direccion),self.rectangulo_colision.centery-20,frame_rate_ms=20,direccion=self.direccion,velocidad_disparo=8)
                self.municiones.append(bala)
                self.municion -= 1
        else:
            self.esta_disparando = False
    
    def atacar(self,melee=True):
        self.esta_pegando = melee
        if melee:
            self.esta_pegando = True
        
    def saltar(self, jump=True):
        if jump:
            if self.sobre_plataforma:
                self.esta_saltando = True
                self.move_x = 0
                self.move_y = -self.fuerza_salto
                self.comienzo_salto = self.rectangulo_pies.y
        else:
            self.esta_saltando = False

    #VERIFICACIONES     
    def limitar_salto(self):
        if self.rectangulo_pies.y < self.comienzo_salto - 150:
            self.esta_saltando = False
 

    def verificar_plataforma(self, tiles,obstaculos,plataformas):
        if not self.esta_saltando:
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
                        if self.esta_caminando:
                            self.move_x = self.velocidad_movimiento[self.direccion] + plataforma.move_x
                        else:
                            self.move_x = plataforma.move_x
                    else:
                        self.move_y = plataforma.move_y
                        self.cambiar_y(self.move_y)
                    break
            for obstaculo in obstaculos:
                if type(obstaculo) == Obstaculo_Pincho:
                    if self.rectangulo_pies.colliderect(obstaculo.rectangulo_pies):
                        self.sobre_plataforma = True
                        break
                

    def aplicar_gravedad(self):
        if not self.esta_saltando:
            if not self.sobre_plataforma:
                self.move_y = self.gravedad
                self.esta_cayendo = True
            else:
                self.move_y = 0
                self.esta_cayendo = False

    def actualizar_invensible(self, delta_ms):
        if self.invensible:
            self.tiempo_inmune += delta_ms
            if self.tiempo_inmune > 1500:
                self.tiempo_inmune = 0
                self.invensible = False

    
    def actualizar_bala(self,delta_ms,pantalla):
        if self.disparo_cooldown > 0:
            self.disparo_cooldown -= 1
        for bala in self.municiones:
            bala.actualizar(delta_ms,pantalla)
            if bala.impacto:
                self.municiones.remove(bala)

    def comprobar_vidas(self,sonidos):
        if self.vidas < 1:
            pygame.mixer.Sound.play(sonidos[3])
            self.vivo = False
    
    #MOVIMIENTO
    def cambiar_x(self,delta_x):
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x
        self.rectangulo_cabeza.x += delta_x
        self.rectangulo_derecha.x += delta_x
        self.rectangulo_izquierda.x += delta_x


    def cambiar_y(self,delta_y):
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y
        self.rectangulo_cabeza.y += delta_y
        self.rectangulo_derecha.y += delta_y
        self.rectangulo_izquierda.y += delta_y

    #ANIMACIONES
    def animaciones(self):
        if self.vivo:
            if self.esta_saltando:
                self.cambiar_animacion(self.saltando)
            elif(self.esta_cayendo):
                self.cambiar_animacion(self.cayendo)
            elif(self.esta_caminando):
                self.cambiar_animacion(self.caminando)
            elif(self.esta_disparando):
                self.cambiar_animacion(self.disparando)
            elif(self.esta_pegando):
                self.cambiar_animacion(self.atacando)
            else:
                self.cambiar_animacion(self.parado)
        else:
            self.cambiar_animacion(self.muriendo)


    def cambiar_animacion(self, animation):
        if self.animacion != animation[DERECHA] and self.animacion != animation[IZQUIERDA]:
            self.frame = 0
        self.animacion = animation[self.direccion]


    def actualizar_frames(self,delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms
        if self.esta_saltando or self.esta_cayendo:
            if(self.tiempo_transcurrido_animacion >= self.frame_rate_jump_ms):
                self.tiempo_transcurrido_animacion = 0
                if(self.frame < len(self.animacion) - 1):
                    self.frame += 1 
                else:
                    self.frame = 0
                    if self.esta_cayendo:
                        self.frame = len(self.animacion) - 1   
                 
        else:
            if(self.tiempo_transcurrido_animacion >= self.frame_rate_ms):
                self.tiempo_transcurrido_animacion = 0
                if(self.frame < len(self.animacion) - 1):
                    self.frame += 1 
                else:
                    self.frame = 0
                    if self.vivo == False:
                        self.frame = len(self.animacion) - 1 

    def renderizar(self,pantalla):
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_cabeza)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_derecha)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_izquierda)
        
        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen,self.rect)

    def eventos(self,teclas,eventos,sonidos):
        #EVENTOS
        for evento in eventos:
            if evento.type == pygame.QUIT: # Salir
                pygame.quit()
                sys.exit() 
            
            if evento.type == pygame.KEYDOWN: # Apretar alguna tecla
                if evento.key == pygame.K_SPACE: # Saltar
                    self.saltar()
            
                if evento.key == pygame.K_s: # Saltar
                    self.disparar(True)
                    pygame.mixer.Sound.play(sonidos[0])

                if evento.key == pygame.K_a: # Saltar
                    self.atacar()

            if evento.type == pygame.KEYUP: # Dejar de apretar alguna tecla
                if evento.key == pygame.K_RIGHT and evento.key == pygame.K_LEFT and evento.key == pygame.K_SPACE: # Quedarse quieto
                    self.parar()
            
                if evento.key == pygame.K_SPACE: # Saltar
                    self.saltar(False)
                
                if evento.key == pygame.K_s: # Saltar
                    self.disparar(False)
                
                if evento.key == pygame.K_a: # Saltar
                    self.atacar(False)

        #TECLAS PRESIONADAS
        if(teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT]):
            self.caminar(IZQUIERDA)

        if(not teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT]):
            self.caminar(DERECHA)

        if(teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT] and not teclas[pygame.K_SPACE]):
            self.parar()  
        
        if(not teclas[pygame.K_LEFT] and not teclas[pygame.K_RIGHT] and not teclas[pygame.K_SPACE]):
            self.parar()      

    #MOVIMIENTO
    def hacer_movimiento(self,delta_ms,tiles,obstaculos,plataformas):
        self.tiempo_transcurrido_movimiento += delta_ms
        if(self.tiempo_transcurrido_movimiento >= self.move_rate_ms):
            self.tiempo_transcurrido_movimiento = 0

            self.verificar_plataforma(tiles,obstaculos,plataformas)
            self.aplicar_gravedad()
            self.cambiar_y(self.move_y)
            if self.vivo:
                self.limitar_salto()
                self.cambiar_x(self.move_x)
                

    #ANIMACIONES
    def hacer_animaciones(self,delta_ms):
        self.animaciones()
        self.actualizar_frames(delta_ms)      

    #ACTUALIZACION PRINCIPAL
    def actualizar(self,delta_ms,pantalla,teclas,eventos,tiles,obstaculos,plataformas,sonidos):
        self.eventos(teclas,eventos,sonidos)
        # if not self.ganar:
        self.comprobar_vidas(sonidos)
        self.hacer_movimiento(delta_ms,tiles,obstaculos,plataformas)
        self.hacer_animaciones(delta_ms)
        self.actualizar_invensible(delta_ms)
        self.actualizar_bala(delta_ms,pantalla)
        # self.renderizar(pantalla)
        

    


