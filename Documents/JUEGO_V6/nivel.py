import pygame
from auxiliar import *
from configuraciones import *
from plataformas import *
from objetos import *
from botínes import *
from enemigos import *
from jugador import *

class Nivel:
    def __init__(self,nivel,pantalla):
        self.nivel_data = Auxiliar.cargar_nivel(r"C:\Users\lucia\Documents\JUEGO_V6\niveles.json",nivel)
        self.mapa = self.nivel_data["mapa"]
        self.objetos_data = self.nivel_data["objetos"]
        self.enemigos_data = self.nivel_data["enemigos"]
        self.jugador_data = self.nivel_data["jugador"]
        self.fondo = self.nivel_data["fondo"]
        self.tiles = self.crear_mapa()
        self.loot = self.crear_loot()
        self.objetos = self.crear_objetos()
        self.obstaculos = self.crear_obstaculos()
        self.enemigos = self.crear_enemigos()
        self.jugador = self.crear_jugador()
        self.pantalla = pantalla
        self.nivel = [self.tiles,self.loot,self.objetos,self.enemigos,self.obstaculos,self.jugador.municiones]

        self.tiempo_activado = 0
        
        
    def crear_jugador(self):
        for coordenadas in self.jugador_data["coordenadas"]:
            x = coordenadas[0]
            y = coordenadas[1]
            jugador = Jugador(x,y, velocidad_movimiento = 8, gravedad = 8, fuerza_salto = 8, frame_rate_ms = 40,frame_rate_jump_ms = 120, move_rate_ms = 20, altura_salto = 180, p_scale=0.2)
            return jugador


    def crear_mapa(self):
        tiles = []
        x = 0
        y = 0
        for fila in self.mapa:
            for tile in fila:
                if tile == PLATAFORMA:
                    tiles.append(Plataforma(x,y,ancho=50,alto=50,tipo=1))
                elif tile == MURO:
                    tiles.append(Muro(x,y,ancho=50,alto=50,tipo=4))
                elif tile == CAJA:
                    tiles.append(Objeto_Estatico(x,y,ancho=50,alto=50,tipo_desbloqueado=2))
                x += 50

            x = 0
            y += 50
        return tiles

    def crear_loot(self):
        loot = []
        x = 0
        y = 0
        for fila in self.mapa:
            for tile in fila:
                if tile == LOOT:
                    loot.append(Botín(x,y,frame_rate_ms=60))
                x += 50
            x = 0
            y += 50
        return loot

    def crear_enemigos(self):
        enemigos = []
        for enemigo in self.enemigos_data:
            for i in range(enemigo["cantidad"]):
                for coordenada in enemigo["coordenadas"]:
                    x = coordenada[0]
                    y = coordenada[1]
                    patrulla = coordenada[2]
                    if enemigo["nombre"] == "soldado":
                        enemigos.append(Enemigo_Melee(x,y,velocidad_movimiento=4,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=patrulla))
                    elif enemigo["nombre"] == "artillero":
                        enemigos.append(Enemigo_Distancia(x,y,velocidad_movimiento=0,gravedad=10,frame_rate_ms=20,move_rate_ms=20,patrulla=patrulla))
        return enemigos
           
    def crear_objetos(self):
        objetos = []
        for objeto in self.objetos_data:
            for i in range(objeto["cantidad"]):
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

    def crear_obstaculos(self):
        obstaculos = []
        x = 0
        y = 0
        for fila in self.mapa:
            for tile in fila:
                if tile == PINCHO:
                    obstaculos.append(Objeto(x,y,ancho=50,alto=50,tipo_desbloqueado=0))
                x += 50
            x = 0
            y += 50
        return obstaculos

    def colisiones(self,delta_ms):
        #MUROS
        for tile in self.tiles:
            for bala in self.jugador.municiones:
                if bala.rectangulo_colision.colliderect(tile.rectangulo_colision):
                    self.jugador.municiones.remove(bala)
            if type(tile) == Muro:
                if tile.rectangulo_colision.colliderect(self.jugador.rectangulo_derecha):
                    self.jugador.cambiar_x(-3)
                elif tile.rectangulo_colision.colliderect(self.jugador.rectangulo_izquierda):
                    self.jugador.cambiar_x(3)
                elif tile.rectangulo_colision.colliderect(self.jugador.rectangulo_cabeza):
                    self.jugador.comienzo_salto = ALTO_VENTANA
                elif tile.rectangulo_colision.colliderect(self.jugador.rectangulo_pies):
                    self.jugador.sobre_plataforma = True
            if type(tile) == Objeto:
                if tile.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                    if not self.jugador.invensible:
                        self.jugador.vidas -= 1
                        self.jugador.invensible = True
                
        #ENEMIGOS
        for enemigo in self.enemigos:
            if enemigo.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                if not self.jugador.invensible:
                    self.jugador.vidas -= 1
                    self.jugador.invensible = True
            for bala in self.jugador.municiones:
                if bala.rectangulo_colision.colliderect(enemigo.rectangulo_colision):
                    enemigo.vidas -= 1
                    self.jugador.municiones.remove(bala)
            if type(enemigo) == Enemigo_Distancia:                
                for bala in enemigo.municiones:
                    if bala.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                        if not self.jugador.invensible:
                            self.jugador.vidas -= 1
                            self.jugador.invensible = True
                            enemigo.municiones.remove(bala)
            if not enemigo.vivo:
                self.enemigos.remove(enemigo)


        #BOTÍN
        for loot in self.loot:
            if loot.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                loot.recolectado = True
                self.jugador.puntuacion += 50
                self.loot.remove(loot)

        #OBJETOS   
        for objeto in self.objetos:
            if objeto.nombre == "interruptor":
                if objeto.rectangulo_colision.colliderect(self.jugador.rectangulo_colision):
                    objeto.activado = True
                    objeto.desbloqueado = True
                    self.jugador.puede_ganar = True
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
   

    def renderizar(self):
        for lista in self.nivel:
            for elemento in lista:
                elemento.renderizar(self.pantalla)
        for enemigo in self.enemigos:
            if enemigo == Enemigo_Distancia:
                enemigo.municiones.renderizar(self.pantalla)
        
                
    
    def actualizar(self,delta_ms):
        for lista in self.nivel:
            for elemento in lista:
                if type(elemento) == Enemigo_Melee:
                    elemento.actualizar(delta_ms,self.tiles,self.jugador.municiones)
                elif type(elemento) == Enemigo_Distancia:
                    elemento.actualizar(self.pantalla,delta_ms,self.tiles,self.jugador.rectangulo_colision)
                elif type(elemento) == Botín:
                    elemento.actualizar(delta_ms)
                    
                
                

    # def actualizar_nivel(self,delta_ms):
    #     self.actualizar(delta_ms)
    #     self.colisiones(delta_ms)
        # self.jugador.actualizar(delta_ms,self.pantalla,teclas,eventos,self.tiles)

    