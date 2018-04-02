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
		self.IA = None

		self.utility = 0

	def setIA(self, IA):
		self.IA = IA
	def __str__(self):
		ret = ""
		for line in self.game_matrix:
			for e in line:
				ret = ret + str(e)
			ret = ret + "\n"
		return ret

	def get_free_adjacents(self, x, y, who):
		ret = []

		nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
		ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]
		for i in range(0,9):
			try:
				if self.game_matrix[nx[i]][ny[i]] == 0:
					m = Move(who,nx[i], ny[i])
					ret.append(m)
			except:
				pass
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
		for i in range(1, 5):
			try:
				if self.game_matrix[x + i * dx][y + i * dy] is not who:
					hw = False
					break
			except:
				hw = False
				pass
				break
		self.utility = 20
		return hw

	def make_move(self, who, x, y):
		#print(self.game_matrix[x][y])
		self.game_matrix[x][y] = str(who)

		mooove = Move(who, x, y)

		print(mooove)

		if self.has_winner(x,y):
			self.win = True

	def find_moves(self, who, last, penultimate):
		moves = []
		xlast = last.x
		ylast = last.y

		xpenu = penultimate.x
		ypenu = penultimate.y

		dirx = xlast - xpenu
		diry = ylast - ypenu
		if dirx < -1:
			dirx = -1
		if dirx > 1:
			dirx = 1
		if diry < -1:
			diry = -1
		if diry > 1:
			diry = 1

		path = 1

		xcurr = xlast
		ycurr = ylast

		while self.game_matrix[xcurr][ycurr] is who:
			xcurr = xcurr + dirx * path
			ycurr = ycurr + diry * path
			#print(xcurr)
			#print(ycurr)
		if self.game_matrix[xcurr][ycurr] is 0:
			move1 = Move("1", xcurr, ycurr)
			moves = moves + [move1]
		path = -1

		xcurr = xpenu
		ycurr = ypenu

		while self.game_matrix[xcurr][ycurr] is who:
			xcurr = xcurr + dirx * path
			ycurr = ycurr + diry * path
		if self.game_matrix[xcurr][ycurr] is 0:
			move2 = Move("1", xcurr, ycurr)
			moves = moves + [move2]

		return moves

	def correct_range(self, x, y):
		if x < 0 or x > 14 or y > 14 or y < 0:
			return False
		return True

	def emitUValue(npieces):
		if npieces == 2:
			return 1
		if npieces == 3:
			return 3
		if npieces == 4:
			return 5
		if npieces == 5:
			return 20
	def setUtilityValue(self, node):
		already_visited = set()
		utility = 0
		node_moves = node.get_moves()
		for mov in node_moves:
			x = mov.x
			y = mov.y
			player = mov.player
			if player is "1":
				other = "2"
			if player is "2":
				other = "1"
			already_visited.add(mov)
			nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
			ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]

			piece_counter = 2

			for i in range(0, 9):
				m = Move(player, nx[i], ny[i])

				if m in node_moves:
					dirx = mov.x - nx[i]
					diry = mov.y - ny[i]

					# caso 1
					m1_1 = Move(player, mov.x + 3*dirx, mov.y + 3*diry)
					m2_1 = Move(player, mov.x + 2*dirx, mov.y + 2*diry)
					m3_1 = Move(player, mov.x + dirx, mov.y + diry)

					m1_1_o = Move(other, mov.x + 3*dirx, mov.y + 3*diry)
					m2_1_o = Move(other, mov.x + 2*dirx, mov.y + 2*diry)
					m3_1_o = Move(other, mov.x + dirx, mov.y + diry)

					if m1_1 in node_moves:
						piece_counter = piece_counter + 1
					if m2_1 in node_moves:
						piece_counter = piece_counter + 1
					if m3_1 in node_moves:
						piece_counter = piece_counter + 1

					if ((self.correct_range(m1_1.x, m1_1.y) and
						self.correct_range(m2_1.x, m2_1.y) and
						self.correct_range(m3_1.x, m3_1.y)) and
						not (m1_1 in already_visited or
						m2_1 in already_visited or
						m3_1 in already_visited or
						m1_1_o in node_moves or
						m2_1_o in node_moves or
						m3_1_o in node_moves)):
						if player == "2":
							utility = utility + emitUValue(piece_counter)
						if player == "1":
							utility = utility - emitUValue(piece_counter)

					piece_counter = 2

					#caso 2
					m1_2 = m2_1
					m2_2 = m3_1
					m3_2 = Move(player, nx[i] - dirx, ny[i] - diry)

					m1_2_o = m2_1_o
					m2_2_o = m3_1_o
					m3_2_o = Move(other, nx[i] - dirx, ny[i] - diry)

					if m1_2 in node_moves:
						piece_counter = piece_counter + 1
					if m2_2 in node_moves:
						piece_counter = piece_counter + 1
					if m3_2 in node_moves:
						piece_counter = piece_counter + 1

					if ((self.correct_range(m1_2.x, m1_2.y) and
						self.correct_range(m2_2.x, m2_2.y) and
						self.correct_range(m3_2.x, m3_2.y)) and
						not (m1_2 in already_visited or
						m2_2 in already_visited or
						m3_2 in already_visited or
						m1_2_o in node_moves or
						m2_2_o in node_moves or
						m3_2_o in node_moves)):
						if player == "2":
							utility = utility + emitUValue(piece_counter)
						if player == "1":
							utility = utility - emitUValue(piece_counter)

					piece_counter = 2
					#caso 3
					m1_3 = m2_2
					m2_3 = m3_2
					m3_3 = Move(player, nx[i] - 2*dirx, ny[i] - 2*diry)

					m1_3_o = m2_2_o
					m2_3_o = m3_2_o
					m3_3_o = Move(other, nx[i] - 2*dirx, ny[i] - 2*diry)

					if m1_3 in node_moves:
						piece_counter = piece_counter + 1
					if m2_3 in node_moves:
						piece_counter = piece_counter + 1
					if m3_3 in node_moves:
						piece_counter = piece_counter + 1

					if ((self.correct_range(m1_3.x, m1_3.y) and
						self.correct_range(m2_3.x, m2_3.y) and
						self.correct_range(m3_3.x, m3_3.y)) and
						not (m1_3 in already_visited or
						m2_3 in already_visited or
						m3_3 in already_visited or
						m1_3_o in node_moves or
						m2_3_o in node_moves or
						m3_3_o in node_moves)):
						if player == "2":
							utility = utility + emitUValue(piece_counter)
						if player == "1":
							utility = utility - emitUValue(piece_counter)

					piece_counter = 2

					#caso 4

					m1_4 = m2_3
					m2_4 = m3_3
					m3_4 = Move(player, nx[i] - 3*dirx, ny[i] - 3*diry)

					m1_4_o = m2_3_o
					m2_4_o = m3_3_o
					m3_4_o = Move(other, nx[i] - 3*dirx, ny[i] - 3*diry)

					if m1_4 in node_moves:
						piece_counter = piece_counter + 1
					if m2_4 in node_moves:
						piece_counter = piece_counter + 1
					if m3_4 in node_moves:
						piece_counter = piece_counter + 1

					if ((self.correct_range(m1_4.x, m1_4.y) and
						self.correct_range(m2_4.x, m2_4.y) and
						self.correct_range(m3_4.x, m3_4.y)) and
						not (m1_4 in already_visited or
						m2_4 in already_visited or
						m3_4 in already_visited or
						m1_4_o in node_moves or
						m2_4_o in node_moves or
						m3_4_o in node_moves)):
						if player == "2":
							utility = utility + emitUValue(piece_counter)
						if player == "1":
							utility = utility - emitUValue(piece_counter)
		if node.get_alpha() < utility:
			node.set_alpha(utility)