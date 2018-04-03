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

	levels = 0

	while g.win is False:
		if who is "1":
			who = "2"

			if first:
				first = False
				second = True
				#print('')
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

			elif second:
				second = False
				x = random.sample(nx,1)[0]
				y = random.sample(ny,1)[0]
				m = Move(who,x,y)
				first_five_moves.append(m)

			else:
				possible_moves = set()
				possible_moves1 = set()
				adnodes1 = curr_node.get_adjs()
				for adnode1 in adnodes1:
					mvs = adnode1.get_moves()
					for m in mvs:
						alpha1 = 0
						if m.player is "2":
							adjs = adnode1.find_adjacents("2", m.x, m.y)
							for adj in adjs:
								possible_moves = possible_moves | adnode1.find_moves("2", m, adj, "1")
						if m.player is "1":
							adjs = adnode1.find_adjacents("1", m.x, m.y)
							for adj in adjs:
								possible_moves = possible_moves | adnode1.find_moves("1", m, adj, "1")
					for l in possible_moves:
						adnode1.add_adj(Node(mvs + [l]))
						levels+=1
					adnodes2 = adnode1.get_adjs()

					for adnode2 in adnodes2:
						alpha2 = 0
						mvs1 = adnode2.get_moves()
						for m in mvs1:
							if m.player is "2":
								adjs = adnode2.find_adjacents("2", m.x, m.y)
								for adj in adjs:
									possible_moves1 = possible_moves1 | adnode2.find_moves("2", m, adj, "2")
							if m.player is "1":
								adjs = adnode2.find_adjacents("1", m.x, m.y)
								for adj in adjs:
									possible_moves1 = possible_moves1 | adnode2.find_moves("1", m, adj, "2")
						for l in possible_moves1:
							adnode1.add_adj(Node(mvs1 + [l]))
							levels+=1
						adnodes3 = adnode2.get_adjs()
						for adnode3 in adnodes3:
							g.setUtilityValue(adnode3)
							alpha2 += adnode3.get_alpha()
						adnode2.set_alpha(alpha2)
						alpha1 += adnode2.get_alpha()
					adnode1.set_alpha(alpha1)
				chosen_nodes = curr_node.get_adjs()
				print(len(chosen_nodes))
				chosen_node = chosen_nodes[0]
				for cadj in chosen_nodes:
					if cadj.get_alpha() > chosen_node.get_alpha():
						chosen_node = cadj

				curr_node = chosen_node
				levels = levels - 1
				actual_move = curr_node.get_moves()[-1]
				x = actual_move.x
				y = actual_move.y


			'''
			else:
				
				last_move   = randomsplays.get_moves()[-1]
				penultimate = randomsplays.get_moves()[-2]
				print(randomsplays.get_moves())

				moves = g.find_moves(who, last_move, penultimate)
				if len(moves) == 0:
					print("vish")
					rmove = random.sample(g.get_free_adjacents(last_move.x, last_move.y, who),1)[0]
					adjs3 = Node(randomsplays.get_moves() + [rmove])
					randomsplays.add_adj(adjs3)
				else:
					adjs1 = Node(randomsplays.get_moves() + [moves[0]])
					randomsplays.add_adj(adjs1)
					try:
						adjs2 = Node(randomsplays.get_moves() + [moves[1]])
						randomsplays.add_adj(adjs2)
					except:
						pass
				randomsplays = random.sample(randomsplays.get_adjs(), 1)[0]
				smove = randomsplays.get_moves()[len(randomsplays.get_moves())-1]
				x = smove.x
				y = smove.y
			'''
				


			if g.game_matrix[x][y] is 0:
				g.make_move(who,x,y)
		else:
			who = "1"
			y = int(input())
			x = int(input())
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
					g.setUtilityValue(father)
					print("ALPHA=")
					print(father.get_alpha())

					possible_moves = set()
					mvs = curr_node.get_moves()
					for m in mvs:
						if m.player is "2":
							adjs = curr_node.find_adjacents("2", m.x, m.y)
							for adj in adjs:
								possible_moves = possible_moves | curr_node.find_moves("2", m, adj, "2")
						if m.player is "1":
							adjs = curr_node.find_adjacents("1", m.x, m.y)
							for adj in adjs:
								possible_moves = possible_moves | curr_node.find_moves("1", m, adj, "2")
					for l in possible_moves:
						father.add_adj(Node(first_five_moves + [l]))
						levels=1
				else:
					cm = curr_node.get_moves()
					cm.append(m)
					curr_node.add_adj(Node(cm))
					curr_node = curr_node.get_adjs()[0]
		g.win = g.has_winner(x,y)
		print(g)

	print("Jogador " + who + " ganhou!")