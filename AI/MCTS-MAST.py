import random
from AI.nodes import MASTNode


def get_mast_score(global_table, move):
    wins, visits = global_table(move)
    return wins/visits


def select_mast_child(global_table, childNodes):
    bestChildren = list()
    bestScore = - float("inf")

    for childNode in childNodes:
        wins, visits = global_table(childNode.move)
        score = wins/visits
        if score > bestScore:
            bestScore = score
            bestChildren = {childNode}
        elif score == bestScore:
            bestChildren.append(childNode)

    return bestChildren[random.Next(bestChildren.Count)]


def MCTS_MAST(initialState, numberOfIteration):
    global_table = dict()
    for move in all_moves():
        global_table[move] = (0, 0)
    rootnode = MASTNode(initialState)
    for _ in range(numberOfIteration):
        node = rootnode
        iteration_state = node.state

        # Selection
        while node.untriedMoves == [] and node.childNodes != []:
            node = select_mast_child(global_table, node.child_nodes)

        # Expansion
        if node.untriedMoves != []:
            move = random.choice(node.untried_moves)
            iteration_state.do_move(move)
            node = node.AddChild(iteration_state, move)

        # Playout
        while True:
            all_possible_moves = GetAllPosibleMoves(iteration_state)
            if all_possible_moves == []:
                break
            move = random.choice(all_possible_moves)
            iteration_state = StateAfterMove(iteration_state, move)

        # Backpropagation
        result = GetResult(iterationState)
        node.Backpropagation(result)

    return sorted(rootnode.child_nodes, key=lambda c: c.visits)[-1].move
