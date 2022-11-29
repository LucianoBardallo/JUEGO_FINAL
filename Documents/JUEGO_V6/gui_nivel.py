import pygame
from pygame.locals import *
from configuraciones import *
from nivel import Nivel
from enemigos import Enemigo_Distancia
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormNivel(Form):
    def __init__(self, name, master_surface, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=None, color_border=None, active=False):
        self.name = name
        self.nivel_actual = Nivel(self.name,master_surface)
        imagen_background = self.nivel_actual.fondo
        self.ganar = False
        self.perder = False
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.pb1 = ProgressBar(master=self,x=60,y=60,w=200,h=20,color_background=None,color_border=None,image_background=None,image_progress=CORAZON,value=10,value_max=10)
        self.pb2 = ProgressBar(master=self,x=350,y=60,w=300,h=20,color_background=None,color_border=None,image_background=None,image_progress=BALA,value=15,value_max=15)
        
        self.lista_widget = [self.pb1,self.pb2]

        
    def resetear(self):
        self.__init__(name = self.name, master_surface = self.master_surface)


    def update(self, lista_eventos, teclas, delta_ms):
        self.nivel_actual.actualizar(delta_ms)
        self.nivel_actual.colisiones(delta_ms)
        self.nivel_actual.jugador.actualizar(delta_ms,self.nivel_actual.pantalla,teclas,lista_eventos,self.nivel_actual.tiles)
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("pausa")
                if evento.key == pygame.K_UP:
                    self.ganar = True
                    self.perder = True
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    self.ganar = False
                    self.perder = False


        if self.nivel_actual.jugador.ganar and self.ganar:
            self.set_active("you_win")
        if not self.nivel_actual.jugador.vivo and self.perder:
            self.set_active("you_lose")
        
    def draw(self): 
        super().draw()
        self.nivel_actual.renderizar()
        self.nivel_actual.jugador.renderizar(self.nivel_actual.pantalla)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
        


        