from move import Move

class Tree:

	def __init__(self):
		self.nodes = []




class Node:

	def __init__(self, moves=None):
		self.adjs = []
		if moves is None:
			self.moves = []
		else:
			self.moves = moves

	def get_moves(self):
		return self.moves

	def set_adjs(self, adjs):
		self.adjs = adjs
	def get_adjs(self):
		return self.adjs
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