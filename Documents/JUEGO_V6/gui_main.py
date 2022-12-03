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

flags = DOUBLEBUF 
PANTALLA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()


form_menu_A = FormMenuA(name="menu",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\menu.jpg",color_border=BLACK,active=True)
form_menu_B = FormMenuB(name="opciones",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\menu.jpg",color_border=BLACK,active=False)
form_menu_C = FormMenuC(name="niveles",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,imagen_background=RUTA_IMAGEN + "Menu\Fondo\Space_Level.jpg",color_border=BLACK,active=False)
form_nivel_1 = FormNivel(name="nivel_1",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
form_nivel_2 = FormNivel(name="nivel_2",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
form_nivel_3 = FormNivel(name="nivel_3",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
form_nivel_4 = FormNivel(name="nivel_4",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
# form_nivel_5 = FormNivel(name="nivel_5",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
# form_nivel_6 = FormNivel(name="nivel_6",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
# form_nivel_7 = FormNivel(name="nivel_7",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
# form_nivel_8 = FormNivel(name="nivel_8",master_surface = PANTALLA,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=BLACK,color_border=BLACK,active=False)
form_menu_pausa = FormMenuPausa(name="pausa",master_surface = PANTALLA,x=500,y=200,w=300,h=300,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
form_menu_pausa_opciones = FormMenuPausaOpciones(name="pausa_opciones",master_surface = PANTALLA,x=500,y=200,w=300,h=300,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
form_win = FormWin(name="you_win",master_surface = PANTALLA,x=500,y=200,w=300,h=430,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)
form_lose = FormLose(name="you_lose",master_surface = PANTALLA,x=500,y=200,w=300,h=230,imagen_background=RUTA_IMAGEN + r"Menu\Button\Window.png",color_background=BLACK,color_border=BLACK,active=False)

timer_1s = pygame.USEREVENT + 0
pygame.time.set_timer(timer_1s,1000)

while True:     
    teclas = pygame.key.get_pressed()
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    

    delta_ms = clock.tick(FPS)

    # lista_form_nivel = [form_nivel_1,form_nivel_2,form_nivel_3,form_nivel_4,form_nivel_5,form_nivel_6,form_nivel_7,form_nivel_8]

    if(form_menu_A.active):
        form_menu_A.update(eventos)
        form_menu_A.draw()

    elif(form_menu_B.active):
        form_menu_B.update(eventos)
        form_menu_B.draw()

    elif(form_menu_C.active):
        form_menu_C.update(eventos)
        form_menu_C.draw()
    
    elif(form_menu_pausa.active):
        form_menu_pausa.update(eventos)
        form_menu_pausa.draw()
    
    elif(form_menu_pausa_opciones.active):
        form_menu_pausa_opciones.update(eventos)
        form_menu_pausa_opciones.draw()

    elif(form_win.active):
        form_win.update(eventos)
        form_win.draw()
    
    elif(form_lose.active):
        form_lose.update(eventos) 
        form_lose.draw()

    elif(form_nivel_1.active):
        form_nivel_1.update(eventos, teclas, delta_ms, timer_1s)
        form_nivel_1.draw()
    
    elif(form_nivel_2.active):
        form_nivel_2.update(eventos, teclas, delta_ms, timer_1s)
        form_nivel_2.draw()
    
    elif(form_nivel_3.active):
        form_nivel_3.update(eventos, teclas, delta_ms, timer_1s)
        form_nivel_3.draw()

    elif(form_nivel_4.active):
        form_nivel_4.update(eventos, teclas, delta_ms, timer_1s)
        form_nivel_4.draw()
    
    # elif(form_nivel_5.active):
    #     form_nivel_5.update(eventos, teclas, delta_ms, timer_1s)
    #     form_nivel_5.draw()
    
    # elif(form_nivel_6.active):
    #     form_nivel_6.update(eventos, teclas, delta_ms, timer_1s)
    #     form_nivel_6.draw()
    
    # elif(form_nivel_7.active):
    #     form_nivel_7.update(eventos, teclas, delta_ms, timer_1s)
    #     form_nivel_7.draw()

    # elif(form_nivel_8.active):
    #     form_nivel_8.update(eventos, teclas, delta_ms, timer_1s)
    #     form_nivel_8.draw()


    # for form in lista_form_nivel:
    #     form.update(eventos, teclas, delta_ms)
    #     form.draw()
    

    pygame.display.flip()




    


  



