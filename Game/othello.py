from tkinter import *
from math import *
from time import *
from random import *
from copy import deepcopy
from tkinter import font

# from tkinter import tkFont

#Tkinter setup
root = Tk()
screen = Canvas(root, width=500, height=600, background="DarkOliveGreen4",highlightthickness=0)
screen.pack()
board = None
moves = None 
depth = None
running = False
nodes = None

computerPlaying = False


class Board:
	def __init__(self, player = 0):
		self.player = player
		self.passed = False
		self.won = False
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
		screen.delete("highlight")
		screen.delete("tile")
		screen.delete("player_signalization")
		for x in range(8):
			for y in range(8):
				#Could replace the circles with images later, if I want
				if self.oldplacements[x][y]=="w":
					screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile {0}-{1}".format(x,y),fill="#aaa",outline="#aaa")
					screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile {0}-{1}".format(x,y),fill="#fff",outline="#fff")

				elif self.oldplacements[x][y]=="b":
					screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile {0}-{1}".format(x,y),fill="#000",outline="#000")
					screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile {0}-{1}".format(x,y),fill="#111",outline="#111")
		#Animation of new tiles
		screen.update()
		for x in range(8):
			for y in range(8):
				#Could replace the circles with images later, if I want
				if self.placements[x][y] != self.oldplacements[x][y] and self.placements[x][y] == "w":
					screen.delete("{0}-{1}".format(x,y))
					#42 is width of tile so 21 is half of that
					#Shrinking
					for i in range(21):
						screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#000",outline="#000")
						screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#111",outline="#111")
						if i%3==0:
							sleep(0.01)
						screen.update()
						screen.delete("animated")
					#Growing
					for i in reversed(range(21)):
						screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#aaa",outline="#aaa")
						screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#fff",outline="#fff")
						if i%3==0:
							sleep(0.01)
						screen.update()
						screen.delete("animated")
					screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile",fill="#aaa",outline="#aaa")
					screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile",fill="#fff",outline="#fff")
					screen.update()

				elif self.placements[x][y]!=self.oldplacements[x][y] and self.placements[x][y]=="b":
					screen.delete("{0}-{1}".format(x,y))
					#42 is width of tile so 21 is half of that
					#Shrinking
					for i in range(21):
						screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#aaa",outline="#aaa")
						screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#fff",outline="#fff")
						if i%3==0:
							sleep(0.01)
						screen.update()
						screen.delete("animated")
					#Growing
					for i in reversed(range(21)):
						screen.create_oval(54+i+50*x,54+i+50*y,96-i+50*x,96-i+50*y,tags="tile animated",fill="#000",outline="#000")
						screen.create_oval(54+i+50*x,52+i+50*y,96-i+50*x,94-i+50*y,tags="tile animated",fill="#111",outline="#111")
						if i%3==0:
							sleep(0.01)
						screen.update()
						screen.delete("animated")

					screen.create_oval(54+50*x,54+50*y,96+50*x,96+50*y,tags="tile",fill="#000",outline="#000")
					screen.create_oval(54+50*x,52+50*y,96+50*x,94+50*y,tags="tile",fill="#111",outline="#111")
					screen.update()
		#Drawing of highlight circles
		#Drawing player sygnalization box
		if self.player == 0:
			sleep(0.02)
			screen.create_rectangle(60,455,440,465,tags="player_signalization", fill="white")
		if self.player == 1 and not(computerPlaying):
			sleep(0.02)
			screen.create_rectangle(60,455,440,465,tags="player_signalization", fill="black")
		for x in range(8):
			for y in range(8):
				if self.player == 0:
					if valid(self.placements,self.player,x,y):
						# helv36 = font.Font(family='Helvetica', size=36, weight='bold')
						# screen.create_text(68+50*x,68+50*y,32+50*(x+1),32+50*(y+1), anchor=W, font=("Helvetica",60), text="X")
						screen.create_oval(68+50*x,68+50*y,32+50*(x+1),32+50*(y+1),tags="highlight",fill="grey78")
				elif self.player == 1 and not(computerPlaying):
					if valid(self.placements,self.player,x,y):
						screen.create_oval(68+50*x,68+50*y,32+50*(x+1),32+50*(y+1),tags="highlight",fill="grey30")
		if not self.won:
			#Draw the scoreboard and update the screen
			self.drawScoreBoard()
			screen.update()
		else:
			screen.create_text(250,550,anchor="c",font=("Consolas",15), text="The game is done!")

	#Moves to position
	def boardMove(self,x,y):
		global nodes
		#Move and update screen
		self.oldplacements = self.placements
		# print("something")
		if computerPlaying or self.player == 0 :
			self.oldplacements[x][y]="w" #change
		elif not(computerPlaying):
			print("here", self.oldplacements[x][y])
			self.oldplacements[x][y]="b" #change
			print("hereAfter", self.oldplacements[x][y])
		self.placements = move(self.placements,x,y)
		
		#Switch Player
		self.player = 1-self.player
		self.update()
		
		#Check if ai must pass
		# self.passTest()
		# self.update()	
	
	def drawScoreBoard(self):
		global moves
		#Deleting prior score elements
		screen.delete("score")

		#Scoring based on number of tiles
		player_score = 0
		computer_score = 0
		for x in range(8):
			for y in range(8):
				if self.placements[x][y]=="w":
					player_score+=1
				elif self.placements[x][y]=="b":
					computer_score+=1

		if self.player==0:
			player_colour = "white"
			computer_colour = "black"
		else:
			player_colour = "white"
			computer_colour = "black"

		screen.create_oval(5,540,25,560,fill=player_colour,outline=player_colour)
		screen.create_oval(380,540,400,560,fill=computer_colour,outline=computer_colour)

		#Pushing text to screen
		screen.create_text(30,550,anchor="w", tags="score",font=("Consolas", 50),fill="white",text=player_score)
		screen.create_text(400,550,anchor="w", tags="score",font=("Consolas", 50),fill="black",text=computer_score)

		moves = player_score+computer_score

	#METHOD: Test if player must pass: if they do, switch the player
	def passTest(self):
		mustPass = True
		for x in range(8):
			for y in range(8):
				if valid(self.placements,self.player,x,y):
					mustPass=False
		if mustPass:
			self.player = 1-self.player
			if self.passed==True:
				self.won = True
			else:
				self.passed = True
			self.update()
		else:
			self.passed = False

	
