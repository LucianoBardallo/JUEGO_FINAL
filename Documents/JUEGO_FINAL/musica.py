import pygame
from configuraciones import *

# AGREGAR MUSICA
class Musica:
    """
    Esta clase sirve para cargar todos los sonidos y musica del juego, asi como ponerles un volumen inicial
    """
    def __init__(self) -> None:
        self.muerte = pygame.mixer.Sound(RUTA_MUSICA + r"muerte_robot.wav")
        self.disparo = pygame.mixer.Sound(RUTA_MUSICA + r"laser_gun.wav")
        self.recolectar = pygame.mixer.Sound(RUTA_MUSICA + r"coin.wav")
        self.puerta_activada = pygame.mixer.Sound(RUTA_MUSICA + r"activado.wav")
        self.victoria = pygame.mixer.Sound(RUTA_MUSICA + r"victoria.wav")
        self.disparo_boss = pygame.mixer.Sound(RUTA_MUSICA + r"laser_boss.wav")
        self.hit = pygame.mixer.Sound(RUTA_MUSICA + r"impacto.wav")
        self.muerte_boss = pygame.mixer.Sound(RUTA_MUSICA + r"muerte_boss.wav")
        self.muerte_enemigo = pygame.mixer.Sound(RUTA_MUSICA + r"muerte_enemigo.wav")
        self.sonidos = [self.disparo,self.puerta_activada,self.hit,self.muerte,self.recolectar,self.victoria,self.disparo_boss,self.muerte_boss,self.muerte_enemigo]
        for sonido in self.sonidos:
            sonido.set_volume(0.3)

    def play_musica(self):
        pygame.mixer.init()
        pygame.mixer.music.load(RUTA_MUSICA + r"track 1.ogg")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
