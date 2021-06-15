import multiprocessing
import time
from Tests.test import Test
from AI.Heuristic import heu
from AI.MCTS import MCTS
from AI.MCTS_MAST import MCTS_MAST
from AI.MCTS_RAVE import MCTS_RAVE

SEED = 1202052400
REPETITIONS = 75
TREE_ITERATIONS = 5000


def generate_instances():
    result = []
    # result.append(Test(MCTS, MCTS_RAVE, n_repetition=REPETITIONS,
    #                    name="mcts_vs_rave", seed=SEED, n_iterations=TREE_ITERATIONS))
    # result.append(Test(MCTS, MCTS_MAST, n_repetition=REPETITIONS,
    #                    name="mcts_vs_mast", seed=SEED + (1 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(MCTS, heu, n_repetition=REPETITIONS,
    #                    name="mcts_vs_heu", seed=SEED + (2 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(MCTS_RAVE, MCTS_MAST, n_repetition=REPETITIONS,
    #                    name="rave_vs_mast", seed=SEED + (3 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(MCTS_RAVE, heu, n_repetition=REPETITIONS,
    #                    name="rave_vs_heu", seed=SEED + (4 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(MCTS_MAST, heu, n_repetition=REPETITIONS,
    #                    name="mast_vs_heu", seed=SEED + (5 * REPETITIONS), n_iterations=TREE_ITERATIONS))

    # result.append(Test(MCTS_RAVE, MCTS, n_repetition=REPETITIONS,
    #                    name="rave_vs_mcts", seed=SEED + (6 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(MCTS_MAST, MCTS, n_repetition=REPETITIONS,
    #                    name="mast_vs_mcts", seed=SEED + (7 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(heu, MCTS, n_repetition=REPETITIONS,
    #                    name="heu_vs_mcts", seed=SEED + (8 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(MCTS_MAST, MCTS_RAVE, n_repetition=REPETITIONS,
    #                    name="mast_vs_rave", seed=SEED + (9 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(heu, MCTS_RAVE, n_repetition=REPETITIONS,
    #                    name="heu_vs_rave", seed=SEED + (10 * REPETITIONS), n_iterations=TREE_ITERATIONS))
    # result.append(Test(heu, MCTS_MAST,  n_repetition=REPETITIONS,
    #                    name="heu_vs_mast", seed=SEED + (11 * REPETITIONS), n_iterations=TREE_ITERATIONS))

    result.append(Test(MCTS, MCTS, n_repetition=REPETITIONS,
                       name="mcts_vs_mcts", seed=SEED, n_iterations=TREE_ITERATIONS))
    result.append(Test(MCTS_MAST, MCTS_MAST, n_repetition=REPETITIONS,
                       name="mast_vs_mast", seed=SEED, n_iterations=TREE_ITERATIONS))
    result.append(Test(heu, heu, n_repetition=REPETITIONS,
                       name="heu_vs_heu", seed=SEED, n_iterations=TREE_ITERATIONS))
    result.append(Test(MCTS_RAVE, MCTS_RAVE, n_repetition=REPETITIONS,
                       name="rave_vs_rave", seed=SEED, n_iterations=TREE_ITERATIONS))
    return result


def run_test(test):
    print("in t: " + test.name)
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