def getPlayersColor():
	if board.player==0:
		colour = "w"
	else:
		colour = "b"
	return colour

def move(passedArray,x,y):
	#Must copy the passedArray so we don't alter the original
	array = deepcopy(passedArray)
	#Set colour and set the moved location to be that colour
	colour = getPlayersColor()
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


	
def checkForAnyLine(placements, colour, x, y, i, j):
	neighX = i
	neighY = j
	
	#If the neighbour colour is equal to your colour, it doesn't form a line
	#Go onto the next neighbour
	if placements[neighX][neighY]==colour:
		return False

	#Determine the direction of the line
	deltaX = neighX-x
	deltaY = neighY-y
	tempX = neighX
	tempY = neighY
	
	while 0<=tempX<=7 and 0<=tempY<=7:
		#If an empty space, no line is formed
		if placements[tempX][tempY]==None:
			return False
		#If it reaches a piece of the player's colour, it forms a line
		if placements[tempX][tempY]==colour:
			return True
		#Move the index according to the direction of the line
		tempX+=deltaX
		tempY+=deltaY
	return False

#Checks if a move is valid for a given array.
def valid(placements, player, x, y):
	#Sets player colour
	colour = getPlayersColor()
	#If there's already a piece there, it's an invalid move
	if placements[x][y] != None:
		return False

	else:
		#Generating the list of neighbours
		neighbour = False
		neighbours = []
		valid = False
		for i in range(max(0,x-1),min(x+2,8)):
			for j in range(max(0,y-1),min(y+2,8)):
				if placements[i][j]!=None:
					neighbour=True
					neighbours.append([i,j])
					valid = valid or checkForAnyLine(placements, colour, x, y, i, j)
		#If there's no neighbours, it's an invalid move
		if not neighbour:
			return False
		else:
			return valid


