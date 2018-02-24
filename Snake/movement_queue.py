import __init__ as glo

class Movement_Queue:
	
	__slot1 = None
	__slot2 = None
	
	def __init__(self):
		pass
	
	# attempts to add a dir to the movement queue
	# 
	# a movement will be rejected if:
	#	1) the queue is full
	#	2) the movement is invalid compared to the move ahead
	#	   which happens if:
	#		- the move is the same as the move ahead or
	#		- the move opposes the move ahead
	def add_dir(self, dir, head):
		if self.__slot2 is not None:
			return
		
		if dir == head.get_dir():
			return
		
		dir_compare = None
		
		if self.__slot1 is None:
			dir_compare = head.get_dir()
		else: dir_compare = self.__slot1
		
		if dir_compare == glo.Direction.UP:
			if dir == glo.Direction.DOWN: return
		elif dir_compare == glo.Direction.DOWN:
			if dir == glo.Direction.UP: return
		elif dir_compare == glo.Direction.LEFT:
			if dir == glo.Direction.RIGHT: return
		elif dir_compare == glo.Direction.RIGHT:
			if dir == glo.Direction.LEFT: return
		
		if self.__slot1 is None:
			self.__slot1 = dir
		elif self.__slot2 is None:
			self.__slot2 = dir
	
	# get the next movement, if there is one, remove it from
	# the queue and advance the queue
	# 
	# if there are no moves in queue, returns None
	def pop(self):
		dir = self.__slot1
		self.__slot1 = self.__slot2
		self.__slot2 = None
		
		return dir
	
	# clears the queue
	def clear(self):
		self.__slot1 = None
		self.__slot2 = None