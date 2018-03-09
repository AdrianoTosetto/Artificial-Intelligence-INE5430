import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
from random import randint


#1 computador
#2 investidor em bitcoins | otaku
class Connect4:
	def __init__(self):
		self.stack1 = [0] * 7
		self.stack2 = [0] * 7
		self.stack3 = [0] * 7
		self.stack4 = [0] * 7
		self.stack5 = [0] * 7
		self.stack6 = [0] * 7
		self.stack7 = [0] * 7
		self.list = [
			self.stack1,
			self.stack2,
			self.stack3,
			self.stack4,
			self.stack5,
			self.stack6,
			self.stack7,
		]
	def get_input(self):
		col = int(input())
		i = 6
		while self.list[col][i] != 0:
			i = i - 1
		self.list[col][i] = 2
	def col_full(self):
		for cell in list[col]:
			if cell == 0:
				return False
		return True
	def make_move(self, col, who):
		i = 6
		while self.list[col][i] != 0:
			i = i - 1
		if i == -1:
			return False
		if(who == 0):
			self.list[col][i] = 1
		else:
			self.list[col][i] = 2
		return True

	def make_random_move(self):
		next = randint(0,6)

		while not(self.make_move(next, 0)):
			next = randint(0,6)
		return next

	def find_good_row(self):
		i = 0
		curr_counter = 0
		old_counter = 0
		better_row = 0
		temp = ""
		while i < 7:
			for s in (self.list):
				temp += str(s[i]) + " "
				if(s[i] == 1):
					curr_counter += 1
				if(s[i] == 2):
					curr_counter = 0
					continue
			if(curr_counter >= old_counter):
				old_counter = curr_counter
				better_row = i
			i = i + 1
			print(temp)
			temp = ""
		print('better row = ' + str(better_row))
	def __str__(self):
		i = 0
		ret = ""
		while i < 7:
			for s in (self.list):
				ret = ret + str(s[i]) + ' '
			i = i + 1
			ret = ret + ('\n')
		return ret


class Window:
	def __init__(self):
		self.app = QApplication(sys.argv)
   		self.win = QWidget()
		self.stack1 = [QLabel("") for i in range(0,7)]		
		self.stack2 = [QLabel("") for i in range(0,7)]
		self.stack3 = [QLabel("") for i in range(0,7)]
		self.stack4 = [QLabel("") for i in range(0,7)]
		self.stack5 = [QLabel("") for i in range(0,7)]
		self.stack6 = [QLabel("") for i in range(0,7)]
		self.stack7 = [QLabel("") for i in range(0,7)]
		self.list = [
			self.stack1,
			self.stack2,
			self.stack3,
			self.stack4,
			self.stack5,
			self.stack6,
			self.stack7,
		]
   		self.gameGrid = QGridLayout()
   		self.mainGrid = QGridLayout()
   		self.leftGrid = QGridLayout()
   		self.next_button = QPushButton("ha")
   		self.col_field = QLineEdit()
   		self.do_layout()
   		self.set_click_event()
   		self.connect4 = Connect4()
	
   	def do_layout(self):
	    self.win.setWindowTitle("Connect4")
	    self.win.setLayout(self.mainGrid)
	    self.win.setGeometry(500,500,800,600)
	    self.set_game_grid()
	    self.set_left_layout()
	    self.mainGrid.addLayout(self.gameGrid, 0,0)
	    self.mainGrid.addLayout(self.leftGrid, 0,1)
	    self.stretch_columns()

	def set_game_grid(self):
	    for i in range(0,7):
	       for j in range(0,7):
	      		l = self.list[i][j]
	      		l.setStyleSheet('background-color: white')
	       		self.gameGrid.addWidget(l,i,j)
	    for i in range(0,7):
	    	self.gameGrid.setRowStretch(i, 1)
	def set_left_layout(self):
		l1 = QLabel("1")
		l2 = QLabel("2")
		l2.setStyleSheet('background-color: yellow')
		self.leftGrid.addWidget(self.col_field,0,0)
		self.leftGrid.addWidget(self.next_button,1,0)
		self.leftGrid.setRowStretch(0,10)
		self.leftGrid.setRowStretch(1,2)

	def stretch_columns(self):
		self.mainGrid.setColumnStretch(1,10)
		self.mainGrid.setColumnStretch(0,50)

	def set_click_event(self):
		self.next_button.clicked.connect(self.handle_click)

	def handle_click(self):
		col =  int(self.col_field.text())
		#self.connect4.make_move(col, 1)

		i = 6
		while self.connect4.list[col][i] != 0:
			i = i - 1
		if i == -1:
			return False
		for ii in range(0,i):
			#self.connect4.list[col][ii] = 2
			#self.set_game_cells(self.connect4.list)
			#print(self.connect4)
			
			#self.connect4.list[col][ii] = 0
			#self.update_game_cell(col,ii,"2")
			self.list[ii][col].setStyleSheet('background-color: yellow')
			self.list[ii][col].repaint()
			QApplication.processEvents()
			time.sleep(0.1)
			self.list[ii][col].setStyleSheet('background-color: white')
			self.list[ii][col].repaint()
			QApplication.processEvents()
			#self.update_game_cell(col,ii,"")
			#print(ii)
			#self.set_game_cells(self.connect4.list)

		self.connect4.list[col][i] = 2
		#self.update_game_cell(col,i,2)
		self.set_game_cells(self.connect4.list)
		self.computer_play()
		print(self.connect4)
	def computer_play(self):
		i = self.connect4.make_random_move()
		for ii in range(0,i):
			self.list[ii][i].setStyleSheet('background-color: red')
			self.list[ii][i].repaint()
			QApplication.processEvents()
			time.sleep(0.1)
			self.list[ii][i].setStyleSheet('background-color: white')
			self.list[ii][i].repaint()
			QApplication.processEvents()
		self.set_game_cells(self.connect4.list)
		self.connect4.find_good_row()
	def show(self):
		self.win.show()
		sys.exit(self.app.exec_())
	def set_game_cells(self, list):
		i = 0
		j = 0
		while i < 7:
			while j < 7:
				if self.connect4.list[i][j] != 0:
					if self.connect4.list[i][j] == 2:
						self.list[j][i].setStyleSheet('background-color: yellow')
					else:
						self.list[j][i].setStyleSheet('background-color: red')
					self.list[j][i].setText(str(self.connect4.list[i][j]))
					self.list[j][i].repaint()
				j = j + 1
			i = i + 1
			j = 0
		QApplication.processEvents()
	def update_game_cell(self, i, j, str):
		self.list[j][i].setText(str)
		self.list[i][j].repaint()
		QApplication.processEvents()


if __name__ == '__main__':
	window = Window()
	window.show()