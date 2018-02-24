import pygame
import global_consts as glo

class Segment:
	
	__x = 0
	__y = 0
	__dir = None
	
	def __init__(self, x, y, dir):
		self.__x = x
		self.__y = y
		self.__dir = dir
	
	# move the seg based on its dir
	def move(self):
		if self.__dir == glo.Direction.UP:
			self.__y -= 1
		elif self.__dir == glo.Direction.DOWN:
			self.__y += 1
		elif self.__dir == glo.Direction.LEFT:
			self.__x -= 1
		elif self.__dir == glo.Direction.RIGHT:
			self.__x += 1
	
	# draws the segment
	def draw(self, screen):
		pygame.draw.ellipse(screen, glo.SEGMENT_COLOR,
				[self.__x * glo.SEGMENT_SIZE, self.__y * glo.SEGMENT_SIZE,
				glo.SEGMENT_SIZE, glo.SEGMENT_SIZE], 0)
		pygame.draw.ellipse(screen, glo.SEGMENT_OUTLINE_COLOR,
				[self.__x * glo.SEGMENT_SIZE, self.__y * glo.SEGMENT_SIZE,
				glo.SEGMENT_SIZE, glo.SEGMENT_SIZE], 2)
	
	# set the dir of the segment
	def set_dir(self, dir):
		self.__dir = dir
	
	# returns the x pos of the seg
	def get_x(self):
		return self.__x
	
	# returns the y pos of the seg
	def get_y(self):
		return self.__y
	
	# returns the dir of the seg
	def get_dir(self):
		return self.__dir