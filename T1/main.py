import tree
import move
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
	curr_node = None

	first_five_moves = []

	while g.win is False:
		if who is "1":
			who = "2"

			if first:
				first = False
				second = True
				print('')
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
				if len(first_five_moves) < 5:
					first_five_moves.append(m)
				elif father is None:
					first_five_moves.append(m)
					father = Node(first_five_moves)
					tree = Tree(father)
					curr_node = father
					g.setUtilityValue(father)
					print("ALPHA=")
					print(father.get_alpha())
				else:
					cm = curr_node.get_moves()
					cm.append(m)
					curr_node.add_adj(Node(cm))
					curr_node = get_adjs()[0]
		print(g)

	print("Jogador " + who + " ganhou!")