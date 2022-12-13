import pygame
from pygame.locals import *
import sys
from configuraciones import *
from gui.gui_manager import FormManager
from musica import Musica

flags = DOUBLEBUF 
PANTALLA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

musica = Musica()
musica.play_musica()


juego = FormManager(PANTALLA)

timer_1s = pygame.USEREVENT + 0
pygame.time.set_timer(timer_1s,1000)

while True:     
    teclas = pygame.key.get_pressed()
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta_ms = clock.tick(FPS)

    juego.actualizar_forms(eventos,teclas,delta_ms,timer_1s,musica.sonidos)

    pygame.display.flip()

    




    


  



