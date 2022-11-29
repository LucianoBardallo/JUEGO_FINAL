import pygame
from configuraciones import *

class Boton():
	def __init__(self, imagen, pos, texto_entrada, fuente, color_base, color_flotante):
		self.imagen = imagen
		if self.imagen != None:
			self.imagen = pygame.transform.scale(self.imagen,(int(ANCHO_VENTANA * 0.075),int(ALTO_VENTANA * 0.15)))
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.fuente = fuente
		self.color_base, self.color_flotante = color_base, color_flotante
		self.texto_entrada = texto_entrada
		self.texto = self.fuente.render(self.texto_entrada, True, self.color_base)
		if self.imagen is None:
			self.imagen = self.texto
		self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
		self.texto_rect = self.texto.get_rect(center=(self.x_pos, self.y_pos))

	def actualizar(self, screen):
		if self.imagen is not None:
			screen.blit(self.imagen, self.rect)
		screen.blit(self.texto, self.texto_rect)

	def verificar_entrada(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def cambiar_color(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.texto = self.fuente.render(self.texto_entrada, True, self.color_flotante)
		else:
			self.texto = self.fuente.render(self.texto_entrada, True, self.color_base)