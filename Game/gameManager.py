from tkinter import *
from math import *
from time import *
from random import *
from copy import deepcopy
from tkinter import font
import Game.othello as ot
import Game.globals as cdf


g = cdf.Globals()

def clickHandle(event):
    xMouse = event.x
    yMouse = event.y
    if g.running:
        print("g.running")
        if not(g.computerMove):
            if xMouse >= 450 and yMouse <= 50:
                g.root.destroy()
            elif xMouse <= 50 and yMouse <= 50:
                playGame()
            else:
                # Is it the player's turn?
                # if not(g.computerMove) or g.board.player == 0:
                    # Delete the highlights
                    x = int((event.x-50)/50)
                    y = int((event.y-50)/50)
                    print("x, y", x, y)
                    # Determine the grid index for where the mouse was clicked

                    # If the click is inside the bounds and the move is valid, move to that location
                    if 0 <= x <= 7 and 0 <= y <= 7:
                        if g.board.valid( g.board.player, x, y):
                            print("valid, x, y", x, y)
                            g.board.boardMove(x, y)
                            doValidComputerMove()
                       
        else:
            doValidComputerMove()
            # if (not(g.board.mustPass())):
            #     g.switchPlayer()
            #     if (not(g.board.mustPass())):
            #         print("Game won")
            #     else:
            #         doValidComputerMove()
    else:
        # Difficulty clicking
        if 180 <= xMouse <= 310:
            g.depth = 1
            print("played")
            playGame()


def doValidComputerMove():
    #todo
    print("g.board.player, g.computerMove", g.board.player, g.computerMove)
    for x in range(8):
        for y in range(8):
            if g.board.valid(g.board.player,x,y):
                g.board.boardMove(x, y)
                sleep(0.002)


def keyHandle(event):
    symbol = event.keysym
    if symbol.lower() == "r":
        playGame()
    elif symbol.lower() == "q":
        g.root.destroy()

def computerPlay():
    if (g.computerMove):
        if (g.board.mustPass()):
            doValidComputerMove()
        g.switchPlayer()
        while (True):
            if g.computerMove:
                break
        if (not(g.board.mustPass())):
            g.switchPlayer()
            if (not(g.board.mustPass())):
                print("Game won")
            else:
                doValidComputerMove()
    
    

def playGame():
    g.running = True
    g.screen.delete(ALL)
    create_buttons()
    # Draw the background
    drawGridBackground()
    # Create the g.board and update it
    
    g.player1 = 0
    g.player2 = 3
    g.board = ot.Board(g, g.player1)
    print("computerMove", g.computerMove)
    g.board.update()

    # while(True):
    #     computerPlay()


def runGame():
    g.running = False
    print("g.running omg omg", g.running)
    # Title and shadow
    g.screen.create_text(250, 203, anchor="c", text="Othello", font=(
        "Consolas", 50), fill="dark slate gray")
    g.screen.create_text(250, 200, anchor="c", text="Othello",
                         font=("Consolas", 50), fill="white smoke")

    # Creating the play buttons, 1- two players, 2- player vs computer, 3- computer vs computerfor i in range(3):
    # Background
    i=1
    g.screen.create_rectangle(
        25+155*i, 310, 155+155*i, 355, fill="dark slate gray", outline="dark slate gray")
    g.screen.create_rectangle(25+155*i, 300, 155+155*i,
                              350, fill="cadet blue", outline="cadet blue")

    # # Creating the difficulty buttons
    for i in range(3):
               # Background
        g.screen.create_rectangle(
            25+155*i, 310, 155+155*i, 355, fill="dark slate gray", outline="#000")
        g.screen.create_rectangle(
            25+155*i, 300, 155+155*i, 350, fill="cadet blue", outline="#111")

    spacing = 130/(3)
    i=0
    g.screen.create_text(25+(1)*spacing+155*i, 326, anchor="c", text="2", font=("Consolas", 25), fill="gainsboro")
    g.screen.create_text(25+(2)*spacing+155*i, 327, anchor="c",  text="1", font=("Consolas", 25), fill="gainsboro")
    g.screen.create_text(25+(3)*spacing+155*i, 325, anchor="c", text="Sim", font=("Consolas", 25), fill="gainsboro")


#Method for drawing the gridlines
def drawGridBackground(outline=True):
	#If we want an outline on the board then draw one
	if outline:
		g.screen.create_rectangle(50,50,450,450,outline="#111")

	#Drawing the intermediate lines
	for i in range(7):
		lineShift = 50+50*(i+1)

		#Horizontal line
		g.screen.create_line(50,lineShift,450,lineShift,fill="#111")

		#Vertical line
		g.screen.create_line(lineShift,50,lineShift,450,fill="#111")

	g.screen.update()

def create_buttons():
		#Restart button
		#Background/shadow
		g.screen.create_rectangle(0,5,50,55,fill="#000033", outline="#000033")
		g.screen.create_rectangle(0,0,50,50,fill="#000088", outline="#000088")

		#Arrow
		g.screen.create_arc(5,5,45,45,fill="#000088", width="2",style="arc",outline="white",extent=300)
		g.screen.create_polygon(33,38,36,45,40,39,fill="white",outline="white")

		#Quit button
		#Background/shadow
		g.screen.create_rectangle(450,5,500,55,fill="#330000", outline="#330000")
		g.screen.create_rectangle(450,0,500,50,fill="#880000", outline="#880000")
		#"X"
		g.screen.create_line(455,5,495,45,fill="white",width="3")
		g.screen.create_line(495,5,455,45,fill="white",width="3")
		

if __name__ == "__main__":
#     # global gl

    #     # gl = g.Globals()
    print("here")
    runGame()

    # # Binding, setting
    g.screen.bind("<Button-1>", clickHandle)
    g.screen.bind("<Key>", keyHandle)
    g.screen.focus_set()

    # Run forever
    g.root.wm_title("Not othello")
    g.root.mainloop()
