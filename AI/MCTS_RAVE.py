import random
from AI.nodes import RAVENode
from Game.othello2 import get_all_posible_moves, board_move, change_player


def select_rave_child(childNodes):
    bestChildren = list()
    bestScore = - float("inf")

    for childNode in childNodes:
        score = childNode.get_rave_score()
        if score > bestScore:
            bestScore = score
            bestChildren = {childNode}
        elif score == bestScore:
            bestChildren.append(childNode)

    return bestChildren[random.Next(bestChildren.Count)]

def MCTS_RAVE(initial_state, player, number_of_iteration):
    rootnode = RAVENode(None, None, initial_state, player)
    for _ in range(number_of_iteration):
        node = rootnode
        iteration_state = node.state
        moves = []

        # Selection
        while node.untried_moves == [] and node.child_nodes != []:
            node = select_rave_child(node.child_nodes)
            moves = [(node.move, node.player)]
            

        # Expansion
        if node.untried_moves != []:
            move = random.choice(node.untried_moves)
            _, iteration_state = board_move(iteration_state, node.player, move[0], move[1])
            node = node.add_child(move, iteration_state, change_player(node.player))
            moves = [(node.move, node.player)]

        # Playout
        player = node.player
        while True:          
            all_possible_moves = get_all_posible_moves(iteration_state, player)
            if  all_possible_moves != []:
                move = random.choice(all_possible_moves)
                _, iteration_state = board_move(iteration_state, player, move[0], move[1])
                moves = [(move, player)]
                player = change_player(player)
                continue

            player = change_player(player)
            all_possible_moves = get_all_posible_moves(iteration_state, player)
            if  all_possible_moves != []:
                move = random.choice(all_possible_moves)
                _, iteration_state = board_move(iteration_state, player, move[0], move[1])
                moves = [(move, player)]
                player = change_player(player)
                continue

            break

        # Backpropagation
        node.backpropagation(iteration_state, moves)

    return sorted(rootnode.child_nodes, key=lambda c: c.visits)[-1].move