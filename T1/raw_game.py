from move import Move

class RawGame:

	def __init__(self):
		self.game_matrix = [[0 for _ in range(15)] for _ in range(15)]
		self.duplas = set()
		self.triplas = set()
		self.quadruplas = set()
		self.quintuplas = set()
		self.sequencias = set()
		self.win = False
	def __str__(self):
		ret = ""
		for line in self.game_matrix:
			for e in line:
				ret = ret + str(e)
			ret = ret + "\n"
		return ret

	def get_free_adjacents(self, x, y):
		ret = []

		nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
		ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]
		for i in range(0,9):
			try:
				if self.game_matrix[nx[i]][ny[i]] == 0:
					m = Move("0",nx[i], ny[i])
					ret.append(m)
			except:
				pass
		return ret
	def make_move(self, who, x, y):
		#print(self.game_matrix[x][y])
		self.game_matrix[x][y]= str(who)

		mooove = Move(who, x, y)

		if mooove not in self.sequencias:
			self.duplas.update(self.get_free_adjacents(mooove.x,mooove.y))
		if mooove in self.duplas:
			self.duplas.discard(self.get_free_adjacents(mooove.x,mooove.y))
			self.triplas.update(self.get_free_adjacents(mooove.x,mooove.y))

		if mooove in self.triplas:
			self.triplas.discard(self.get_free_adjacents(mooove.x,mooove.y))
			self.quadruplas.update(self.get_free_adjacents(mooove.x,mooove.y))

		if mooove in self.quadruplas:
			self.quadruplas.discard(self.get_free_adjacents(mooove.x,mooove.y))
			self.quintuplas.update(self.get_free_adjacents(mooove.x,mooove.y))

		if mooove in self.quintuplas:
			self.win = True