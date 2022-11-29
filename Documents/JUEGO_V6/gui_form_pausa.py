import pygame
import sys
from pygame.locals import *
from configuraciones import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar

class FormMenuPausa(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.boton1 = Button(master=self,x=50,y=75,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton1,on_click_param="nivel_1",text="REANUDAR",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=50,y=150,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton1,on_click_param="pausa_opciones",text="OPCIONES",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=50,y=225,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_reset,on_click_param="menu",text="MENU",font="IMPACT",font_size=30,font_color=WHITE)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_reset(self,parametro):
        self.forms_dict[self.boton1.on_click_param].resetear()
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active(self.boton1.on_click_param)
    
    def cambiar_nivel(self,parametro):
        self.boton1.on_click_param = parametro

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()