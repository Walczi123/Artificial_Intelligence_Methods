import random
from AI.nodes import Node
from Game.othello import get


def select_uct_child(childNodes):
    bestChildren = list()
    bestScore = - float("inf")

    for childNode in childNodes:
        score = childNode.get_uct_score()
        if score > bestScore:
            bestScore = score
            bestChildren = {childNode}
        elif score == bestScore:
            bestChildren.append(childNode)

    return bestChildren[random.Next(bestChildren.Count)]


def MCTS(initialState, numberOfIteration, Game):
    rootnode = Node(initialState)
    for _ in range(numberOfIteration):
        node = rootnode
        iteration_state = node.state

        # Selection
        while node.untriedMoves == [] and node.childNodes != []:
            node = select_uct_child(node.child_nodes)

        # Expansion
        if node.untriedMoves != []:
            move = random.choice(node.untried_moves)
            iteration_state.do_move(move)
            node = node.add_child(iteration_state, move)

        # Playout
        while True:
            all_possible_moves = Game.get_all_posible_moves(iteration_state)
            if all_possible_moves == []:
                break
            move = random.choice(all_possible_moves)
            iteration_state = Game.state_after_move(iteration_state, move)

        # Backpropagation
        result = GetResult(iterationState)
        node.Backpropagation(result)

    return sorted(rootnode.child_nodes, key=lambda c: c.visits)[-1].move
