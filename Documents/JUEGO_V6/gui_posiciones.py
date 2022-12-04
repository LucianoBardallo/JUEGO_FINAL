import pygame
import sys
from pygame.locals import *
from configuraciones import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from sql import leer_lineas

class Puntuaciones(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.boton1 = Button(master=self,x=ANCHO_VENTANA//2-300,y=100,w=600,h=100,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NIVEL 1",font="IMPACT",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="tabla_1")
        self.boton2 = Button(master=self,x=ANCHO_VENTANA//2-300,y=220,w=600,h=100,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NIVEL 2",font="IMPACT",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="tabla_2")
        self.boton3 = Button(master=self,x=ANCHO_VENTANA//2-300,y=340,w=600,h=100,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NIVEL 3",font="IMPACT",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="tabla_3")
        self.boton4 = Button(master=self,x=ANCHO_VENTANA//2-300,y=460,w=600,h=100,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NIVEL 4",font="IMPACT",font_size=30,font_color=WHITE,on_click=self.on_click_boton1,on_click_param="tabla_4")
            

        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("menu")

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
        
class Tabla(Form):
    def __init__(self, name, nivel, master_surface, x, y, w, h, color_background, imagen_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.puntuaciones = leer_lineas(nivel)
        
        self.boton1 = Button(master=self,x=ANCHO_VENTANA//2-300,y=100,w=600,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NAME: {0} SCORE: {1}".format(self.puntuaciones[0][1],self.puntuaciones[0][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=ANCHO_VENTANA//2-300,y=200,w=600,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NAME: {0} SCORE: {1}".format(self.puntuaciones[1][1],self.puntuaciones[1][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=ANCHO_VENTANA//2-300,y=300,w=600,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NAME: {0} SCORE: {1}".format(self.puntuaciones[2][1],self.puntuaciones[2][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton4 = Button(master=self,x=ANCHO_VENTANA//2-300,y=400,w=600,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NAME: {0} SCORE: {1}".format(self.puntuaciones[3][1],self.puntuaciones[3][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton5 = Button(master=self,x=ANCHO_VENTANA//2-300,y=500,w=600,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NAME: {0} SCORE: {1}".format(self.puntuaciones[4][1],self.puntuaciones[4][3]),font="IMPACT",font_size=30,font_color=WHITE)

        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5]
    
    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("puntuaciones")
        
    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()
