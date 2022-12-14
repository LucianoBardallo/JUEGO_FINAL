import pygame
from auxiliar import *
from configuraciones import *
from plataformas import *
from objetos import *
from loot import *
from enemigos import *
from jugador import *
from obstaculos import *
from boss import Boss

class Nivel:
    """
    Esta clase es la del nivel manager, aca se crea todo lo relacionado al nivel, se actualiza, se dibuja y se verifican las colisiones

    Parametros: recibe como parametro el nivel que es la clave para saber a que parte del json acceder y la pantalla principal donde se va a mostrar el juego
    """
    def __init__(self,nivel,pantalla):
        self.nivel_data = Auxiliar.cargar_nivel(r"C:\Users\lucia\Documents\JUEGO_FINAL\niveles.json",nivel)
        self.fondo = self.nivel_data["fondo"]
        self.mapa = self.nivel_data["mapa"]
        self.objetos_data = self.nivel_data["objetos"]
        self.enemigos_data = self.nivel_data["enemigos"]
        self.jugador_data = self.nivel_data["jugador"]
        self.plataformas_data = self.nivel_data["plataformas"]
        self.obstaculos_data = self.nivel_data["obstaculos"]
        self.tiempo_juego = self.nivel_data["tiempo"]
        self.tiles = self.crear_mapa()
        self.plataformas = self.crear_plataformas_mobiles()
        self.loot = self.crear_loot()
        self.objetos = self.crear_objetos()
        self.obstaculos = self.crear_obstaculos()
        self.obstaculos2 = self.crear_obstaculos2()
        self.enemigos = self.crear_enemigos()
        self.jugador = self.crear_jugador()
        self.pantalla = pantalla
        self.nivel = [self.obstaculos2,self.tiles,self.loot,self.objetos,self.enemigos,self.jugador.municiones,self.plataformas]

        self.tiempo_activado = 0
        self.puntuacion = 0
        
    def crear_jugador(self):
        """
        Este metodo se encarga de crear al jugador principal

        Retorna: el jugador tipo objeto
        """
        for coordenadas in self.jugador_data["coordenadas"]:
            x = coordenadas[0]
            y = coordenadas[1]
            jugador = Jugador(x,y, velocidad_movimiento = 8, gravedad = 8, fuerza_salto = 8, frame_rate_ms = 40, move_rate_ms = 20, p_scale=0.2)
            return jugador


    def crear_mapa(self):
        """
        Este metodo se encarga de crear todo lo que sea tiles y objetos estaticos del nivel

        Retorna: una lista con todos los tiles
        """
        tiles = []
        x = 0
        y = 50
        for fila in self.mapa:
            for tile in fila:
                if tile == PLATAFORMA:
                    tiles.append(Plataforma(x,y,ancho=50,alto=50,tipo=1))
                elif tile == MURO:
                    tiles.append(Muro(x,y,ancho=50,alto=50,tipo=4))
                elif tile == CAJA:
                    tiles.append(Objeto_Estatico(x,y,ancho=50,alto=50,tipo_desbloqueado=2))
                elif tile == PISO:
                    tiles.append(Muro(x,y,ancho=50,alto=50,tipo=1))
                x += 50

            x = 0
            y += 50
        return tiles
    
    def crear_plataformas_mobiles(self):
        """
        Este metodo se encarga de crear todas las plataformas mobiles

        Retorna: una lista con las plataformas mobiles
        """
        plataformas = []
        for plataforma in self.plataformas_data:
            for coordenada in plataforma["coordenadas"]:
                x = coordenada[0]
                y = coordenada[1]
                punto_inicio = coordenada[2]
                punto_final = coordenada[3]
                if plataforma["nombre"] == "horizontal":
                    plataformas.append(Platforma_Mobiles(x,y,ancho=50,alto=50,tipo=14,velocidad=4,move_rate_ms=20,punto_inicio=punto_inicio,punto_final=punto_final,direccion="horizontal"))
                elif plataforma["nombre"] == "vertical":
                    plataformas.append(Platforma_Mobiles(x,y,ancho=50,alto=50,tipo=14,velocidad=4,move_rate_ms=20,punto_inicio=punto_inicio,punto_final=punto_final,direccion="vertical"))
        return plataformas

    def crear_obstaculos(self):
        """
        Este metodo se encarga de crear los obstaculos ya sean pinchos o acido

        Retorna: una lista de con los obstaculos
        """
        obstaculos = []
        x = 0
        y = 50
        for fila in self.mapa:
            for tile in fila:
                if tile == FONDO_ACIDO:
                    obstaculos.append(Obstaculo(x,y,ancho=50,alto=50,tipo=1))
                elif tile == TOP_ACIDO:
                    obstaculos.append(Obstaculo(x,y,ancho=50,alto=50,tipo=0))
                elif tile == PINCHO:
                    obstaculos.append(Obstaculo_Pincho(x,y,ancho=50,alto=50,tipo=0))
                x += 50

            x = 0
            y += 50
        return obstaculos
    
    def crear_obstaculos2(self):
        """
        Este metodo se encarga de crear obstaculos tipo sierra que tienen animacion

        Retorna: una lista de obstaculos sierra
        """
        obstaculos2 = []
        for obstaculo in self.obstaculos_data:
            for coordenada in obstaculo["coordenadas"]:
                x = coordenada[0]
                y = coordenada[1]
                if obstaculo["nombre"] == "sierra":
                    obstaculos2.append(Obstaculo_sierra(x,y,ancho=50,alto=50,tipo=0))
        return obstaculos2


    def crear_loot(self):
        """
        Este metodo se encarga de crear todos los objetos recolectables del nivel

        Retorna: una lista de objetos recolectables
        """
        loot = []
        x = 0
        y = 50
        for fila in self.mapa:
            for tile in fila:
                if tile == LOOT:
                    loot.append(Bot??n(x,y,frame_rate_ms=60))
                x += 50
            x = 0
            y += 50
        return loot

    def crear_enemigos(self):
        """
        Este metodo se encarga de crear todos los enemigos del nivel

        Retorna: una lista de enemigos
        """
        enemigos = []
        for enemigo in self.enemigos_data:
            for coordenada in enemigo["coordenadas"]:
                x = coordenada[0]
                y = coordenada[1]
                patrulla = coordenada[2]
                if enemigo["nombre"] == "soldado":
                    enemigos.append(Enemigo_Melee(x,y,velocidad_movimiento=4,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=patrulla))
                elif enemigo["nombre"] == "artillero_l":
                    enemigos.append(Enemigo_Distancia(x,y,velocidad_movimiento=0,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=patrulla,direccion=IZQUIERDA))
                elif enemigo["nombre"] == "artillero_r":
                    enemigos.append(Enemigo_Distancia(x,y,velocidad_movimiento=0,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=patrulla,direccion=DERECHA))
                elif enemigo["nombre"] == "boss":
                    enemigos.append(Boss(x,y,frame_rate_ms=120))
        return enemigos
           
    def crear_objetos(self):
        """
        Este metodo se encarga de crear todos los objetos que tienen diferentes estados del nivel

        Retorna: una lista de objetos animados
        """
        objetos = []
        for objeto in self.objetos_data:
            for coordenada in objeto["coordenadas"]:
                x = coordenada[0]
                y = coordenada[1]
                if objeto["nombre"] == "inicio":
                    objetos.append(Objeto_Animado("inicio",x,y,ancho=80,alto=120,tipo_desbloqueado=6,tipo_abierto=4,tipo_bloqueado=5))
                if objeto["nombre"] == "interruptor":
                    objetos.append(Objeto_Animado("interruptor",x,y,ancho=25,alto=75,tipo_desbloqueado=8,tipo_abierto=7,tipo_bloqueado=8))
                elif objeto["nombre"] == "final":
                    objetos.append(Objeto_Animado("final",x,y,ancho=80,alto=120,tipo_desbloqueado=6,tipo_abierto=4,tipo_bloqueado=5))
        return objetos

    def colisiones(self,delta_ms,sonidos):
        """
        Este metodo se encarga de verificar todas las coliciones del nivel
        """
        #MUROS
        self.jugador.move_alloved[IZQUIERDA] = True
        self.jugador.move_alloved[DERECHA] = True
        for tile in self.tiles:
            for bala in self.jugador.municiones:
                if bala.rectangulo_colision.colliderect(tile.rectangulo_colision):
                    self.jugador.municiones.remove(bala)
            if type(tile) == Muro:
                if tile.rectangulo_colision.colliderect(self.jugador.rectangulo_derecha):
                    self.jugador.move_alloved[DERECHA] = False
                    self.jugador.move_x = 0
                elif tile.rectangulo_colision.colliderect(self.jugador.rectangulo_izquierda):
                    self.jugador.move_alloved[IZQUIERDA] = False
                    self.jugador.move_x = 0
                if tile.rectangulo_colision.colliderect(self.jugador.rectangulo_cabeza):
                    self.jugador.comienzo_salto = ALTO_VENTANA
            if type(tile) == Objeto:
                if tile.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                    if not self.jugador.invensible:
                        self.jugador.vidas -= 1
                        pygame.mixer.Sound.play(sonidos[2])
                        self.jugador.invensible = True
        
        #OBSTACULO
        for obstaculo in self.obstaculos:
            if type(obstaculo) == Obstaculo:
                if obstaculo.rectangulo_pies.colliderect(self.jugador.rectangulo_colision):
                    if not self.jugador.invensible:
                        self.jugador.vidas -= 5
                        self.jugador.invensible = True
            if type(obstaculo) == Obstaculo_Pincho:
                if obstaculo.rectangulo_pies.colliderect(self.jugador.rectangulo_colision):
                    if not self.jugador.invensible:
                        self.jugador.vidas -= 1
                        pygame.mixer.Sound.play(sonidos[2])
                        self.jugador.invensible = True
        for obstaculo2 in self.obstaculos2:
            if obstaculo2.rectangulo_pies.colliderect(self.jugador.rectangulo_colision):
                if not self.jugador.invensible:
                    self.jugador.vidas -=1
                    pygame.mixer.Sound.play(sonidos[2])
                    self.jugador.invensible = True
            
                
        #ENEMIGOS
        for enemigo in self.enemigos:
            if not enemigo.vivo:
                if type(enemigo) == Boss:
                    self.puntuacion += 2000
                else:
                    self.puntuacion += 200
                self.enemigos.remove(enemigo)
            else:
                if type(enemigo) != Boss:
                    if enemigo.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                        if not self.jugador.invensible:
                            self.jugador.vidas -= 1
                            pygame.mixer.Sound.play(sonidos[2])
                            self.jugador.invensible = True
                for bala in self.jugador.municiones:
                    if type(enemigo) == Boss:
                        if bala.rectangulo_colision.colliderect(enemigo.rect_ojo):
                            enemigo.hp -= 200
                            self.jugador.municiones.remove(bala)
                    else:
                        if bala.rectangulo_colision.colliderect(enemigo.rectangulo_colision):
                            enemigo.vidas -= 1
                            pygame.mixer.Sound.play(sonidos[2])
                            self.jugador.municiones.remove(bala)
                if type(enemigo) == Enemigo_Distancia or type(enemigo) == Boss:                
                    for bala in enemigo.municiones:
                        if bala.rect.colliderect(self.jugador.rectangulo_colision):
                            if not self.jugador.invensible:
                                self.jugador.vidas -= 1
                                pygame.mixer.Sound.play(sonidos[2])
                                self.jugador.invensible = True
                                enemigo.municiones.remove(bala)
            
                

        #BOT??N
        for loot in self.loot:
            if loot.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                loot.recolectado = True
                self.puntuacion += 50
                pygame.mixer.Sound.play(sonidos[4])
                self.loot.remove(loot)

        #OBJETOS   
        for objeto in self.objetos:
            if objeto.nombre == "interruptor":
                if objeto.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                    objeto.activado = True
                    objeto.desbloqueado = True
                    self.jugador.puede_ganar = True
                    pygame.mixer.Sound.play(sonidos[1])
                else:
                    if objeto.activado:
                        self.tiempo_activado += delta_ms
                    if(self.tiempo_activado >= 10000):
                        objeto.activado = False
                        objeto.desbloqueado = False
                        self.jugador.puede_ganar = False
                        self.tiempo_activado = 0

            elif objeto.nombre == "final":
                objeto.desbloqueado = self.jugador.puede_ganar
                objeto.activado = False
                if objeto.rectangulo_colision.colliderect(self.jugador.rectangulo_colision) and self.jugador.puede_ganar:
                    objeto.activado = True
                    self.jugador.ganar = True
   

    def draw(self):
        """
        Este metodo se encarga de 'dibujar' lo que aparece en pantalla. En este todos los elementos que componen el nivel
        Tambien se encarga de dibujar las balas de los enemigos
        """
        for lista in self.nivel:
            for elemento in lista:
                elemento.draw(self.pantalla)
                if type(elemento) == Enemigo_Distancia or type(elemento) == Boss:
                    for bala in elemento.municiones:
                        bala.draw(self.pantalla)
        
                
    
    def update(self,delta_ms,sonidos):
        """
        Este metodo se encarga de actualizar todos los elementos del nivel, usando todos los metodos update
        """
        for lista in self.nivel:
            for elemento in lista:
                if type(elemento) == Enemigo_Melee:
                    elemento.update(delta_ms,self.tiles,sonidos,self.plataformas)
                elif type(elemento) == Enemigo_Distancia:
                    elemento.update(self.pantalla,delta_ms,self.tiles,self.jugador.rectangulo_colision,sonidos,self.plataformas)
                elif type(elemento) == Boss:
                    elemento.update(delta_ms,self.pantalla,self.jugador.rectangulo_colision,sonidos)
                elif type(elemento) == Bot??n or type(elemento) == Platforma_Mobiles or type(elemento) == Obstaculo_sierra:
                    elemento.update(delta_ms)
                
                    
                

    