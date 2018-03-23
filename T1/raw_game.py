from move import Move

class RawGame:

	def __init__(self):
		self.game_matrix = [[0 for _ in range(15)] for _ in range(15)]
		self.duplas1 = set()
		self.triplas1 = set()
		self.quadruplas1 = set()
		self.quintuplas1 = set()
		self.sequencias1 = set()
		self.duplas2 = set()
		self.triplas2 = set()
		self.quadruplas2 = set()
		self.quintuplas2 = set()
		self.sequencias2 = set()
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

		mooove = Move(0, x, y)

		print(mooove)

		if who is "1":
			if mooove not in self.sequencias1:
				print("sequencia")
				self.duplas1.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.duplas1:
				print("dupla")
				self.triplas1.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.triplas1:
				print("tripla")
				self.quadruplas1.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.quadruplas1:
				print("quadrupla")
				self.quintuplas1.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.quintuplas1:
				print("quintupla")
				self.win = True

			self.sequencias1.update(self.get_free_adjacents(mooove.x,mooove.y))

		if who is "2":
			if mooove not in self.sequencias2:
				print("sequencia")
				self.duplas2.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.duplas2:
				print("dupla")
				self.triplas2.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.triplas2:
				print("tripla")
				self.quadruplas2.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.quadruplas2:
				print("quadrupla")
				self.quintuplas2.update(self.get_free_adjacents(mooove.x,mooove.y))

			if mooove in self.quintuplas2:
				print("quintupla")
				self.win = True

			self.sequencias2.update(self.get_free_adjacents(mooove.x,mooove.y))