import multiprocessing
import time
from Tests.test import Test
from AI.Heuristic import heu
from AI.MCTS import MCTS
from AI.MCTS import MCTS
from AI.MCTS import MCTS

SEED = 123 


def generate_instances():
    result = []
    result.append(Test(heu, heu, n_repetition=150, name="heu_vs_heu", seed=SEED))
    result.append(Test(heu, heu, n_repetition=150, name="heu_vs_heu", seed=SEED+10))
    result.append(Test(heu, heu, n_repetition=150, name="heu_vs_heu", seed=SEED+20))
    result.append(Test(heu, heu, n_repetition=150, name="heu_vs_heu", seed=SEED+30))
    result.append(Test(heu, heu, n_repetition=150, name="heu_vs_heu", seed=SEED+40))
    result.append(Test(heu, heu, n_repetition=150, name="heu_vs_heu", seed=SEED+50))
    return result


def run_test(test):
    test.start()


def run_tests():
    iterable = generate_instances()
    start_time = time.time()

    p = multiprocessing.Pool()
    p.map_async(run_test, iterable)

    p.close()
    p.join()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    run_tests()

