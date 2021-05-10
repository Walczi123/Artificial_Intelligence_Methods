import random
from AI.node import Node

def MCTS( initialState, numberOfIteration):
    rootnode = Node(initialState)
    for _ in range(numberOfIteration):
        node = rootnode
        iteration_state = node.state

        #Selection
        while node.untriedMoves == [] and node.childNodes != []:
            node = node.SelectUctChild()

        #Expansion         
        if node.untriedMoves != []:
            move = random.choice(node.untried_moves)
            iteration_state.do_move(move)
            node = node.AddChild(iteration_state, move)

        #Playout
        while True:
            all_possible_moves = GetAllPosibleMoves(iteration_state)
            if all_possible_moves == []:
                break
            move = random.choice(all_possible_moves)
            iteration_state = StateAfterMove(iteration_state, move)
        
        #Backpropagation
        result = GetResult(iterationState)
        node.Backpropagation(result)
    
    return sorted(rootnode.child_nodes, key = lambda c: c.visits)[-1].move