import pygame
import sys
from pygame.locals import *
from configuraciones import *
from gui.gui_form import Form
from gui.gui_widget import Widget
from gui.gui_button import Button

class FormMenu(Form):
    """
    Formulario principal cuando inicia el juego, lleva tanto a opciones, ranking, como a la seleccion de niveles
    """
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.pantalla = master_surface
        self.text1 = Widget(master=self,x=ANCHO_VENTANA//2-200,y=100,w=400,h=100,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="SPACE ADVENTURE",font="IMPACT",font_size=40,font_color=WHITE)
        self.boton1 = Button(master=self,x=ANCHO_VENTANA//2-100,y=260,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton1,on_click_param="niveles",text="JUGAR",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton2 = Button(master=self,x=ANCHO_VENTANA//2-100,y=320,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton1,on_click_param="opciones",text="OPCIONES",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton3 = Button(master=self,x=ANCHO_VENTANA//2-100,y=380,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton1,on_click_param="puntuaciones",text="RANKING",font="IMPACT",font_size=30,font_color=WHITE)
        self.boton4 = Button(master=self,x=ANCHO_VENTANA//2-100,y=440,w=200,h=50,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",on_click=self.on_click_boton2,on_click_param=None,text="SALIR",font="IMPACT",font_size=30,font_color=WHITE)
        
        self.lista_widget = [self.text1,self.boton1,self.boton2,self.boton3,self.boton4]

    def on_click_boton1(self, parametro):
        """
        Este metodo se encarga de obtener un parametro y pasarlo a otro metodo

        Parametro: un str que representa la clave del formulario
        """
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        """
        Este metodo se encarga de cerrar el juego
        """
        pygame.quit()
        sys.exit()

    def update(self, lista_eventos):
        """
        Este metodo se encarga de actualizar el los distintos widget

        Parametros: recibe una lista de eventos
        """
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        """
        Este metodo se encarga de dibujar los distintos widget en pantalla
        """
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()