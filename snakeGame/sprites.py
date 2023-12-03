import pygame as pg
from pygame.math import Vector2 as vec
import random 
import numpy as np
from settings import *



class Snake(pg.sprite.Sprite):
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.game = game

		
		#self.image = pg.Surface((10,10))
		#self.image.fill(COLORS["WHITE"])
		#self.rect = self.image.get_rect()
	
		cx, cy = SCREEN_CENTER
		self.body = [vec(cx, cy), vec(cx - 10, cy), vec(cx - 20, cy)]
		self.chosen_direction = vec(1, 0)
		self.going_direction = vec(1, 0)
		self.vel = 10



	def update(self):
		#self.vel += self.acc
		self.get_direction()
	
			
		
			

	def get_direction(self):
		keys = pg.key.get_pressed()
		if keys[pg.K_a] and self.going_direction != DIRECTIONS["right"]:
			self.chosen_direction = DIRECTIONS["left"]
		if keys[pg.K_d] and self.going_direction != DIRECTIONS["left"]:
			self.chosen_direction = DIRECTIONS["right"]
		if keys[pg.K_w] and self.going_direction != DIRECTIONS["down"]:
			self.chosen_direction = DIRECTIONS["up"]
		if keys[pg.K_s] and self.going_direction != DIRECTIONS["up"]:
			self.chosen_direction = DIRECTIONS["down"]
	
	

class Food(pg.sprite.Sprite):
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		self.game = game
		
		self.image = pg.Surface((10,10))
		self.image.fill(COLORS["CYAN"])
		self.rect = self.image.get_rect()

		self.pos = 0

		self.set_location()
		

	def set_location(self):
		pos_x = random.randrange(SCREEN_SIZE[0]//10)*10
		pos_y = random.randrange(SCREEN_SIZE[1]//10)*10
		self.pos = vec(pos_x, pos_y)
		self.rect.topleft = self.pos

	




		
			