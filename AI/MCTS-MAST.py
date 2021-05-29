import random
from AI.nodes import MASTNode
from Game.othello2 import get_all_posible_moves, board_move, change_player, get_result, get_all_moves

def update_table(global_table, state, moves):
    for move in moves:
        if get_result(state, move[1]):
            global_table[move[0]][0] += 1
        global_table[move[0]][1] += 1

def get_mast_score(global_table, move):
    wins, visits = global_table(move)
    return wins/visits


def select_mast_child(global_table, childNodes):
    probabilities = list()

    for childNode in childNodes:
        probabilities.append(global_table(childNode.move))

    return random.choice(childNodes, 1, p=probabilities)


def MCTS(initial_state, player, number_of_iteration):
    rootnode = MASTNode(None, None, initial_state, player)
    moves = []
    global_table = dict()
    for move in get_all_moves(initial_state): #TODO Wszystkie czy wszystkie mozliwe
        global_table[move] = (0, 0) # 0, 0? 
    for _ in range(number_of_iteration):
        node = rootnode
        iteration_state = node.state

        # Selection
        while node.untried_moves == [] and node.child_nodes != []:
            node = select_mast_child(global_table, node.child_nodes)
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
                moves = [(node.move, node.player)]
                player = change_player(player)
                continue

            player = change_player(player)
            all_possible_moves = get_all_posible_moves(iteration_state, player)
            if  all_possible_moves != []:
                move = random.choice(all_possible_moves)
                board_move(iteration_state, player, move[0], move[1])
                moves = [(node.move, node.player)]
                player = change_player(player)
                continue

            break

        # Backpropagation
        update_table(global_table, iteration_state, moves)

    return sorted(rootnode.child_nodes, key=lambda c: c.visits)[-1].move
