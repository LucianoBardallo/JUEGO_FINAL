import pygame
from pygame.locals import *
from gui_form import Form
from gui_textbox import TextBox
from gui_button import Button
from gui_progressbar import *
from configuraciones import *

class FormMenuB(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = TextBox(master=self,x=ANCHO_VENTANA//2-100,y=130,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="MUSICA",font="IMPACT",font_size=40,font_color=WHITE)
        self.pb1 = ProgressBar(master=self,x=ANCHO_VENTANA//2-200,y=200,w=400,h=35,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\bar.png",image_progress=RUTA_IMAGEN + "Menu\Button\Armor_Bar_Dot.png",value=5,value_max=10)
        self.text2 = TextBox(master=self,x=ANCHO_VENTANA//2-100,y=280,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="EFECTOS",font="IMPACT",font_size=40,font_color=WHITE)
        self.pb2 = ProgressBar(master=self,x=ANCHO_VENTANA//2-200,y=350,w=400,h=35,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\bar.png",image_progress=RUTA_IMAGEN + "Menu\Button\Armor_Bar_Dot.png",value=5,value_max=10)
        self.boton1 = Button(master=self,x=100,y=500,w=150,h=35,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton1,on_click_param="menu",text="VOLVER",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=ANCHO_VENTANA//2-300,y=200,w=50,h=35,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Backward_BTN.png",on_click=self.on_click_boton2,on_click_param="menu",text=None,font=None,font_size=None,font_color=None)
        self.boton3 = Button(master=self,x=ANCHO_VENTANA//2-300,y=350,w=50,h=35,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Backward_BTN.png",on_click=self.on_click_boton3,on_click_param="menu",text=None,font=None,font_size=None,font_color=None)
        self.boton4 = Button(master=self,x=ANCHO_VENTANA//2+250,y=200,w=50,h=35,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Forward_BTN.png",on_click=self.on_click_boton4,on_click_param="menu",text=None,font=None,font_size=None,font_color=None)
        self.boton5 = Button(master=self,x=ANCHO_VENTANA//2+250,y=350,w=50,h=35,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Forward_BTN.png",on_click=self.on_click_boton5,on_click_param="menu",text=None,font=None,font_size=None,font_color=None)
        self.lista_widget = [self.text1,self.text2,self.pb1,self.pb2,self.boton1,self.boton2,self.boton3,self.boton4,self.boton5]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        if self.pb1.value > 0:
            self.pb1.value -= 1
    
    def on_click_boton3(self, parametro):
        if self.pb2.value > 0:
            self.pb2.value -= 1
    
    def on_click_boton4(self, parametro):
        if self.pb1.value < self.pb1.value_max:
            self.pb1.value += 1
    
    def on_click_boton5(self, parametro):
        if self.pb2.value < self.pb2.value_max:
            self.pb2.value += 1
        
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("menu")

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()