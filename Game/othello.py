from tkinter import *
from math import *
from time import *
from random import *
from copy import deepcopy
from tkinter import font

import Game.globals 

class Board:
	def __init__(self, globalValues, player = 0):
		self.player = player
		self.passed = False
		self.won = False
		self.g = globalValues
		#Initializing an empty board
		# self.placements = [[None for _ in range(8)] for _ in range(8)]
		self.placements = []
		for x in range(8):
			self.placements.append([])
			for y in range(8):
				self.placements[x].append(None)
		
		#Initializing center values
		self.placements[3][3] = "w"
		self.placements[3][4] = "b"
		self.placements[4][3] = "b"
		self.placements[4][4] = "w"

		#Initializing old values
		self.oldplacements = self.placements

	def update(self):
		self.g.screen.delete("highlight")
		self.g.screen.delete("tile")
		self.g.screen.delete("player_signalization")
		for x in range(8):
			for y in range(8):
				#Could replace the circles with images later, if I want
				if self.oldplacements[x][y]=="w":
					self.g.screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile {0}-{1}".format(x,y),fill="#aaa",outline="#aaa")
					self.g.screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile {0}-{1}".format(x,y),fill="#fff",outline="#fff")

				elif self.oldplacements[x][y]=="b":
					self.g.screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile {0}-{1}".format(x,y),fill="#000",outline="#000")
					self.g.screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile {0}-{1}".format(x,y),fill="#111",outline="#111")
		#Animation of new tiles
		self.g.screen.update()
		for x in range(8):
			for y in range(8):
				#Could replace the circles with images later, if I want
				if self.placements[x][y] != self.oldplacements[x][y] and self.placements[x][y] == "w":
					self.g.screen.delete("{0}-{1}".format(x,y))
					#42 is width of tile so 21 is half of that
					#Shrinking
					for i in range(21):
						self.g.screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#000",outline="#000")
						self.g.screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#111",outline="#111")
						if i%3==0:
							sleep(0.01)
						self.g.screen.update()
						self.g.screen.delete("animated")
					#Growing
					for i in reversed(range(21)):
						self.g.screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#aaa",outline="#aaa")
						self.g.screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#fff",outline="#fff")
						if i%3==0:
							sleep(0.01)
						self.g.screen.update()
						self.g.screen.delete("animated")
					self.g.screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile",fill="#aaa",outline="#aaa")
					self.g.screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile",fill="#fff",outline="#fff")
					self.g.screen.update()

				elif self.placements[x][y]!=self.oldplacements[x][y] and self.placements[x][y]=="b":
					self.g.screen.delete("{0}-{1}".format(x,y))
					#42 is width of tile so 21 is half of that
					#Shrinking
					for i in range(21):
						self.g.screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#aaa",outline="#aaa")
						self.g.screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#fff",outline="#fff")
						if i%3==0:
							sleep(0.01)
						self.g.screen.update()
						self.g.screen.delete("animated")
					#Growing
					for i in reversed(range(21)):
						self.g.screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#000",outline="#000")
						self.g.screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#111",outline="#111")
						if i%3==0:
							sleep(0.01)
						self.g.screen.update()
						self.g.screen.delete("animated")

					self.g.screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile",fill="#000",outline="#000")
					self.g.screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile",fill="#111",outline="#111")
					self.g.screen.update()
		#Drawing of highlight circles
		#Drawing player sygnalization box
		if self.player == 0:
			sleep(0.02)
			self.g.screen.create_rectangle(60,455,440,465,tags="player_signalization", fill="white")
		if self.player == 1 and not(self.g.computerMove):
			sleep(0.02)
			self.g.screen.create_rectangle(60,455,440,465,tags="player_signalization", fill="black")
		for x in range(8):
			for y in range(8):
				if self.player == 0:
					if self.valid(self.player,x,y):
						# helv36 = font.Font(family='Helvetica', size=36, weight='bold')
						# self.g.screen.create_text(68+50*x,68+50*y,32+50*(x+1),32+50*(y+1), anchor=W, font=("Helvetica",60), text="X")
						self.g.screen.create_oval(68+50*x,68+50*y,32+50*(x+1),32+50*(y+1),tags="highlight",fill="grey78")
				elif self.player == 1 and not(self.g.computerMove):
					if self.valid(self.player,x,y):
						self.g.screen.create_oval(68+50*x,68+50*y,32+50*(x+1),32+50*(y+1),tags="highlight",fill="grey30")
		if not self.won:
			#Draw the scoreboard and update the self.g.screen
			self.drawScoreBoard()
			self.g.screen.update()
		else:
			self.g.screen.create_text(250,550,anchor="c",font=("Consolas",15), text="The game is done!")

	#Moves to position
	def boardMove(self,x,y):
		#Move and update self.g.screen
		self.oldplacements = self.placements
		# print("something")
		if self.player%2 == 0 :
			self.oldplacements[x][y]="w" #change
		else:
			print("here", self.oldplacements[x][y])
			self.oldplacements[x][y]="b" #change
			print("hereAfter", self.oldplacements[x][y])
		self.placements = self.move(x,y)
		
		#Switch Player
		self.g.switchPlayer()
		self.update()
		
	
	def drawScoreBoard(self):
		print("Draw")
		#Deleting prior score elements
		self.g.screen.delete("score")

		#Scoring based on number of tiles
		player_score = 0
		computer_score = 0
		for x in range(8):
			for y in range(8):
				if self.placements[x][y]=="w":
					player_score+=1
				elif self.placements[x][y]=="b":
					computer_score+=1

		if self.player%2==0:
			player_colour = "white"
			computer_colour = "black"
		else:
			player_colour = "white"
			computer_colour = "black"

		self.g.screen.create_oval(5,540,25,560,fill=player_colour,outline=player_colour)
		self.g.screen.create_oval(380,540,400,560,fill=computer_colour,outline=computer_colour)

		#Pushing text to screen
		self.g.screen.create_text(30,550,anchor="w", tags="score",font=("Consolas", 50),fill="white",text=player_score)
		self.g.screen.create_text(400,550,anchor="w", tags="score",font=("Consolas", 50),fill="black",text=computer_score)

		moves = player_score+computer_score

	#METHOD: Test if player must pass: if they do, switch the player
	def mustPass(self):
		mustPass = True
		for x in range(8):
			for y in range(8):
				if self.valid(self.player,x,y):
					mustPass=False
		return mustPass
	
	
	def getPlayersColor(self):
		if self.player%2==0:
			colour = "w"
		else:
			colour = "b"
		return colour

	def move(self, x, y):
		#Must copy the passedArray so we don't alter the original
		array = deepcopy(self.placements)
		#Set colour and set the moved location to be that colour
		colour = self.getPlayersColor()
		array[x][y] = colour
		
		#Determining the neighbours to the square
		neighbours = []
		for i in range(max(0,x-1),min(x+2,8)):
			for j in range(max(0,y-1),min(y+2,8)):
				if array[i][j]!=None:
					neighbours.append([i,j])
		
		#Which tiles to convert
		convert = []

		#For all the generated neighbours, determine if they form a line
		#If a line is formed, we will add it to the convert array
		for neighbour in neighbours:
			neighX = neighbour[0]
			neighY = neighbour[1]
			#Check if the neighbour is of a different colour - it must be to form a line
			if array[neighX][neighY]!=colour:
				#The path of each individual line
				path = []
				
				#Determining direction to move
				deltaX = neighX-x
				deltaY = neighY-y

				tempX = neighX
				tempY = neighY

				#While we are in the bounds of the board
				while 0<=tempX<=7 and 0<=tempY<=7:
					path.append([tempX,tempY])
					value = array[tempX][tempY]
					#If we reach a blank tile, we're done and there's no line
					if value==None:
						break
					#If we reach a tile of the player's colour, a line is formed
					if value==colour:
						#Append all of our path nodes to the convert array
						for node in path:
							convert.append(node)
						break
					#Move the tile
					tempX+=deltaX
					tempY+=deltaY
					
		#Convert all the appropriate tiles
		for i,j in convert:
			array[i][j]=colour

		return array


	
	def checkForAnyLine(self, colour, x, y, i, j):
		neighX = i
		neighY = j
		
		#If the neighbour colour is equal to your colour, it doesn't form a line
		#Go onto the next neighbour
		if self.placements[neighX][neighY]==colour:
			return False

		#Determine the direction of the line
		deltaX = neighX-x
		deltaY = neighY-y
		tempX = neighX
		tempY = neighY
		
		while 0<=tempX<=7 and 0<=tempY<=7:
			#If an empty space, no line is formed
			if self.placements[tempX][tempY]==None:
				return False
			#If it reaches a piece of the player's colour, it forms a line
			if self.placements[tempX][tempY]==colour:
				return True
			#Move the index according to the direction of the line
			tempX+=deltaX
			tempY+=deltaY
		return False

	#Checks if a move is valid for a given array.
	def valid(self, player, x, y):
		#Sets player colour
		colour = self.getPlayersColor()
		#If there's already a piece there, it's an invalid move
		if self.placements[x][y] != None:
			return False

		else:
			#Generating the list of neighbours
			neighbour = False
			neighbours = []
			valid = False
			for i in range(max(0,x-1),min(x+2,8)):
				for j in range(max(0,y-1),min(y+2,8)):
					if self.placements[i][j]!=None:
						neighbour=True
						neighbours.append([i,j])
						valid = valid or self.checkForAnyLine(colour, x, y, i, j)
			#If there's no neighbours, it's an invalid move
			if not neighbour:
				return False
			else:
				return valid


