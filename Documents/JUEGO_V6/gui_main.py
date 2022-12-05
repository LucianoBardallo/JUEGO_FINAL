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
from gui_manager import FormManager

flags = DOUBLEBUF 
PANTALLA = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()

# AGREGAR MUSICA
pygame.mixer.init()
pygame.mixer.music.load(RUTA_MUSICA + r"track 1.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
sonido_muerte = pygame.mixer.Sound(RUTA_MUSICA + r"muerte_robot.wav")
sonido_disparo = pygame.mixer.Sound(RUTA_MUSICA + r"laser_gun.wav")
sonido_recolectar = pygame.mixer.Sound(RUTA_MUSICA + r"space_coin.wav")
sonido_puerta_activada = pygame.mixer.Sound(RUTA_MUSICA + r"door_activada.wav")
sonido_puerta_abierta = pygame.mixer.Sound(RUTA_MUSICA + r"door_open.wav")
sonido_victoria = pygame.mixer.Sound(RUTA_MUSICA + r"victory.wav")
sonido_disparo_boss = pygame.mixer.Sound(RUTA_MUSICA + r"BossLaser.wav")
sonido_hit = pygame.mixer.Sound(RUTA_MUSICA + r"Impact.wav")
sonido_muerte_boss = pygame.mixer.Sound(RUTA_MUSICA + r"boss_death.wav")
sonido_muerte_enemigo = pygame.mixer.Sound(RUTA_MUSICA + r"enemy_death.wav")
sonidos = [sonido_disparo,sonido_puerta_activada,sonido_hit,sonido_muerte,sonido_recolectar,sonido_victoria,sonido_disparo_boss,sonido_muerte_boss,sonido_muerte_enemigo]
for sonido in sonidos:
    sonido.set_volume(0.5)

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

    keys = pygame.key.get_pressed()

    delta_ms = clock.tick(FPS)

    juego.actualizar_forms(eventos,teclas,delta_ms,timer_1s,sonidos)


    
    pygame.display.flip()




    


  



