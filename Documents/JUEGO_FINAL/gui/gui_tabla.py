import pygame
from sql import leer_lineas
from gui.gui_widget import Widget
from gui.gui_form import Form
from configuraciones import *


class FormTabla(Form):
    """
    Formulario que muestra los nombre y score de los jugador dependiendo del nivel
    """
    def __init__(self, name, nivel, master_surface, x, y, w, h, color_background, imagen_background, color_border, active):
        super().__init__(name, master_surface, x, y, w, h, color_background, imagen_background, color_border, active)

        self.nivel = nivel
        self.puntuaciones = leer_lineas(self.nivel)
        
        self.boton1 = Widget(master=self,x=ANCHO_VENTANA//2-300,y=100,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[0][1]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton2 = Widget(master=self,x=ANCHO_VENTANA//2-300,y=200,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[1][1]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton3 = Widget(master=self,x=ANCHO_VENTANA//2-300,y=300,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[2][1]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton4 = Widget(master=self,x=ANCHO_VENTANA//2-300,y=400,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[3][1]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton5 = Widget(master=self,x=ANCHO_VENTANA//2-300,y=500,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[4][1]),font="IMPACT",font_size=30,font_color=WHITE)

        self.boton6 = Widget(master=self,x=ANCHO_VENTANA//2+100,y=100,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[0][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton7 = Widget(master=self,x=ANCHO_VENTANA//2+100,y=200,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[1][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton8 = Widget(master=self,x=ANCHO_VENTANA//2+100,y=300,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[2][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton9 = Widget(master=self,x=ANCHO_VENTANA//2+100,y=400,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[3][3]),font="IMPACT",font_size=30,font_color=WHITE)
        self.boton10 = Widget(master=self,x=ANCHO_VENTANA//2+100,y=500,w=300,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table.png",text=" {0} ".format(self.puntuaciones[4][3]),font="IMPACT",font_size=30,font_color=WHITE)

        self.ima1 = Widget(master=self,x=ANCHO_VENTANA//2-500,y=100,w=80,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table_01.png",text=None,font=None,font_size=None,font_color=None)
        self.ima2 = Widget(master=self,x=ANCHO_VENTANA//2-500,y=200,w=80,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table_01.png",text=None,font=None,font_size=None,font_color=None)
        self.ima3 = Widget(master=self,x=ANCHO_VENTANA//2-500,y=300,w=80,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table_01.png",text=None,font=None,font_size=None,font_color=None)
        self.ima4 = Widget(master=self,x=ANCHO_VENTANA//2-500,y=400,w=80,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table_01.png",text=None,font=None,font_size=None,font_color=None)
        self.ima5 = Widget(master=self,x=ANCHO_VENTANA//2-500,y=500,w=80,h=80,color_background=None,color_border=None,image_background=RUTA_IMAGEN + r"Menu\Button\Table_01.png",text=None,font=None,font_size=None,font_color=None)

        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4,self.boton5,self.boton6,self.boton7,self.boton8,self.boton9,self.boton10,self.ima1,self.ima2,self.ima3,self.ima4,self.ima5]
    
    def update(self, lista_eventos):
        self.puntuaciones = leer_lineas(self.nivel)
        self.boton1._text = " {0} ".format(self.puntuaciones[0][1])
        self.boton2._text = " {0} ".format(self.puntuaciones[1][1])
        self.boton3._text = " {0} ".format(self.puntuaciones[2][1])
        self.boton4._text = " {0} ".format(self.puntuaciones[3][1])
        self.boton5._text = " {0} ".format(self.puntuaciones[4][1])
        self.boton6._text = " {0} ".format(self.puntuaciones[0][3])
        self.boton7._text = " {0} ".format(self.puntuaciones[1][3])
        self.boton8._text = " {0} ".format(self.puntuaciones[2][3])
        self.boton9._text = " {0} ".format(self.puntuaciones[3][3])
        self.boton10._text = " {0} ".format(self.puntuaciones[4][3])
        
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

