from Game.run_game import run_game

from AI.Heuristic import heu
from AI.MCTS import MCTS
from AI.MCTS_RAVE import MCTS_RAVE
from AI.MCTS_MAST import MCTS_MAST

if __name__ == "__main__":
    result = run_game(MCTS_RAVE, MCTS_MAST, True, True, n_iterations=30)
    print(result)
    # result = run_game(heu, MCTS)
