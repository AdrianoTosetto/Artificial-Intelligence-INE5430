from tree import Node
from move import Move
from random import randint
from raw_game import RawGame
from tree import Tree
import random

if __name__ == "__main__":

	g = RawGame()
	who = "2"
	first = True
	second = False
	x = 0
	y = 0
	nx = None
	ny = None
	father = None
	tree = None
	curr_node = Node()

	first_five_moves = []

	while g.win is False:
		if who is "1":
			who = "2"

			if first:
				#print("First")
				centerx = set([4,5,6,7,8,9,10])
				centery = set([4,5,6,7,8,9,10])
				sorroundx = set([x - 4, x - 3, x - 2, x - 1, x + 1, x + 2, x + 3, x + 4])
				sorroundy = set([y - 4, y - 3, y - 2, y - 1, y + 1, y + 2, y + 3, y + 4])
				interx = centerx & sorroundx
				intery = centery & sorroundy
				x = random.sample(interx,1)[0]
				y = random.sample(intery,1)[0]
				m = Move(who, x, y)
				first_five_moves.append(m)
				nx = [x-1, x-1, x-1, x, x, x+1,x+1,x+1]
				ny = [y-1, y, y+1, y-1,y+1, y-1, y, y+1]
				if g.game_matrix[x][y] is 0:
					print("joguei")
					g.make_move(who,x,y)
					first = False
					second = True
				else:
					print("joga logo")
					who="1"
					continue

			elif second:
				#print("Second")
				x = random.sample(nx,1)[0]
				y = random.sample(ny,1)[0]
				m = Move(who,x,y)
				first_five_moves.append(m)
				if g.game_matrix[x][y] is 0:
					print("joguei")
					g.make_move(who,x,y)
					second = False
				else:
					print("joga logo")
					who="1"
					continue

			else:
				#print("pau no cu do first")
				curr_node.populate(2)
				curr_node.pruning(2, -1 * float("inf"), float("inf"))
				chosen_nodes = curr_node.get_adjs()
				min_v = -1 * float("inf")
				possible_nodes = []
				for cadj in chosen_nodes:
					if cadj.get_heuristic() == min_v:
						possible_nodes = possible_nodes + [cadj]
					if cadj.get_heuristic() > min_v:
						min_v = cadj.get_heuristic()
						possible_nodes = [cadj]
				chosen_node = random.sample(possible_nodes,1)[0]
				curr_node = chosen_node
				x = curr_node.get_moves()[-1].x
				y = curr_node.get_moves()[-1].y
				if g.game_matrix[x][y] is 0:
					print("joguei")
					g.make_move(who,x,y)
				else:
					print("joga logo")
					who="1"
					continue

		else:
			who = "1"
			print("Faca sua jogada!")
			print("X:")
			y = int(input()) - 1
			print("Y:")
			x = int(input()) - 1
			m = Move(who, x, y)
			if g.game_matrix[x][y] is 0:
				g.make_move(who,x,y)
				if len(first_five_moves) < 4:
					first_five_moves.append(m)
				elif father is None:
					first_five_moves.append(m)
					father = Node(first_five_moves)
					tree = Tree(father)
					curr_node = father
					father.setUtilityValue()
				else:
					cm = curr_node.get_moves()
					cm.append(m)
					next_node = None
					old_curr = curr_node
					for nds in curr_node.get_adjs():
						next_node = nds
						if nds.get_moves()[-1] == m:
							curr_node = nds
							break
					if old_curr == curr_node:
						next_node = Node(cm)
						curr_node.add_adj(next_node)
						curr_node = next_node
			else:
				who = "2"
				continue		
		g.win = g.has_winner(x,y)
		print(g)

	print("Jogador " + who + " ganhou!")