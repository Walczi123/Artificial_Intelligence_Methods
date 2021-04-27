from math import log, sqrt


class Node:
    def __init__(self, parent, move, state):
        self.wins = 0
        self.visits = 0
        self.parent = parent
        self.state = state
        self.child_nodes = []

    def select_UCT_child(self, c: float = sqrt(2)):
        return self.wins / self.visits + c * \
            sqrt(log(self.parent.visits) / self.visits)

    def add_child(self, move, state):
        self.child_nodes.append(Node(self, move, state))
