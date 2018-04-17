from move import Move

class RawGame:

	def __init__(self):
		self.game_matrix = [[0 for _ in range(15)] for _ in range(15)]
		self.win = False
		self.IA = None

	def setIA(self, IA):
		self.IA = IA
	def __str__(self):
		ret = ""
		for line in self.game_matrix:
			for e in line:
				ret = ret + str(e)
			ret = ret + "\n"
		return ret

	def has_winner(self, lastx, lasty):
		result = self.has_winner_in_direction(lastx, lasty, 1,1)
		result = result or self.has_winner_in_direction(lastx, lasty, 1,0)
		result = result or self.has_winner_in_direction(lastx, lasty, 0,1)
		result = result or self.has_winner_in_direction(lastx, lasty, 1,-1)
		result = result or self.has_winner_in_direction(lastx, lasty, -1,-1)
		result = result or self.has_winner_in_direction(lastx, lasty, -1,0)
		result = result or self.has_winner_in_direction(lastx, lasty, 0,-1)
		result = result or self.has_winner_in_direction(lastx, lasty, -1,1)

		return result


	def has_winner_in_direction(self, x, y, dx, dy):
		who = self.game_matrix[x][y]

		if who is "0":
			return False

		hw = True
		pieces = 1
		for i in range(1, 5):
			try:
				if self.game_matrix[x + i * dx][y + i * dy] is not who:
					break
				else:
					pieces += 1
			except:
				pass
				break
		for i in range(1, 5):
			try:
				if self.game_matrix[x - i * dx][y - i * dy] is not who:
					break
				else:
					pieces += 1
			except:
				pass
				break

		return pieces >= 5

	def make_move(self, who, x, y):
		#print(self.game_matrix[x][y])
		self.game_matrix[x][y] = str(who)

		mooove = Move(who, x, y)

		print(Move(who, y+1, 15-x))

		if self.has_winner(x,y):
			self.win = True