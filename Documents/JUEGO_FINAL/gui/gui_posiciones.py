import pygame
from pygame.locals import *
from configuraciones import *
from gui.gui_form import Form
from gui.gui_button import Button
from gui.gui_widget import Widget
from sql import leer_lineas


class FormPuntuaciones(Form):
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
        
