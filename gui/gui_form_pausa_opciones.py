import pygame
from pygame.locals import *
from gui.gui_form import Form
from gui.gui_widget import Widget
from gui.gui_button import Button
from gui.gui_progressbar import ProgressBar
from configuraciones import *

class FormPausaOpciones(Form):
    """
    Forrmulario de opciones que esta dentro de pausa
    """
    def __init__(self,name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,imagen_background,color_border,active)

        self.text1 = Widget(master=self,x=100,y=50,w=100,h=40,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="MUSICA",font="IMPACT",font_size=20,font_color=WHITE)
        self.text2 = Widget(master=self,x=100,y=170,w=100,h=40,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text="EFECTOS",font="IMPACT",font_size=20,font_color=WHITE)
        self.pb1 = ProgressBar(master=self,x=50,y=110,w=200,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\bar.png",image_progress=RUTA_IMAGEN + "Menu\Button\Armor_Bar_Dot.png",value=3,value_max=10)
        self.pb2 = ProgressBar(master=self,x=50,y=230,w=200,h=30,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\bar.png",image_progress=RUTA_IMAGEN + "Menu\Button\Armor_Bar_Dot.png",value=3,value_max=10)
        self.boton1 = Button(master=self,x=20,y=120,w=20,h=20,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Backward_BTN.png",on_click=self.on_click_boton1,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.boton2 = Button(master=self,x=20,y=240,w=20,h=20,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Backward_BTN.png",on_click=self.on_click_boton2,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.boton3 = Button(master=self,x=255,y=120,w=20,h=20,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Forward_BTN.png",on_click=self.on_click_boton3,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.boton4 = Button(master=self,x=255,y=240,w=20,h=20,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Forward_BTN.png",on_click=self.on_click_boton4,on_click_param=None,text=None,font=None,font_size=None,font_color=None)
        self.lista_widget = [self.text1,self.text2,self.pb1,self.pb2,self.boton1,self.boton2,self.boton3,self.boton4]

    def on_click_boton1(self, parametro):
        """
        Este metodo se encarga de decrementar el valor del progressbar
        """
        if self.pb1.value > 0:
            self.pb1.value -= 1
    
    def on_click_boton2(self, parametro):
        """
        Este metodo se encarga de decrementar el valor del progressbar
        """
        if self.pb2.value > 0:
            self.pb2.value -= 1
    
    def on_click_boton3(self, parametro):
        """
        Este metodo se encarga de incrementar el valor del progressbar
        """
        if self.pb1.value < self.pb1.value_max:
            self.pb1.value += 1
    
    def on_click_boton4(self, parametro):
        """
        Este metodo se encarga de incrementar el valor del progressbar
        """
        if self.pb2.value < self.pb2.value_max:
            self.pb2.value += 1
        
    def update(self, lista_eventos,sonidos):
        """
        Este metodo se encarga de actualizar y controlar el sonido y los distintos widget

        Parametros: recibe una lista de eventos y sonidos
        """
        pygame.mixer.music.set_volume(self.pb1.value/10)
        for sonido in sonidos:
            sonido.set_volume(self.pb2.value/10)
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)
        for evento in lista_eventos:
             if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    self.set_active("pausa")

    def draw(self): 
        """
        Este metodo se encarga de dibujar los distintos widget en pantalla
        """
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()