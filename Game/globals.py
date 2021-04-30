from tkinter import *
from math import *
from time import *
from random import *
from copy import deepcopy
from tkinter import font

class Globals:
    def __init__(self, player1= None, player2 = None, board = None, moves = None, depth = None, running = False, nodes = None):
        self.root = Tk()
        self.screen = Canvas(root, width=500, height=600, background="DarkOliveGreen4",highlightthickness=0)
        screen.pack()
        self.board = board
        self.moves = moves 
        self.depth = depth
        self.running = running
        self.nodes = nodes

        self.player1 = player1
        self.player2 = player2

