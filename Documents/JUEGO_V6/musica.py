import pygame
from configuraciones import *

# AGREGAR MUSICA
class Musica:
    def __init__(self) -> None:
        self.muerte = pygame.mixer.Sound(RUTA_MUSICA + r"muerte_robot.wav")
        self.disparo = pygame.mixer.Sound(RUTA_MUSICA + r"laser_gun.wav")
        self.recolectar = pygame.mixer.Sound(RUTA_MUSICA + r"space_coin.wav")
        self.puerta_activada = pygame.mixer.Sound(RUTA_MUSICA + r"door_activada.wav")
        self.victoria = pygame.mixer.Sound(RUTA_MUSICA + r"victory.wav")
        self.disparo_boss = pygame.mixer.Sound(RUTA_MUSICA + r"BossLaser.wav")
        self.hit = pygame.mixer.Sound(RUTA_MUSICA + r"Impact.wav")
        self.muerte_boss = pygame.mixer.Sound(RUTA_MUSICA + r"boss_death.wav")
        self.muerte_enemigo = pygame.mixer.Sound(RUTA_MUSICA + r"enemy_death.wav")
        self.sonidos = [self.disparo,self.puerta_activada,self.hit,self.muerte,self.recolectar,self.victoria,self.disparo_boss,self.muerte_boss,self.muerte_enemigo]
        for sonido in self.sonidos:
            sonido.set_volume(0.5)

    def play_musica(self):
        pygame.mixer.init()
        pygame.mixer.music.load(RUTA_MUSICA + r"track 1.ogg")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
