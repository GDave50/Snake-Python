import global_consts as glo
import segment

class Snake:
	
	__segs = []
	
	def __init__(self):
		self.__segs.clear()
		
		# create 5 segments to start
		for i in range(glo.SNAKE_GROWTH_RATE):
			self.__segs.append(segment.Segment(-i, 0, glo.Direction.RIGHT))
	
	# make the dir of all segs to be the dir of the seg ahead of it.
	# this is what makes the snake follow itself
	def update_dirs(self):
		for i in reversed(range(1, len(self.__segs))):
			self.__segs[i].set_dir(self.__segs[i-1].get_dir())
	
	# moves all the segs in the snake based on their direction
	def move_all(self):
		for seg in self.__segs:
			seg.move()
	
	# changes the dir of the head of the snake
	def change_dir(self, dir):
		self.__segs[0].set_dir(dir)
	
	# add a segment to the tail of the snake
	def grow(self, seg):
		self.__segs.append(seg)
	
	# determines if the snake has collided with itself
	def collides(self):
		for i in range(1, len(self.__segs)):
			if self.__segs[0].get_x() == self.__segs[i].get_x() and \
					self.__segs[0].get_y() == self.__segs[i].get_y():
				return True
		
		return False
	
	# determines if the snake is out of bounds
	def out_of_bounds(self):
		return self.__segs[0].get_x() < 0 or \
				self.__segs[0].get_y() < 0 or \
				self.__segs[0].get_x() >= glo.GRID_SIZE or \
				self.__segs[0].get_y() >= glo.GRID_SIZE
	
	# determines if the given grid spot is occupied by the snake
	def grid_spot_occupied(self, x ,y):
		for seg in self.__segs:
			if seg.get_x() == x and seg.get_y() == y:
				return True
	
	# resets the snake
	def reset(self):
		self.__init__()
	
	# draw the snake
	def draw(self, screen):
		for seg in self.__segs:
			seg.draw(screen)
	
	# returns the length of the snake
	def get_length(self):
		return len(self.__segs)
	
	# returns the head of the snake
	def get_head(self):
		return self.__segs[0]
	
	# returns the tail of the snake
	def get_tail(self):
		return self.__segs[len(self.__segs) - 1]