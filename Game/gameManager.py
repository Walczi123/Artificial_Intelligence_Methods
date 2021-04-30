from tkinter import *
from math import *
from time import *
from random import *
from copy import deepcopy
from tkinter import font
import Game.othello as ot
import Game.globals as g


gl = g.Globals()

def clickHandle(event):
    xMouse = event.x
    yMouse = event.y
    if g.running:
        print("g.running")
        if xMouse >= 450 and yMouse <= 50:
            g.root.destroy()
        elif xMouse <= 50 and yMouse <= 50:
            playGame()
        else:
            # Is it the player's turn?
            if not(g.computerPlaying) or g.board.player == 0:
                # Delete the highlights
                x = int((event.x-50)/50)
                y = int((event.y-50)/50)
                print("x, y", x, y)
                # Determine the grid index for where the mouse was clicked

                # If the click is inside the bounds and the move is valid, move to that location
                if 0 <= x <= 7 and 0 <= y <= 7:
                    if ot.valid(g.board.placements, g.board.player, x, y):
                        print("valid, x, y", x, y)
                        g.board.g.boardMove(x, y)
    else:
        print("else before played")
        # Difficulty clicking
        if 180 <= xMouse <= 310:
            g.depth = 1
            print("played")
            playGame()


def keyHandle(event):
    symbol = event.keysym
    if symbol.lower() == "r":
        playGame()
    elif symbol.lower() == "q":
        g.root.destroy()


def playGame():
    g.running = True
    g.screen.delete(ALL)
    ot.create_buttons()
    # Draw the background
    ot.drawGridBackground()
    # Create the g.board and update it
    g.board = ot.Board(gl)
    g.board.update()


# def runGame():
#     g.running = False
#     print("g.running omg omg", g.running)
#     # Title and shadow
#     g.screen.create_text(250, 203, anchor="c", text="Othello", font=(
#         "Consolas", 50), fill="dark slate gray")
#     g.screen.create_text(250, 200, anchor="c", text="Othello",
#                          font=("Consolas", 50), fill="white smoke")

#     # Creating the play buttons, 1- two players, 2- player vs computer, 3- computer vs computerfor i in range(3):
#     # Background
#     i=1
#     g.screen.create_rectangle(
#         25+155*i, 310, 155+155*i, 355, fill="dark slate gray", outline="dark slate gray")
#     g.screen.create_rectangle(25+155*i, 300, 155+155*i,
#                               350, fill="cadet blue", outline="cadet blue")

#     # # Creating the difficulty buttons
#     # for i in range(3):
#     #            # Background
#     #     g.screen.create_rectangle(
#     #         25+155*i, 310, 155+155*i, 355, fill="dark slate gray", outline="#000")
#     #     g.screen.create_rectangle(
#     #         25+155*i, 300, 155+155*i, 350, fill="cadet blue", outline="#111")

#     #     spacing = 130/(i+2)
#     #     for x in range(i+1):
#     #             # Star with double shadow
#     #         g.screen.create_text(25+(x+1)*spacing+155*i, 326, anchor="c", text="Multiplayer", font=("Consolas", 25), fill="gainsboro")
#     #         g.screen.create_text(25+(x+1)*spacing+155*i, 327, anchor="c",  text="Single", font=("Consolas", 25), fill="gainsboro")
#     #         g.screen.create_text(25+(x+1)*spacing+155*i, 325, anchor="c", text="Simulation", font=("Consolas", 25), fill="gainsboro")

#     #     # screen.create_rectangle(25+155*i, 300, 155+155*i, 350, fill="#111", outline="#111")
#     #     # i=1
#     spacing = 130/2
#     g.screen.create_rectangle(25+155*1, 310, 155+155*i, 355, fill="dark slate gray", outline="dark slate gray")
#     g.screen.create_rectangle(25+155*1, 300, 155+155*i, 350, fill="cadet blue", outline="cadet blue")
#     g.screen.create_text(25+1*spacing+155*1,327,anchor="c",text="PlayOMG", font=("Consolas",25),fill="gainsboro")
#     g.screen.update()

def runGame():
	running = False
	print("running", g.running)
	#Title and shadow
	g.screen.create_text(250,203,anchor="c",text="Othello",font=("Consolas", 50),fill="dark slate gray")
	g.screen.create_text(250,200,anchor="c",text="Othello",font=("Consolas", 50),fill="white smoke")
	
	#Creating the play button
	i=1
	spacing = 130/2
	g.screen.create_rectangle(25+155*1, 310, 155+155*i, 355, fill="dark slate gray", outline="dark slate gray")
	g.screen.create_rectangle(25+155*1, 300, 155+155*i, 350, fill="cadet blue", outline="cadet blue")
	g.screen.create_text(25+1*spacing+155*1,327,anchor="c",text="Nooo", font=("Consolas",25),fill="gainsboro")
	g.screen.update()

if __name__ == "__main__":
    # global gl

    # gl = g.Globals()
    print("here")
    runGame()

    # Binding, setting
    g.screen.bind("<Button-1>", clickHandle)
    g.screen.bind("<Key>", keyHandle)
    g.screen.focus_set()

    # Run forever
    g.root.wm_title("Not othello")
    g.root.mainloop()
