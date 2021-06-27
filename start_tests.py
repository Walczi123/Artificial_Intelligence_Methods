from Tests.test import Test

from AI.Heuristic import heu
from AI.MCTS import MCTS
from AI.MCTS_RAVE import MCTS_RAVE
from AI.MCTS_MAST import MCTS_MAST


if __name__ == "__main__":
    # result = runGame(mcts.MCTS, heu.heu)
    test = Test(heu, heu, n_repetition=10, name="heu_vs_heu", seed=123)
    test.start()
