import pygame
import global_consts as glo
import snake
import movement_queue
import segment
import food

class Game:
	
	__snake = snake.Snake()
	__movement_queue = movement_queue.Movement_Queue()
	__food = food.Food()
	__growth_queue = 0
	
	def __init__(self):
		pass
	
	# executes the game logic
	# returns True if the game has ended, false otherwise
	def game_logic(self):
		# save a copy of the tail of the snake in case it grows
		snake_tail = self.__snake.get_tail()
		snake_tail_copy = segment.Segment(snake_tail.get_x(),
				snake_tail.get_y(), snake_tail.get_dir())
		
		# update the snake
		self.__snake.move_all()
		self.__snake.update_dirs()
		
		if self.__snake.collides() or self.__snake.out_of_bounds():
			return True
		
		# advance movement queue
		new_head_dir = self.__movement_queue.pop()
		if not new_head_dir == None:
			self.__snake.change_dir(new_head_dir)
		
		snake_head = self.__snake.get_head()
		
		# check if the snake has run into food
		if snake_head.get_x() == self.__food.get_x() and \
				snake_head.get_y() == self.__food.get_y():
			self.__growth_queue += glo.SNAKE_GROWTH_RATE
			self.__food.new_pos()
		
		# grow the snake if the growth queue is not empty
		if self.__growth_queue > 0:
			self.__snake.grow(snake_tail_copy)
			self.__growth_queue -= 1
		
		return False
	
	# adds a new direction to the movement queue
	def change_snake_dir(self, dir):
		self.__movement_queue.add_dir(dir)
	
	# draws the game
	def draw(self, screen):
		self.__food.draw(screen)
		self.__snake.draw(screen)