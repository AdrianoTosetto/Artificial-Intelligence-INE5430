from move import Move
import random
import globals

# as arveres somos nozes

class Tree:

	def __init__(self, initialNode):
		self.father = initialNode
		self.current_game_matrix = [[0 for _ in range(15)] for _ in range(15)]
		self.father.set_maximizing(False)

class Node:

	def __init__(self, moves=None):
		self.alpha = -1 * float("inf")
		self.beta = float("inf")
		self.adjs = []
		self.father = None
		self.heuristic = -1 * float("inf")
		self.maximizing = None
		if moves is None:
			self.moves = []
		else:
			self.moves = moves

	def is_maximizing(self):
		return self.maximizing
	def set_maximizing(self, max):
		self.maximizing = max

	def get_heuristic(self):
		return self.heuristic
	def set_heuristic(self, value):
		self.heuristic = value

	def get_moves(self):
		return self.moves

	def get_alpha(self):
		return self.alpha
	def get_beta(self):
		return self.beta

	def set_alpha(self, alpha):
		self.alpha = alpha
	def set_beta(self, beta):
		self.beta = beta

	def set_moves(self, moves):
		self.moves = moves

	def add_move(self, move):
		self.moves.append(move)

	def set_father(self, father):
		self.father = father

	def set_adjs(self, adjs):
		self.adjs = adjs
		for adj in adjs:
			adj.set_father(self)
			adj.set_maximizing(not(self.is_maximizing()))

	def add_adj(self, adj):
		self.adjs.append(adj)
		adj.set_father(self)
		adj.set_maximizing(not(self.is_maximizing()))

	def get_adjs(self):
		return self.adjs

	def last_move_adjs(self):
		last_move = self.moves[-1]
		last_last_move = self.moves[-2]
		x = last_move.x
		y = last_move.y
		dirx = x - last_last_move.x
		diry = y - last_last_move.y
		nx = x
		ny = y
		node1 = Node("2", x + dirx, y + diry)
		node2 = Node("2", x + dirx, y + diry)
		while node2.player is "2":
			nx = 0
		nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
		ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]
		ret = []
		for i in range(0,9):
			try:
				m = Move("2", nx[i], ny[i])
				#print(m)
				node = Node(self.get_moves() + [m])
				ret.append(node)
			except:
				pass
		self.set_adjs(ret)
		return ret

	def find_adjacents(self, who, x, y):

		nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
		ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]
		ret = []

		moves = self.get_moves()

		for i in range(0,8):
			m = Move(who, nx[i], ny[i])
			if m in moves:
				ret.append(m)
		return ret

	# possiveis movimentos adjacentes

	def find_moves(self, who, last, penultimate, player):
		list_moves = self.moves
		moves = set()
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

		#print("PATH = 1")
		while Move(who, xcurr, ycurr) in list_moves:
			#print(Move(who, xcurr, ycurr))
			xcurr = xcurr + dirx * path
			ycurr = ycurr + diry * path
			#print(xcurr)
			#print(ycurr)
		if ((Move("1", xcurr, ycurr) not in list_moves) or
			(Move("2", xcurr, ycurr) not in list_moves)) and self.correct_range(xcurr, ycurr):
			move1 = Move(player, xcurr, ycurr)
		#	print(move1)
			moves.add(move1)
		path = -1

		xcurr = xpenu
		ycurr = ypenu

		#print("PATH = -1")
		while Move(who, xcurr, ycurr) in list_moves:
			#print(Move(who, xcurr, ycurr))
			xcurr = xcurr + dirx * path
			ycurr = ycurr + diry * path
		if ((Move("1", xcurr, ycurr) not in list_moves) or
			(Move("2", xcurr, ycurr) not in list_moves)) and self.correct_range(xcurr, ycurr):
			move2 = Move(player, xcurr, ycurr)
			#print(move2)
			moves.add(move2)

		x = last.x
		y = last.y

		if len(moves) == 0:
			#print("eita")
			rand_adj = self.find_adjacents(0, last.x, last.y)
			rand_adj = rand_adj + self.find_adjacents(0, penultimate.x, penultimate.y)
			for m in rand_adj:
				moves.add(Move(player, m.x, m.y))
		#else:
			#print("eita")

		return moves
	#gilui eh um bbk
	def populate(self, levels):
		if levels == 0:
			return
		moves = self.get_moves()
		adnodes = self.get_adjs()
		is_present = False
		who = moves[-2].player

		for m in moves:
			if m.player is "2":
				adjs = self.find_adjacents("2", m.x, m.y)
				for adj in adjs:
					possible_moves2 = self.find_moves("2", m, adj, who)
					for pos in possible_moves2:
						is_present = False
						for adnode in adnodes:
							if moves + [pos] == adnode.get_moves():
								is_present = True
						if not is_present:
							self.add_adj(Node(moves + [pos]))
							self.get_adjs()[-1].populate(levels-1)
			if m.player is "1":
				adjs = self.find_adjacents("1", m.x, m.y)
				for adj in adjs:
					possible_moves1 = self.find_moves("1", m, adj, who)
					for pos in possible_moves1:
						is_present = False
						for adnode in adnodes:
							if moves + [pos] == adnode.get_moves():
								is_present = True
						if not is_present:
							self.add_adj(Node(moves + [pos]))
							self.get_adjs()[-1].populate(levels-1)

		return

	def pruning(self, levels, alpha, beta):
		if levels == 0:
			self.setUtilityValue()
			return self.get_heuristic()
		if self.is_maximizing():
			v = -1 * float("inf")
			for node in self.get_adjs():
				v = max(v, node.pruning(levels-1,alpha,beta))
				alpha = max(v, alpha)
				if beta <= alpha:
					break
			self.set_heuristic(v)
			return v
		else:
			v = float("inf")
			for node in self.get_adjs():
				v = min(v, node.pruning(levels-1,alpha,beta))
				beta = min(v, beta)
				if beta <= alpha:
					break
			self.set_heuristic(v)
			return v

	def __str__(self):
		return self.moves.__str__()
	def depth_search_first(self):
		visited, stack = set(), [self]
		while stack:
			vertex = stack.pop()

			if vertex not in visited:
				#print(vertex)
				visited.add(vertex)
				stack.extend(set(vertex.get_adjs()) - visited)
		return list(visited)

	def correct_range(self, x, y):
		if x < 0 or x > 14 or y > 14 or y < 0:
			return False
		return True

	def emitUValue(self, npieces):
		if npieces == 2:
			return 5
		if npieces == 3:
			return 2500
		if npieces == 4:
			return 1250000
		if npieces == 5:
			return 625000000
		return 1

	def setUtilityValue(self):
		fear_factor = 2500
		already_visited = set()
		utility = 0
		node_moves = self.get_moves()
		for mov in node_moves:
			x = mov.x
			y = mov.y
			player = mov.player
			if player is "1":
				other = "2"
			if player is "2":
				other = "1"
			#print(mov)
			already_visited.add(mov)
			nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
			ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]

			for i in range(0, 8):
				piece_counter = 2
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
						#	print("+valor")
							utility = utility + self.emitUValue(piece_counter)
						elif player == "1":
							#print("-valor")
							utility = utility - self.emitUValue(piece_counter) * 10

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
						#	print("+valor")
							utility = utility + self.emitUValue(piece_counter)# * 500010fear_factor
						elif player == "1":
							#print("-valor")
							utility = utility - self.emitUValue(piece_counter) * fear_factor

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
							#print("+valor")
							utility = utility + self.emitUValue(piece_counter)# * 5000
						elif player == "1":
							#print("-valor")
							utility = utility - self.emitUValue(piece_counter) * fear_factor

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
							#print("+valor")
							utility = utility + self.emitUValue(piece_counter)# * 5000
						elif player == "1":
							#print("-valor")
							utility = utility - self.emitUValue(piece_counter) * fear_factor
			self.set_heuristic(utility)