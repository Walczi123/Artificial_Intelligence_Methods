import multiprocessing
import time
from Tests.test import Test
from AI.Heuristic import heu
from AI.MCTS import MCTS
from AI.MCTS_MAST import MCTS_MAST
from AI.MCTS_RAVE import MCTS_RAVE

SEED = 1202050400
REPETITIONS = 2
DEPTH = 9

def generate_instances():
    result = []
    result.append(Test(MCTS, MCTS_RAVE, n_repetition=REPETITIONS,
                                        name="mcts_vs_rave", seed=SEED, depth=DEPTH))
    result.append(Test(MCTS, MCTS_MAST, n_repetition=REPETITIONS,
                                        name="mcts_vs_mast", seed=SEED + (1 * REPETITIONS), depth=DEPTH))
    result.append(Test(MCTS, heu, n_repetition=REPETITIONS,
                                        name="mcts_vs_heu", seed=SEED + (2 * REPETITIONS), depth=DEPTH))
    result.append(Test(MCTS_RAVE, MCTS_MAST, n_repetition=REPETITIONS,
                                        name="rave_vs_mast", seed=SEED + (3 * REPETITIONS), depth=DEPTH))
    result.append(Test(MCTS_RAVE, heu, n_repetition=REPETITIONS,
                                        name="rave_vs_heu", seed=SEED + (4 * REPETITIONS), depth=DEPTH))
    result.append(Test(MCTS_MAST, heu, n_repetition=REPETITIONS,
                                        name="mast_vs_heu", seed=SEED + (5 * REPETITIONS), depth=DEPTH))
    return result


def run_test(test):
    print("in t: "+ test.name)
    test.start()


def run_tests():
    iterable = generate_instances()
    print("iterable", iterable)
    start_time = time.time()

    p = multiprocessing.Pool()
    p.map_async(run_test, iterable)

    p.close()
    p.join()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    run_tests()

