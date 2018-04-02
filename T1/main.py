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
	while g.win is False:
		if who is "1":
			who = "2"
			if first:
				m = Move(who,x,y)
				node = Node([m])
				tree = Tree(node)
				first = False
				second = True
				g.setIA(tree)
				x = tree.father.get_moves()[1].x
				y = tree.father.get_moves()[1].y
			elif second:
				randomsplays = random.sample(tree.father.get_adjs(), 1)[0]
				smove = randomsplays.get_moves()[len(randomsplays.get_moves())-1]
				x = smove.x
				y = smove.y
				second = False
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


			if g.game_matrix[x][y] is 0:
				g.make_move(who,x,y)
		else:
			who = "1"
			y = int(input())
			x = int(input())
			if g.game_matrix[x][y] is 0:
				g.make_move(who,x,y)
		print(g)

	print("Jogador " + who + " ganhou!")