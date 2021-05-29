from math import log, sqrt
from Game.othello2 import get_result, get_all_posible_moves, change_player

class Node:
    def __init__(self, parent, move, state, player, all_posible_moves = None):
        self.wins = 0
        self.visits = 0
        self.parent = parent
        self.state = state
        self.child_nodes = []
        self.player = player
        self.move = move
        if all_posible_moves is None:
            all_posible_moves = get_all_posible_moves(state, player)
        self.untried_moves = all_posible_moves

    def get_uct_score(self, c: float = sqrt(2)):
        return self.wins / self.visits + c * \
            sqrt(log(self.parent.visits) / self.visits) #TODO czy jeśli dziecko jest przeciwne to uct dalej powinno byc takiej samej wartości?

    def add_child(self, move, state, player):
        all_posible_moves = get_all_posible_moves(state, player)
        if all_posible_moves == []:
            p = change_player(player)
            all_posible_moves = get_all_posible_moves(state, player)
            if all_posible_moves != []:
                child = Node(self, move, state, p, all_posible_moves)
            else :
                child = Node(self, move, state, player, all_posible_moves)
        else:
            child = Node(self, move, state, player)

        self.child_nodes.append(child)
        return child

    def backpropagation(self, state):
        if get_result(state, self.player):
            self.wins += 1
        self.visits +=1
        if self.parent is not None:
            self.parent.backpropagation(state)


class RAVENode(Node):
    def __init__(self, parent, move, state, player):
        super(parent, move, state, player)
        self.rave_wins = 0
        self.rave_visits = 0

    def get_rave_score(self, k: int = 1000):
        b = sqrt(k/((3*self.visits)+k))
        return (b * (self.rave_wins/self.rave_visits)) + \
            ((1-b) * (self.wins/self.visits))

    def backpropagation(self, state, moves):
        if get_result(state, self.player):
            self.wins += 1
        self.visits +=1
        update_children = [child for child in self.child_nodes if (child.move, child.player) in moves]
        for child in update_children:
            if get_result(state, child.player):
                child.rave_wins += 1
            self.rave_visits +=1
        if self.parent is not None:
            self.parent.backpropagation(state)


class MASTNode(Node):
    def __init__(self, parent, move, state, player):
        super(parent, move, state, player)

    def get_mast_score(self, c: float = sqrt(2)):
        return self.wins / self.visits + c * sqrt(log(self.parent.visits) / self.visits)
