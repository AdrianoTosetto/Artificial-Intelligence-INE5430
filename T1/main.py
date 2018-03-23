from tree import Node
from move import Move
from random import randint
from raw_game import RawGame

if __name__ == "__main__":

	g = RawGame()
	who = ""
	while g.win is False:
		x = randint(0, 14)
		y = randint(0, 14)
		if g.game_matrix[x][y] is 0:
			if who is "1":
				who = "2"
			else:
				who = "1"
			g.make_move(who,x,y)
			print(g)
			print(g.get_free_adjacents(4,4))
		batata = input()

	print("Jogador " + who + " ganhou!")