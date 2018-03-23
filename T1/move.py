class Move:
	def __init__(self, player, x, y):
		self.player = player
		self.x = x
		self.y = y

	def get_move(self):
		return (self.x, self.y)

	def __str__(self):
		return "[" + str(self.x) + "," + str(self.y) + "]"

	def __repr__(self):
		return self.__str__()		