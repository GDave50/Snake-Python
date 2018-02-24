import global_consts as glo

class Movement_Queue:
	
	__slot1 = None
	__slot2 = None
	
	def __init__(self):
		pass
	
	def add_dir(self, dir):
		if self.__slot1 == None:
			self.__slot1 = dir
		elif self.__slot2 == None:
			self.__slot2 = dir
	
	def pop(self):
		dir = self.__slot1
		self.__slot1 = self.__slot2
		self.__slot2 = None
		
		return dir