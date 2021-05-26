from math import log, sqrt


class Node:
    def __init__(self, parent, move, state):
        self.wins = 0
        self.visits = 0
        self.parent = parent
        self.state = state
        self.child_nodes = []

    def get_uct_score(self, c: float = sqrt(2)):
        return self.wins / self.visits + c * \
            sqrt(log(self.parent.visits) / self.visits)

    def add_child(self, move, state):
        self.child_nodes.append(Node(self, move, state))


class RAVENode:
    def __init__(self, parent, move, state):
        self.wins = 0
        self.visits = 0
        self.rave_wins = 0
        self.rave_visits = 0
        self.parent = parent
        self.state = state
        self.child_nodes = []

    def get_rave_score(self, k: int = 1000):
        b = sqrt(k/((3*self.visits)+k))
        return (b * (self.rave_wins/self.rave_visits)) + \
            ((1-b) * (self.wins/self.visits))

    def add_child(self, move, state):
        self.child_nodes.append(Node(self, move, state))


class MASTNode:
    def __init__(self, parent, move, state):
        self.wins = 0
        self.visits = 0
        self.parent = parent
        self.state = state
        self.child_nodes = []

    def get_mast_score(self, c: float = sqrt(2)):
        return self.wins / self.visits + c * sqrt(log(self.parent.visits) / self.visits)

    def add_child(self, move, state):
        self.child_nodes.append(Node(self, move, state))
