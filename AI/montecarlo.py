import random
from AI.node import Node


class MonteCarloTreeSearch:
    def __init__(self):
        pass

    def selection(self):
        best_children = []
        best_score = float('-inf')

        for child in self.children:
            score = child.select_UTC_child()

            if score > best_score:
                best_score = score
                best_children = [child]
            elif score == best_score:
                best_children.append(child)

        return random.choice(best_children)

    def expansion(self, node):
        if node.untried_moves != []:
            m = random.choice(node.untried_moves)
            state.make_move(m)
            node = node.add_child(m, state)

    def playout(self):
        while True:
            all_possible_moves = state.get_all_possible_moves()
            if all_possible_moves != []:
                state.make_move(random.choice(all_possible_moves))
                continue
            state.chg_color()
            all_possible_moves = state.get_all_possible_moves()
            if all_possible_moves != []:
                for corner in [0, 7, 56, 63]:
                    if corner in all_possible_moves:
                        state.make_move(corner)
                        continue
                state.make_move(random.choice(all_possible_moves))
                continue
            break

    def backpropagation(self, result):
        self.win_value += result
        self.visits += 1

        if self.parent:
            self.parent.backpropagation(result)

    def get_move(self, state):
        node = self.selection()
        self.expansion(node)
        self.playout()
        self.backpropagation()
