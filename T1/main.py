from tree import Node
from move import Move
from random import randint
from raw_game import RawGame
from tree import Tree
import random
from layout import GameLayout
from PyQt5.QtWidgets import QApplication
import sys
from threading import Thread


gl = None
def func():
	app = QApplication(sys.argv)
	global gl
	gl = GameLayout()
	sys.exit(app.exec_())


if __name__ == "__main__":
	Thread(target=func).start()
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
	loop_desperate_measure = 0
	curr_node = Node()

	first_five_moves = []

	while g.win is False:
		if who is "1":
			who = "2"
			if loop_desperate_measure >= 100:
				print("A IA se desesperou!")
				x = randint(0,14)
				y = randint(0,14)
				if g.game_matrix[x][y] is 0:
					curr_node.add_adj(Node(curr_node.get_moves() + [Move("2",x,y)]))
					curr_node = curr_node.get_adjs()[-1]
					g.make_move(who,x,y)
					loop_desperate_measure = 0
					g.win = g.has_winner(x,y)
					print(g)
					continue
			if first:
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
					#print("joguei")
					g.make_move(who,x,y)
					gl.make_move(x, y)
					loop_desperate_measure = 0
					first = False
					second = True
				else:
					print("A IA está pensando...")
					loop_desperate_measure += 1
					who="1"
					continue

			elif second:
				x = random.sample(nx,1)[0]
				y = random.sample(ny,1)[0]
				m = Move(who,x,y)
				first_five_moves.append(m)
				if g.game_matrix[x][y] is 0:
					#print("joguei")
					g.make_move(who,x,y)
					gl.make_move(x, y)
					loop_desperate_measure = 0
					second = False
				else:
					print("A IA está pensando...")
					loop_desperate_measure += 1
					who="1"
					continue

			else:
				curr_node.populate(4)
				curr_node.pruning(4, -1 * float("inf"), float("inf"))
				#old_node = curr_node
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
					#print("joguei")
					g.make_move(who,x,y)
					gl.make_move(x, y)
					loop_desperate_measure = 0
				else:
					print("A IA está pensando...")
					loop_desperate_measure += 1
					who="1"
					#curr_node = old_node
					continue

		else:
			if gl is None:
				continue
			if not(gl.canPlay[0]):
				continue
			who = "1"
			print("Faça sua jogada!")
			print("X:")
			y = gl.lastYPlayed[0]
			print("Y:")
			x = gl.lastXPlayed[0]
			m = Move(who, x, y)
			if g.game_matrix[x][y] is 0:
				g.make_move(who,x,y)
				if len(first_five_moves) < 4:
					#print("LENGTH")
					#print(len(first_five_moves))
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
						if nds.get_moves() == cm:
							curr_node = nds
							break
					if curr_node.get_moves() != nds.get_moves():
						next_node = Node(cm)
						curr_node.add_adj(next_node)
						curr_node = curr_node.get_adjs()[-1]
				gl.canPlay[0] = False
			else:
				who = "2"
				continue
		g.win = g.has_winner(x,y)
		print(g)

	print("Jogador " + who + " ganhou!")
