from move import Move
import random
import globals

# as arveres somos nozes

class Tree:

	def __init__(self, initialNode):
		self.father = initialNode
		self.current_game_matrix = [[0 for _ in range(15)] for _ in range(15)]
		'''
		centerx = set([4,5,6,7,8,9,10])
		centery = set([4,5,6,7,8,9,10])
		sX = self.father.get_moves()[0].x
		sY = self.father.get_moves()[0].y
		sorroundx = set([sX - 4, sX - 3, sX - 2, sX - 1, sX + 1, sX + 2, sX + 3, sX + 4])
		sorroundy = set([sY - 4, sY - 3, sY - 2, sY - 1, sY + 1, sY + 2, sY + 3, sY + 4])
		interx = centerx & sorroundx
		intery = centery & sorroundy
		x = random.sample(interx,1)[0]
		y = random.sample(intery,1)[0]
		mooove = Move(2, x, y)
		self.father.set_moves([mooove])
		nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
		ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]

		for i in range(0,9):
			try:
				m = Move("2", nx[i], ny[i])
				node = Node(self.father.get_moves() + [m])
				self.father.add_adj(node)
			except:
				pass

		self.father.add_move(mooove)
		print(mooove)
		'''

	def next(self, move):
		print()

class Node:

	def __init__(self, moves=None):
		self.alpha = -1 * float("inf")
		self.beta = float("inf")
		self.adjs = []
		self.father = None
		if moves is None:
			self.moves = []
		else:
			self.moves = moves

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

	def set_adjs(self, adjs):
		self.adjs = adjs
		for adj in adjs:
			adj.set_father(self)

	def set_father(self, father):
		self.father = father

	def add_adj(self, adj):
		self.adjs.append(adj)
		adj.set_father(self)

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
				print(m)
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

		while Move(who, xcurr, ycurr) in list_moves:
			xcurr = xcurr + dirx * path
			ycurr = ycurr + diry * path
			#print(xcurr)
			#print(ycurr)
		if ((Move("1", xcurr, ycurr) not in list_moves) or
			(Move("2", xcurr, ycurr) not in list_moves)) and (xcurr > -1 and xcurr < 15 and ycurr > -1 and ycurr < 15):
			move1 = Move(player, xcurr, ycurr)
			moves.add(move1)
		path = -1

		xcurr = xpenu
		ycurr = ypenu

		while Move(who, xcurr, ycurr) in list_moves:
			xcurr = xcurr + dirx * path
			ycurr = ycurr + diry * path
		if ((Move("1", xcurr, ycurr) not in list_moves) or
			(Move("2", xcurr, ycurr) not in list_moves)) and (xcurr > -1 and xcurr < 15 and ycurr > -1 and ycurr < 15):
			move2 = Move(player, xcurr, ycurr)
			moves.add(move2)

		#
		if len(moves) == 0:

			nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
			ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]

			m = Move(who, random.sample(nx, 1)[0], random.sample(ny, 1)[0])

			moves.add(m)

		return moves

	def __str__(self):
		return self.moves.__str__()
	def depth_search_first(self):
		visited, stack = set(), [self]
		
		while stack:
			vertex = stack.pop()

			if vertex not in visited:
				print(vertex)
				visited.add(vertex)
				stack.extend(set(vertex.get_adjs()) - visited)
		return list(visited)