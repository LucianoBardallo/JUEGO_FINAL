import pygame
from pygame.locals import *
from configuraciones import *
from nivel import Nivel
from enemigos import Enemigo_Distancia
from gui_widget import Widget
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from sql import insertar_linea


class FormNivel(Form):
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, color_border=None, active=False):
        self.nombre_jugador = "PLAYER"
        self.name = name
        self.nivel_actual = Nivel(self.name,master_surface)
        imagen_background = self.nivel_actual.fondo
        self.ganar = False
        self.perder = False
        self.tiempo_juego = self.nivel_actual.tiempo_juego
        self.jugador = self.nivel_actual.jugador
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.text1 = Button(master=self,x=-100,y=-10,w=1400,h=60,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\bar.png",text=None,font=None,font_size=None,font_color=None)
        self.text2 = Button(master=self,x=550,y=10,w=100,h=30,color_background=None,color_border=None,image_background=None,text="{0}".format(self.tiempo_juego),font="IMPACT",font_size=30,font_color=WHITE)
        self.text3 = Button(master=self,x=1000,y=10,w=200,h=30,color_background=None,color_border=None,image_background=None,text="{0}".format(self.nivel_actual.puntuacion),font="IMPACT",font_size=30,font_color=WHITE)
        self.ima1 = Button(master=self,x=510,y=10,w=30,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Clock_Icon.png",text=None,font=None,font_size=None,font_color=None)
        self.ima2 = Button(master=self,x=50,y=10,w=30,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\HP_Icon.png",text=None,font=None,font_size=None,font_color=None)
        self.ima3 = Button(master=self,x=960,y=10,w=30,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Shop_Cristal_Icon_01.png",text=None,font=None,font_size=None,font_color=None)
        self.pb1 = ProgressBar(master=self,x=100,y=15,w=100,h=20,color_background=None,color_border=None,image_background=None,image_progress=CORAZON,value=self.nivel_actual.jugador.vidas,value_max=5)

        
        self.puntuacion_nivel = 0
        self.lista_widget = [self.text1,self.text2,self.text3,self.pb1,self.ima1,self.ima2,self.ima3]

        
    def resetear(self):
        self.__init__(name = self.name, master_surface = self.master_surface)


    def update(self, lista_eventos, teclas, delta_ms, tiempo, sonidos):
        self.nivel_actual.actualizar(delta_ms,sonidos)
        self.nivel_actual.colisiones(delta_ms,sonidos)
        self.jugador.actualizar(delta_ms,self.nivel_actual.pantalla,teclas,lista_eventos,self.nivel_actual.tiles,self.nivel_actual.obstaculos,self.nivel_actual.plataformas,sonidos)
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("pausa")
                if evento.key == pygame.K_UP:
                    self.ganar = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    self.ganar = False
           
            if evento.type == tiempo:
                self.tiempo_juego -= 1
        

        if self.nivel_actual.jugador.ganar and self.ganar:
            self.set_active("you_win")
            pygame.mixer.Sound.play(sonidos[5])
            if self.name == "nivel_1":
                self.puntuacion_nivel = self.nivel_actual.puntuacion
                insertar_linea(self.nombre_jugador,"nivel_1", self.puntuacion_nivel)
            if self.name == "nivel_2":
                self.puntuacion_nivel = self.nivel_actual.puntuacion
                insertar_linea(self.nombre_jugador,"nivel_2", self.puntuacion_nivel)
            if self.name == "nivel_3":
                self.puntuacion_nivel = self.nivel_actual.puntuacion
                insertar_linea(self.nombre_jugador,"nivel_3", self.puntuacion_nivel)
            if self.name == "nivel_4":
                self.puntuacion_nivel = self.nivel_actual.puntuacion
                insertar_linea(self.nombre_jugador,"nivel_4", self.puntuacion_nivel)

        if not self.jugador.vivo or self.perder:
            self.set_active("you_lose")

        self.pb1.value = self.jugador.vidas
        if self.tiempo_juego >= 0:
            self.text2._text = "{0}".format(self.tiempo_juego)
        else:
            self.perder = True
        self.text3._text = "{0}".format(self.nivel_actual.puntuacion).zfill(8)
   
        
    def draw(self): 
        super().draw()
        self.nivel_actual.renderizar()
        self.nivel_actual.jugador.renderizar(self.nivel_actual.pantalla)
        for obstaculo in self.nivel_actual.obstaculos:
            obstaculo.renderizar(self.nivel_actual.pantalla)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
        


        