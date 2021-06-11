from Game.run_game import run_game

from AI.Heuristic import heu
from AI.MCTS import MCTS
from AI.MCTS_RAVE import MCTS_RAVE
from AI.MCTS_MAST import MCTS_MAST

if __name__ == "__main__":
    result = run_game(MCTS_RAVE, MCTS_MAST,  n_iterations=800, printfinalResult=True, printSteps=True)
    print(result)
    # please, work
    # result = run_game(heu, MCTS)
