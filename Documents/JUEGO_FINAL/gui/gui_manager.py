from pygame.locals import *
from configuraciones import *
from gui.gui_form_menu import FormMenu
from gui.gui_form_opciones import FormOpciones
from gui.gui_form_niveles import FormNiveles
from gui.gui_form_pausa import FormPausa
from gui.gui_form_pausa_opciones import FormPausaOpciones
from gui.gui_nivel import FormNivel
from gui.gui_form_win import FormWin
from gui.gui_form_lose import FormLose
from gui.gui_posiciones import FormPuntuaciones
from gui.gui_tabla import FormTabla


class FormManager():
    """
    Formulario manager que crea los demas formularios, los actualiza y dibuj, asi como tambien se fija cual mostrar en pantalla
    """
    def __init__(self,pantalla) -> None:
        self.pantalla = pantalla
        self.form_menu = FormMenu(name="menu",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\menu.jpg",color_border=BLACK,active=True)
        self.form_opciones = FormOpciones(name="opciones",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\menu.jpg",color_border=BLACK,active=False)
        self.form_niveles = FormNiveles(name="niveles",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\Space_Level.jpg",color_border=BLACK,active=False)
        self.form_nivel_1 = self.crear_nivel("nivel_1")
        self.form_nivel_2 = self.crear_nivel("nivel_2")
        self.form_nivel_3 = self.crear_nivel("nivel_3")
        self.form_nivel_4 = self.crear_nivel("nivel_4")
        self.form_pausa = FormPausa(name="pausa",master_surface = pantalla,x=500,y=200,w=300,h=300,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_pausa_opciones = FormPausaOpciones(name="pausa_opciones",master_surface = pantalla,x=500,y=200,w=300,h=300,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_win = FormWin(name="you_win",master_surface = pantalla,x=500,y=200,w=300,h=230,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_lose = FormLose(name="you_lose",master_surface = pantalla,x=500,y=200,w=300,h=230,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
        self.form_puntuaciones = FormPuntuaciones(name="puntuaciones",master_surface = pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Button\Window_2.png",color_border=BLACK,active=False)
        self.form_tabla1 = self.crear_tabla("tabla_1","nivel_1")
        self.form_tabla2 = self.crear_tabla("tabla_2","nivel_2")
        self.form_tabla3 = self.crear_tabla("tabla_3","nivel_3")
        self.form_tabla4 = self.crear_tabla("tabla_4","nivel_4")
        self.niveles = [self.form_menu,self.form_opciones,self.form_niveles,self.form_nivel_1,self.form_nivel_2,self.form_nivel_3,
            self.form_nivel_4,self.form_pausa,self.form_pausa_opciones,self.form_puntuaciones,self.form_tabla1,self.form_tabla2,self.form_tabla3,self.form_tabla4]

    def crear_nivel(self,nivel):
        return FormNivel(name=nivel,master_surface = self.pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)

    def crear_tabla(self,tabla,nivel):
        return FormTabla(name=tabla,nivel=nivel,master_surface = self.pantalla,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Button\Window_2.png",color_border=BLACK,active=False)

    def actualizar_forms(self,eventos,teclas,delta_ms,timer_1s,sonidos):
        
        if(self.form_menu.active):
            self.form_menu.update(eventos)
            self.form_menu.draw()

        elif(self.form_opciones.active):
            self.form_opciones.update(eventos,sonidos)
            self.form_opciones.draw()

        elif(self.form_niveles.active):
            self.form_niveles.update(eventos)
            self.form_niveles.draw()
        
        elif(self.form_pausa.active):
            self.form_pausa.update(eventos)
            self.form_pausa.draw()
        
        elif(self.form_pausa_opciones.active):
            self.form_pausa_opciones.update(eventos,sonidos)
            self.form_pausa_opciones.draw()

        elif(self.form_win.active):
            self.form_win.update(eventos)
            self.form_win.draw()
            
        elif(self.form_lose.active):
            self.form_lose.update(eventos) 
            self.form_lose.draw()

        elif(self.form_nivel_1.active):
            self.form_nivel_1.nombre_jugador = self.form_opciones.nombre
            self.form_nivel_1.update(eventos, teclas, delta_ms, timer_1s, sonidos)
            self.form_nivel_1.draw()
        
        elif(self.form_nivel_2.active):
            self.form_nivel_2.nombre_jugador = self.form_opciones.nombre
            self.form_nivel_2.update(eventos, teclas, delta_ms, timer_1s, sonidos)
            self.form_nivel_2.draw()
        
        elif(self.form_nivel_3.active):
            self.form_nivel_3.nombre_jugador = self.form_opciones.nombre
            self.form_nivel_3.update(eventos, teclas, delta_ms, timer_1s, sonidos)
            self.form_nivel_3.draw()

        elif(self.form_nivel_4.active):
            self.form_nivel_4.nombre_jugador = self.form_opciones.nombre
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

            

            
            
