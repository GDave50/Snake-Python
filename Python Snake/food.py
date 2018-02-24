import pygame
import random
import global_consts as glo

class Food:
	
	__x = 0
	__y = 0
	
	def __init__(self):
		self.new_pos()
	
	# choose a new position for the food
	def new_pos(self):
		x = random.randint(0, glo.GRID_SIZE - 1)
		y = random.randint(0, glo.GRID_SIZE - 1)
		
		self.__x = x
		self.__y = y
	
	# draws the food
	def draw(self, screen):
		pygame.draw.ellipse(screen, glo.FOOD_COLOR,
				[self.__x * glo.SEGMENT_SIZE, self.__y * glo.SEGMENT_SIZE,
				glo.SEGMENT_SIZE, glo.SEGMENT_SIZE], 0)
		pygame.draw.ellipse(screen, glo.FOOD_OUTLINE_COLOR,
				[self.__x * glo.SEGMENT_SIZE, self.__y * glo.SEGMENT_SIZE,
				glo.SEGMENT_SIZE, glo.SEGMENT_SIZE], 2)
	
	# returns the x pos of the food
	def get_x(self):
		return self.__x
	
	# returns the y pos of the food
	def get_y(self):
		return self.__y