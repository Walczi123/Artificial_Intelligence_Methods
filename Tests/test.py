import numpy as np
from Game.run_game import run_game


class Test:
    def __init__(self,  player1, player2, n_repetition=1, name="test", seed=None, n_iterations=800):
        self.n_repetition = n_repetition
        self.n_iterations = n_iterations
        self.player1 = player1
        self.player2 = player2
        self.name = name
        self.seed = seed

    def start(self):
        results = []
        s = self.seed
        for i in range(self.n_repetition):
            if self.seed is not None:
                self.seed = self.seed + 1
                np.random.seed(self.seed)
            result, moves_amount = run_game(
                self.player1, self.player2, self.n_iterations)
            results.append((result, moves_amount))
        self.seed = s
        self.save_to_file(results, "Results/" +
                          self.name + "_" +
                          str(self.n_repetition) + "_" + str(self.seed) + "_" + str(self.n_iterations) + ".txt")


    def save_to_file(self, results, file_path):
        f = open(file_path, "w")
        print("savind", self.name)
        player2_wins = sum([i[0] for i in results])
        player1_wins = self.n_repetition - player2_wins
        f.write(f"Player(1) {str(self.player1.__name__)} wins: \t Player(2) {str(self.player2.__name__)} wins: \t tree iterations:\n")
        f.write(str(player1_wins)+" \t " + str(player2_wins) +
                "\t" + str(self.n_iterations) + "\n")
        f.write("Game"+"\t"+"winner"+"\t"+"moves:\n")
        results = [str(i+1)+"\t"+str(results[i][0]+1) + "\t" + str(results[i][1]+1) + '\n'
                   for i in range(len(results))]
        f.writelines(results)
        f.close
