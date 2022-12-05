import pygame
from pygame.locals import *
import sys
from configuraciones import *
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC
from gui_form_pausa import FormMenuPausa
from gui_form_pausa_opciones import FormMenuPausaOpciones
from gui_nivel import FormNivel
from gui_form_win import FormWin
from gui_form_lose import FormLose
from gui_posiciones import *




class FormManager():
    def __init__(self,pantalla) -> None:
        self.form_menu_A = FormMenuA(name="menu",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\menu.jpg",color_border=BLACK,active=True)
        self.form_menu_B = FormMenuB(name="opciones",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\menu.jpg",color_border=BLACK,active=False)
        self.form_menu_C = FormMenuC(name="niveles",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\Space_Level.jpg",color_border=BLACK,active=False)
        self.form_nivel_1 = FormNivel(name="nivel_1",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
        self.form_nivel_2 = FormNivel(name="nivel_2",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
        self.form_nivel_3 = FormNivel(name="nivel_3",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
        self.form_nivel_4 = FormNivel(name="nivel_4",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
        self.form_menu_pausa = FormMenuPausa(name="pausa",master_surface = pantalla,x=500,y=200,w=300,h=300,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_menu_pausa_opciones = FormMenuPausaOpciones(name="pausa_opciones",master_surface = pantalla,x=500,y=200,w=300,h=300,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_win = FormWin(name="you_win",master_surface = pantalla,x=500,y=200,w=300,h=230,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_lose = FormLose(name="you_lose",master_surface = pantalla,x=500,y=200,w=300,h=230,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_puntuaciones = Puntuaciones(name="puntuaciones",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Button\Window_2.png",color_border=BLACK,active=False)
        self.form_tabla1 = Tabla(name="tabla_1",nivel="nivel_1",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Button\Window_2.png",color_border=BLACK,active=False)
        self.form_tabla2 = Tabla(name="tabla_2",nivel="nivel_2",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Button\Window_2.png",color_border=BLACK,active=False)
        self.form_tabla3 = Tabla(name="tabla_3",nivel="nivel_3",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Button\Window_2.png",color_border=BLACK,active=False)
        self.form_tabla4 = Tabla(name="tabla_4",nivel="nivel_4",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Button\Window_2.png",color_border=BLACK,active=False)
        

    def actualizar_forms(self,eventos,teclas,delta_ms,timer_1s,sonidos):
        if(self.form_menu_A.active):
            self.form_menu_A.update(eventos)
            self.form_menu_A.draw()

        elif(self.form_menu_B.active):
            self.form_menu_B.update(eventos,sonidos)
            self.form_menu_B.draw()

        elif(self.form_menu_C.active):
            self.form_menu_C.update(eventos)
            self.form_menu_C.draw()
        
        elif(self.form_menu_pausa.active):
            self.form_menu_pausa.update(eventos)
            self.form_menu_pausa.draw()
        
        elif(self.form_menu_pausa_opciones.active):
            self.form_menu_pausa_opciones.update(eventos,sonidos)
            self.form_menu_pausa_opciones.draw()

        elif(self.form_win.active):
            self.form_win.update(eventos)
            self.form_win.draw()
            
        elif(self.form_lose.active):
            self.form_lose.update(eventos) 
            self.form_lose.draw()

        elif(self.form_nivel_1.active):
            self.form_nivel_1.nombre_jugador = self.form_menu_B.nombre
            self.form_nivel_1.update(eventos, teclas, delta_ms, timer_1s, sonidos)
            self.form_nivel_1.draw()
        
        elif(self.form_nivel_2.active):
            self.form_nivel_2.nombre_jugador = self.form_menu_B.nombre
            self.form_nivel_2.update(eventos, teclas, delta_ms, timer_1s, sonidos)
            self.form_nivel_2.draw()
        
        elif(self.form_nivel_3.active):
            self.form_nivel_3.nombre_jugador = self.form_menu_B.nombre
            self.form_nivel_3.update(eventos, teclas, delta_ms, timer_1s, sonidos)
            self.form_nivel_3.draw()

        elif(self.form_nivel_4.active):
            self.form_nivel_4.nombre_jugador = self.form_menu_B.nombre
            self.form_nivel_4.update(eventos, teclas, delta_ms, timer_1s, sonidos)
            self.form_nivel_4.draw()
        
        elif(self.form_puntuaciones.active):
            self.form_puntuaciones.update(eventos)
            self.form_puntuaciones.draw()
        
        elif(self.form_tabla1.active):
            self.form_tabla1.update(eventos)
            self.form_tabla1.draw()
        
        elif(self.form_tabla2.active):
            self.form_tabla2.update(eventos)
            self.form_tabla2.draw()
        
        elif(self.form_tabla3.active):
            self.form_tabla3.update(eventos)
            self.form_tabla3.draw()
        
        elif(self.form_tabla4.active):
            self.form_tabla4.update(eventos)
            self.form_tabla4.draw()

            

            
            
