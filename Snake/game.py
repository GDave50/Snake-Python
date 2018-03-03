import pygame
import __init__ as glo
import snake
import movement_queue
import segment
import food

class Game:
	
	__snake = snake.Snake()
	__movement_queue = movement_queue.Movement_Queue()
	__food = food.Food(__snake)
	__growth_queue = 0
	
	def __init__(self):
		pass
	
	# executes the game logic
	# returns True if the game has ended, False otherwise
	def game_logic(self):
		# save a copy of the tail of the snake in case it grows
		snake_tail = self.__snake.get_tail()
		snake_tail_copy = segment.Segment(snake_tail.get_x(),
				snake_tail.get_y(), snake_tail.get_dir())
		
		# update the snake
		self.__snake.move_all()
		self.__snake.update_dirs()
		
		if self.__snake.collides() or self.__snake.out_of_bounds():
			glo.DIE_SOUND.play()
			return True
		
		# advance movement queue
		new_head_dir = self.__movement_queue.pop()
		if new_head_dir is not None:
			self.__snake.change_dir(new_head_dir)
		
		snake_head = self.__snake.get_head()
		
		# check if the snake has run into food
		if snake_head.get_x() == self.__food.get_x() and \
				snake_head.get_y() == self.__food.get_y():
			self.__growth_queue += glo.SNAKE_GROWTH_RATE
			self.__food.new_pos(self.__snake)
			glo.EAT_SOUND.play()
		
		# grow the snake if the growth queue is not empty
		if self.__growth_queue > 0:
			self.__snake.grow(snake_tail_copy)
			self.__growth_queue -= 1
		
		return False
	
	# adds a new direction to the movement queue
	def change_snake_dir(self, dir):
		self.__movement_queue.add_dir(dir, self.__snake.get_head())
	
	# resets the game
	def reset(self):
		self.__snake.reset()
		self.__movement_queue.clear()
		self.__growth_queue = 0
	
	# draws the game
	def draw(self, screen):
		# render score
		score_str = str(self.__snake.get_length())
		text_width, text_height = glo.FONT.size(score_str)
		draw_x = glo.WINDOW_SIZE / 2 - text_width / 2
		draw_y = glo.WINDOW_SIZE / 2 - text_height / 2
		screen.blit(glo.FONT.render(score_str, False, (255,255,255)),
			(draw_x, draw_y))
		
		self.__food.draw(screen)
		self.__snake.draw(screen)