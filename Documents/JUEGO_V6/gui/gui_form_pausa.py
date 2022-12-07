import pygame
from pygame.locals import *
from configuraciones import *
from gui.gui_form import Form
from gui.gui_button import Button
from gui.gui_widget import Widget

class FormPausa(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master=self,x=100,y=50,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="PAUSA",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=50,y=130,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Replay_BTN.png",on_click=self.on_click_reset,on_click_param="nivel_1",text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=180,y=130,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Settings_BTN.png",on_click=self.on_click_boton1,on_click_param="pausa_opciones",text=None,font=None,font_size=None,font_color=None)
        self.boton3 = Button(master=self,x=50,y=210,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Menu_BTN.png",on_click=self.on_click_boton1,on_click_param="menu",text=None,font=None,font_size=None,font_color=None)
        self.boton4 = Button(master=self,x=180,y=210,w=70,h=70,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Hangar_BTN.png",on_click=self.on_click_boton1,on_click_param="niveles",text=None)
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.text1]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_reset(self,parametro):
        self.forms_dict[self.boton1.on_click_param].resetear()
        self.set_active(parametro)
    
    def cambiar_nivel(self,parametro):
        self.boton1.on_click_param = parametro

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active(self.boton1.on_click_param)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()