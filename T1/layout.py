import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QGridLayout, 
    QPushButton, QApplication, QMessageBox)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtCore import *
from functools import partial

from threading import Thread



class GameLayout(QWidget):
    
    def __init__(self, *args, **kwargs):
        self.currPlayer = [1]
        self.lastXPlayed = [-1]
        self.lastYPlayed = [-1]
        self.canPlay = [False]
        self.buttons = [[None for _ in range(15)] for _ in range(15)]
        super().__init__()
        self.grid = None
        self.initUI()

    def initUI(self):
        
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.init_cells()
        self.move(300, 150)
        self.setWindowTitle('Gomokuzera')
        self.show()

    def make_move(self, x, y):
        print('rs')
        self.buttons[x][y].make_move(self.currPlayer)

    def init_cells(self):
        cells_content = []

        for i in range(0, 250):
            cells_content.append(' ')

        positions = [(i,j) for i in range(15) for j in range(15)]
        
        for position, name in zip(positions, cells_content):
            
            if name == '':
                continue
            self.buttons[position[0]][position[1]] = GomokuCell(" ", position[0], position[1])
            self.buttons[position[0]][position[1]].clicked.connect(partial(self.buttons[position[0]][position[1]].on_click, self.currPlayer, self.lastXPlayed, self.lastYPlayed, self.canPlay))
            self.buttons[position[0]][position[1]].setStyleSheet(GomokuCell.defaultStyleSheet)
            self.grid.addWidget(self.buttons[position[0]][position[1]], *position)


class WarningMessageBox:
    def __init__(self, msg):
        self.msg = msg
    def show(self):
        edialog =  QtWidgets.QErrorMessage()
        edialog.showMessage(self.msg)
class GomokuCell(QPushButton):

    defaultStyleSheet = """
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #f6f7fa, stop: 1 #dadbde);;
                border-radius:15px;
                height:30px;
                width:30px;"""
    playerOneStyleSheet = """
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 blue);;
                border-radius:15px;
                height:30px;
                width:30px;"""
    playerTwoStyleSheet = """
                background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 red);;
                border-radius:15px;
                height:30px;
                width:30px;"""

    def __init__(self, name, x, y):
        super().__init__(name)
        self.x = x
        self.y = y
        self.alreadyClicked = False
    def on_click(self, currPlayer, lastx, lasty, canPlay):
        if currPlayer[0] == 2:
            return
        if not (self.alreadyClicked):
            self.alreadyClicked = True
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!')
            error_dialog.exec()
            return
        print(currPlayer)
        print(str(self.x) +' '+ str(self.y))
        if currPlayer[0] is 1:
            self.setStyleSheet(GomokuCell.playerOneStyleSheet)
            currPlayer[0] = 2
        else:
            self.setStyleSheet(GomokuCell.playerTwoStyleSheet)
            currPlayer[0] = 1
        lastx[0] = self.x
        lasty[0] = self.y
        canPlay[0] = True
        currPlayer[0] = 2
        print(canPlay)
    def make_move(self, currPlayer):
        if not (self.alreadyClicked):
            self.alreadyClicked = True
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Oh no!')
            error_dialog.exec()
            return
        if currPlayer[0] is 1:
            self.setStyleSheet(GomokuCell.playerOneStyleSheet)
            currPlayer[0] = 2
        else:
            self.setStyleSheet(GomokuCell.playerTwoStyleSheet)
            currPlayer[0] = 1
