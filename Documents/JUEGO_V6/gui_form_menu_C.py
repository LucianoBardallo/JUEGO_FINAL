import pygame
import sys
from pygame.locals import *
from configuraciones import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar

class FormMenuC(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = TextBox(master=self,x=ANCHO_VENTANA//2-100,y=20,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NIVELES",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=140,y=150,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_1",text="1",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=410,y=150,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_2",text="2",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=690,y=150,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_3",text="3",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton4 = Button(master=self,x=975,y=150,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_4",text="4",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton5 = Button(master=self,x=140,y=400,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_5",text="5",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton6 = Button(master=self,x=410,y=400,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_6",text="6",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton7 = Button(master=self,x=690,y=400,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_7",text="7",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton8 = Button(master=self,x=975,y=400,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_8",text="8",font="IMPACT",font_size=30,font_color=WHITE)

        
        
        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3,self.boton4,self.boton5,self.boton6,self.boton7,self.boton8]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("menu")

    def on_click_boton_nivel(self,parametro):
        self.set_active(parametro)
        self.forms_dict["pausa"].cambiar_nivel(parametro)
        self.forms_dict["you_win"].cambiar_nivel(parametro)
        self.forms_dict["you_lose"].cambiar_nivel(parametro)


    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()