def clickHandle(event):
	global depth
	xMouse = event.x
	yMouse = event.y
	if running:
		print("running")
		if xMouse>=450 and yMouse<=50:
			root.destroy()
		elif xMouse<=50 and yMouse<=50:
			playGame()
		else:
			#Is it the player's turn?
			if not(computerPlaying) or board.player == 0:
				#Delete the highlights
				x = int((event.x-50)/50)
				y = int((event.y-50)/50)
				print("x, y", x, y)
				#Determine the grid index for where the mouse was clicked
				
				#If the click is inside the bounds and the move is valid, move to that location
				if 0<=x<=7 and 0<=y<=7:
					if valid(board.placements,board.player,x,y):
						print("valid, x, y", x, y)
						board.boardMove(x,y)
	else:
		print("else before played")
		#Difficulty clicking
		if 180<=xMouse<=310:
			depth = 1
			print("played")
			playGame()


def keyHandle(event):
	symbol = event.keysym
	if symbol.lower()=="r":
		playGame()
	elif symbol.lower()=="q":
		root.destroy()

	
def runGame():
	global running
	running = False
	print("running", running)
	#Title and shadow
	screen.create_text(250,203,anchor="c",text="Othello",font=("Consolas", 50),fill="dark slate gray")
	screen.create_text(250,200,anchor="c",text="Othello",font=("Consolas", 50),fill="white smoke")
	
	#Creating the play button
	i=1
	spacing = 130/2
	screen.create_rectangle(25+155*1, 310, 155+155*i, 355, fill="dark slate gray", outline="dark slate gray")
	screen.create_rectangle(25+155*1, 300, 155+155*i, 350, fill="cadet blue", outline="cadet blue")
	screen.create_text(25+1*spacing+155*1,327,anchor="c",text="Play", font=("Consolas",25),fill="gainsboro")
	screen.update()

#Method for drawing the gridlines
def drawGridBackground(outline=True):
	#If we want an outline on the board then draw one
	if outline:
		screen.create_rectangle(50,50,450,450,outline="#111")

	#Drawing the intermediate lines
	for i in range(7):
		lineShift = 50+50*(i+1)

		#Horizontal line
		screen.create_line(50,lineShift,450,lineShift,fill="#111")

		#Vertical line
		screen.create_line(lineShift,50,lineShift,450,fill="#111")

	screen.update()

def create_buttons():
		#Restart button
		#Background/shadow
		screen.create_rectangle(0,5,50,55,fill="#000033", outline="#000033")
		screen.create_rectangle(0,0,50,50,fill="#000088", outline="#000088")

		#Arrow
		screen.create_arc(5,5,45,45,fill="#000088", width="2",style="arc",outline="white",extent=300)
		screen.create_polygon(33,38,36,45,40,39,fill="white",outline="white")

		#Quit button
		#Background/shadow
		screen.create_rectangle(450,5,500,55,fill="#330000", outline="#330000")
		screen.create_rectangle(450,0,500,50,fill="#880000", outline="#880000")
		#"X"
		screen.create_line(455,5,495,45,fill="white",width="3")
		screen.create_line(495,5,455,45,fill="white",width="3")
		
def playGame():
	global board, running
	running = True
	screen.delete(ALL)
	create_buttons()
	#Draw the background
	drawGridBackground()
	#Create the board and update it
	board = Board()
	board.update()

runGame()

#Binding, setting
screen.bind("<Button-1>", clickHandle)
screen.bind("<Key>",keyHandle)
screen.focus_set()

#Run forever
root.wm_title("Othello")
root.mainloop()