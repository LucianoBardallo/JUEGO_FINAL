import pygame
from pygame.locals import *
from configuraciones import *
from gui.gui_form import Form
from gui.gui_button import Button
from gui.gui_widget import Widget


class FormNiveles(Form):
    """
    Formulario de la seleccion de nivel
    """
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master=self,x=ANCHO_VENTANA//2-100,y=20,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="NIVELES",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton1 = Button(master=self,x=200,y=350,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_1",text="1",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=625,y=375,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_2",text="2",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=980,y=315,w=100,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_3",text="3",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton4 = Button(master=self,x=100,y=50,w=150,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton_nivel,on_click_param="nivel_4",text="FINAL",font="IMPACT",font_size=30,font_color=WHITE)

        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3,self.boton4]

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("menu")

    def on_click_boton_nivel(self,parametro):
        self.forms_dict[parametro].resetear()
        self.set_active(parametro)
        self.forms_dict["pausa"].cambiar_nivel(parametro)
        self.forms_dict["you_win"].cambiar_nivel(parametro)
        self.forms_dict["you_lose"].cambiar_nivel(parametro)


    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()