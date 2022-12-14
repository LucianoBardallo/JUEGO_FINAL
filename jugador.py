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
    """
    Esta es la clase jugador, que contiene todo lo relacionado a nuestro personaje, animaciones, algunas colisiones, actualizacion, dibujado, eventos, etc

    Parametros: una posicion x, una posicion y, la velocidad de movimiento, la gravedad, fuerza de salto, frame_rate, move_rate, y la escala.
    """
    def __init__(self,x,y,velocidad_movimiento,gravedad,fuerza_salto,frame_rate_ms,move_rate_ms,p_scale=1) -> None:
        
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

        self.golpeado = {}
        self.golpeado[DERECHA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Slide ({0}).png",10,False,w=100,h=100)
        self.golpeado[IZQUIERDA] = Auxiliar.getSurfaceFromSeparateFiles(RUTA_IMAGEN + "Characters/robot/Slide ({0}).png",10,True,w=100,h=100)

        self.velocidad_movimiento = {}
        self.velocidad_movimiento[DERECHA] = velocidad_movimiento
        self.velocidad_movimiento[IZQUIERDA] = -velocidad_movimiento

        self.lives = 1
        self.comienzo_vidas = 5
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
        self.esta_golpeado = False
        self.puede_ganar = False
        self.invensible = False
        self.vivo = True
        self.ganar = False

        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
        self.comienzo_salto = self.rectangulo_pies.y

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
        self.municion = 200

        self.move_alloved = {}
        self.move_alloved[IZQUIERDA] = True
        self.move_alloved[DERECHA] = True

    #ACCIONES
    def caminar(self,direccion:int): 
        """
        Este metodo se encarga del movimiento del jugador, le da un valor al movimiento de x

        Parametros: recibe como parametros la direccion de hacia donde mira el personaje
        """
        if self.vivo:
            self.direccion = direccion
            self.esta_caminando = True
            if self.move_alloved[self.direccion]:
                self.move_x = self.velocidad_movimiento[self.direccion]
                if self.esta_saltando:
                    self.move_x = self.velocidad_movimiento[self.direccion] // 2
         
    def parar(self):
        """
        Este metodo se encarga se parar al personaje cuando no esta haciendo ninguna accion
        """
        self.esta_caminando = False
        self.move_x = 0

    def disparar(self,shoot=True):
        """
        Este metodo se encarga del disparo del personaje, crear una bala cuando se usa el boton de disparar y se guarda en una lista de municiones

        Parametros: recibe un booleano que sirve para verificar si el personaje tiene que disparar o no
        """
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
        """
        Este metodo se encarga del ataque cuerpo a cuerpo del personaje

        Parametros: recibe un booleano que sirve para verificar si el personaje tiene que atacar o no
        """
        self.esta_pegando = melee
        if melee:
            self.esta_pegando = True
        
    def saltar(self, jump=True):
        """
        Este metodo se encarga del salto del personaje, le da un valor al movimiento de y

        Parametros: recibe un booleano que sirva para verificar si el personaje tiene que saltar o no
        """
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
        """
        Este metodo se encarga de darle un limite al salto, para que no salte infinitamente
        """
        if self.rectangulo_pies.y < self.comienzo_salto - 150:
            self.esta_saltando = False
 

    def verificar_plataforma(self, tiles,obstaculos,plataformas):
        """
        Este metodo se encarga de verificar todas las plataformas con los pies del personaje, para saber si se aplica la gravedad o no.

        Parametros: recibe una lista de tiles, obstaculos y plataformas que es donde el personaje puede pisar y no caerse
        """
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
        """
        Este metodo se encarga de la gravedad, si no esta sobre una plataforma o saltando, se aplica la gravedad y el personaje cae
        """
        if not self.esta_saltando:
            if not self.sobre_plataforma:
                self.move_y = self.gravedad
                self.esta_cayendo = True
            else:
                self.move_y = 0
                self.esta_cayendo = False

    def actualizar_invensible(self, delta_ms):
        """
        Este metodo se encarga de actualizar al invensibilidad del personaje, dandole un tiempo donde el personaje no recibe da??o

        Parametros: recibe un valor de delta_ms que sirve para controlar cuando tiempo dura la invensibilidad
        """
        if self.invensible:
            self.tiempo_inmune += delta_ms
            if self.tiempo_inmune >= 500:
                self.tiempo_inmune = 0
                self.invensible = False

    def actualizar_bala(self,delta_ms,pantalla):
        """
        Este metodo se encarga de actualizar las balas del personaje, actualiza el tiempo de cooldowwn, dibuja y updatea las balas

        Parametros: recibe un valor delta_ms que se le pasa al update de las balas y la pantalla donde se van a dibujar las balas
        """
        if self.disparo_cooldown > 0:
            self.disparo_cooldown -= 1
        for bala in self.municiones:
            bala.update(delta_ms)
            bala.draw(pantalla)

    def comprobar_vidas(self,sonidos):
        """
        Este metodo se encarga de comprobar las vidas del personaje, y si llegan a cero el personaje pasa a estado muerto

        Parametros: recibe una lista de sonidos, para usarlo cuando recibe un hit
        """
        if self.vidas < 1:
            pygame.mixer.Sound.play(sonidos[3])
            self.vivo = False
    
    #MOVIMIENTO
    def cambiar_x(self,delta_x):
        """
        Este metodo se encarga de cambiar el valor de X para darle movimiento al personaje

        Parametros: recibe como parametro un int que representa los pixeles a mover
        """
        self.rect.x += delta_x
        self.rectangulo_colision.x += delta_x
        self.rectangulo_pies.x += delta_x
        self.rectangulo_cabeza.x += delta_x
        self.rectangulo_derecha.x += delta_x
        self.rectangulo_izquierda.x += delta_x


    def cambiar_y(self,delta_y):
        """
        Este metodo se encarga de cambiar el valor de Y para darle movimiento al personaje

        Parametros: recibe como parametro un int que representa los pixeles a mover
        """
        self.rect.y += delta_y
        self.rectangulo_colision.y += delta_y
        self.rectangulo_pies.y += delta_y
        self.rectangulo_cabeza.y += delta_y
        self.rectangulo_derecha.y += delta_y
        self.rectangulo_izquierda.y += delta_y

    #ANIMACIONES
    def animaciones(self):
        """
        Este metodo se encarga de cambiar las distintas animaciones del personaje
        """
        if self.vivo:
            if not self.invensible:
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
                self.cambiar_animacion(self.golpeado)
        else:
            self.cambiar_animacion(self.muriendo)


    def cambiar_animacion(self, animation):
        """
        Este metodo se encarga de cambiar la animacion actual en caso de ser necesario

        Parametro: recibe como parametro la animacion a verificar
        """
        if self.animacion != animation[DERECHA] and self.animacion != animation[IZQUIERDA]:
            self.frame = 0
        self.animacion = animation[self.direccion]


    def actualizar_frames(self,delta_ms):
        """
        Este metodo se encarga de actualiza los frames de las animaciones

        Parametro: recibe un valor delta_ms que se acumula y ayuda a control el tiempo de la actualizacion
        """
        self.tiempo_transcurrido_animacion += delta_ms
        if self.esta_saltando or self.esta_cayendo:
            if(self.tiempo_transcurrido_animacion >= self.frame_rate_ms + 80):
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

    def draw(self,pantalla):
        """
        Este metodo se encarga de 'dibujar' lo que aparece en pantalla, tambien tiene un modo debug que muestra los rectangulos. 
        Por ultima actualiza la imagen que se va a blitear

        Parametros: recibe como parametro la pantalla que es donde se va a 'dibujar' el objeto
        """
        if(DEBUG):
            pygame.draw.rect(pantalla,color=(255,0 ,0),rect=self.rectangulo_colision)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_pies)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_cabeza)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_derecha)
            pygame.draw.rect(pantalla,color=(255,255,0),rect=self.rectangulo_izquierda)
        
        self.imagen = self.animacion[self.frame]
        pantalla.blit(self.imagen,self.rect)

    def events(self,teclas,eventos,sonidos):
        """
        Este metodo se encarga de verificar todos los eventos del usuario con el juego o la pantalla

        Parametros: recibe como parametros, las teclas presionadas, los eventos ocurridos y una lista de sonidos para usarlos en algunos casos
        """
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
        """
        Este metodo se encarga de todo el movimiento del personaje, usando los distintos tipos de metodos creados anteriormente

        Parametros: recibe como parametros el valor delta_ms que se usa para controlar el tiempo, una lista de tiles,obstaculos y plataformas
        """
        self.tiempo_transcurrido_movimiento += delta_ms
        if(self.tiempo_transcurrido_movimiento >= self.move_rate_ms):
            self.tiempo_transcurrido_movimiento = 0

            self.verificar_plataforma(tiles,obstaculos,plataformas)
            self.aplicar_gravedad()
            self.cambiar_y(self.move_y)
            self.limitar_salto()
            self.cambiar_x(self.move_x)
                

    #ANIMACIONES
    def hacer_animaciones(self,delta_ms):
        """
        Este metodo se encarga de controlar las animaciones usando los metodos relacionados con el mismo creados anteriormente
        """
        self.animaciones()
        self.actualizar_frames(delta_ms)      

    #ACTUALIZACION PRINCIPAL
    def update(self,delta_ms,pantalla,teclas,eventos,tiles,obstaculos,plataformas,sonidos):
        """
        Esta es el metodo principal utilizado para usar todos los metodos principales del objeto jugador y ponerlos en un solo metodo

        Parametros: recibe como parametros el valor delta_ms, pantalla, lista de teclas, eventos, 
        tiles, obstaculos, plataformas y sonidos para pasarlos a los metodo correspondientes
        """
        self.events(teclas,eventos,sonidos)
        self.comprobar_vidas(sonidos)
        self.hacer_movimiento(delta_ms,tiles,obstaculos,plataformas)
        self.hacer_animaciones(delta_ms)
        self.actualizar_invensible(delta_ms)
        self.actualizar_bala(delta_ms,pantalla)
        

    


