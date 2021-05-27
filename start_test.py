
import Game.othello2 as ot
import Game.globals as cdf
import AI.MCTS as mcts
import AI.Heuristic as heu

g = cdf.Globals()


def runGame(f1,f2, printfinalResult, printSteps):
    """[summary]

    Args:
        f1 (function name with library): AI function name (must take three arguments: gamestate table, player (0 or 1), iterations amount) \n \t
        f2 (function name with library): AI function name (must take three arguments: gamestate table, player (0 or 1), iterations amount) \n \t
        printfinalResult (bool): Indicates whether the final state of the game should be displayed \n \t
        printSteps (bool): Indicates whether every move of the game should be displayed \n

    Returns:
        int: Number of the winner
    """
    g.board = ot.Board(g)
    passed_1 = False
    passed_2 = False

    while not(passed_2 and passed_1):
        passed_1 = False
        passed_2 = False

        if not(ot.must_pass(g.board.placements, g.board.player)):
            x, y = eval(str(f1(g.board.placements, g.board.player, 3)))
            g.board.oldplacements, g.board.placements = ot.board_move(g.board.placements, g.board.player, x, y)
            if printSteps:
                g.board.update()
        else:
            passed_1 = True

        g.switchPlayer()  #player2

        if not(ot.must_pass(g.board.placements, g.board.player)):
            x, y = eval(str(f2(g.board.placements, g.board.player, 3)))
            g.board.oldplacements, g.board.placements = ot.board_move(g.board.placements, g.board.player, x, y)
            if printSteps:
                g.board.update()
            g.switchPlayer()  # player1
        else:
            passed_2 = True
            g.switchPlayer()  # player1
            if ot.must_pass(g.board.placements, g.board.player):
                passed_1 = True

    if printfinalResult:
        g.board.update_without_animation(sleep_time = 1)

    if ot.get_result(g.board.placements, g.board.player):
        return g.board.player
    else:
        g.switchPlayer()
        return g.board.player
    
    


#Method for drawing the gridlines
def drawGridBackground(outline=True):
	#If we want an outline on the board then draw one
	if outline:
		g.screen.create_rectangle(50, 50, 450, 450, outline="#111")

	#Drawing the intermediate lines
	for i in range(7):
		lineShift = 50+50*(i+1)

		#Horizontal line
		g.screen.create_line(50, lineShift, 450, lineShift, fill="#111")

		#Vertical line
		g.screen.create_line(lineShift, 50, lineShift, 450, fill="#111")

	g.screen.update()


if __name__ == "__main__":
    drawGridBackground()

    print("Won:", runGame(mcts.MCTS, heu.heu, True, False))
    # # Binding, setting
    # g.screen.bind("<Button-1>", clickHandle)
    # g.screen.bind("<Key>", keyHandle)
    # g.screen.focus_set()

    # # Run forever
    # g.root.wm_title("Not othello")
    # g.root.mainloop()
