from collections import namedtuple

class Move(namedtuple('Move', ['player', 'x', 'y'])):
    def __eq__(self, other):
    	return self.x == other.x and self.y == other.y