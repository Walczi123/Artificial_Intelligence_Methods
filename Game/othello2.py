


def create_start_state():
    iteration_state = []
    for x in range(8):
        iteration_state.append([])
        for y in range(8):
            iteration_state[x].append(None)

    iteration_state[3][3] = 1
	iteration_state[3][4] = 0
	iteration_state[4][3] = 0
	iteration_state[4][4] = 1

    return iteration_state

def getAllPosibleMoves(iteration_state, player):
    moveList = []
    for x in range(8):
        for y in range(8):
                if valid(iteration_state, player,x,y)
                    moveList.append((x,y))
    return moveList

def boardMove(iteration_state, player,x,y):
    """ Moves to position and updates 'oldplacements' table
    """
    #Move and update self.g.screen
    oldplacements = iteration_state
    # print("something")
    if player%2 == 0 :
        oldplacements[x][y]=1 #change
    else:
        oldplacements[x][y]=0 #change
    iteration_state = move(iteration_state, player, x,y)
    
    #Switch Player
    self.g.switchPlayer()
    self.update()

def mustPass(iteration_state, player):
    """ 
    Tests if player must pass this round

    Returns:
        [type]: boolean
    """
    must_pass = True
    for x in range(8):
        for y in range(8):
            if valid(iteration_state, player,x,y):
                must_pass=False
    return must_pass

def move(iteration_state,  player, x, y):
		""" Make move and reverse all influenced oponnent's disks 

		Returns:
			[type]: array - board after move
		"""
		#Must copy the passedArray so we don't alter the original
		array = deepcopy(iteration_state)
		#Set colour and set the moved location to be that colour
		colour = player
		array[x][y] = colour
		
		#Determining the neighbours to the square
		neighbours = []
		for i in range(max(0,x-1),min(x+2,8)):
			for j in range(max(0,y-1),min(y+2,8)):
				if array[i][j]!=None:
					neighbours.append([i,j])
		
		#Which tiles to convert
		convert = []

		#For all the generated neighbours, determine if they form a line
		#If a line is formed, we will add it to the convert array
		for neighbour in neighbours:
			neighX = neighbour[0]
			neighY = neighbour[1]
			#Check if the neighbour is of a different colour - it must be to form a line
			if array[neighX][neighY]!=colour:
				#The path of each individual line
				path = []
				
				#Determining direction to move
				deltaX = neighX-x
				deltaY = neighY-y

				tempX = neighX
				tempY = neighY

				#While we are in the bounds of the board
				while 0<=tempX<=7 and 0<=tempY<=7:
					path.append([tempX,tempY])
					value = array[tempX][tempY]
					#If we reach a blank tile, we're done and there's no line
					if value==None:
						break
					#If we reach a tile of the player's colour, a line is formed
					if value==colour:
						#Append all of our path nodes to the convert array
						for node in path:
							convert.append(node)
						break
					#Move the tile
					tempX+=deltaX
					tempY+=deltaY
					
		#Convert all the appropriate tiles
		for i,j in convert:
			array[i][j]=colour

		return array


def checkForAnyLine(iteration_state, player, x, y, i, j):
    """ Check if move creates a line. 
        So if there is a line from (x,y) to another player's colored disk going through the neighbour (i,j), 
        where (i,j) has the opponent's color

    Args:
        colour ([type]): [description]
        x ([type]): move's x coordinate
        i ([type]): neighbour's x coordinate 

    Returns:
        [type]: boolean - true if it forms a correct line
    """
    neighX = i
    neighY = j
    
    #If the neighbour colour is equal to your colour, it doesn't form a line
    #Go onto the next neighbour
    if iteration_state[neighX][neighY]==colour:
        return False

    #Determine the direction of the line
    deltaX = neighX-x
    deltaY = neighY-y
    tempX = neighX
    tempY = neighY
    
    while 0<=tempX<=7 and 0<=tempY<=7:
        #If an empty space, no line is formed
        if iteration_state[tempX][tempY]==None:
            return False
        #If it reaches a piece of the player's colour, it forms a line
        if iteration_state[tempX][tempY]==colour:
            return True
        #Move the index according to the direction of the line
        tempX+=deltaX
        tempY+=deltaY
    return False

#Checks if a move is valid for a given array.
def valid(iteration_state, player, x, y):
    """ Check if placing disk on (x,y) is a valid move

    Args:
        player ([type]): [description]
        x ([type]): [description]
        y ([type]): [description]

    Returns:
        [type]: [description]
    """
    #Sets player colour
    colour = player
    #If there's already a piece there, it's an invalid move
    if iteration_state[x][y] != None:
        return False

    else:
        #Generating the list of neighbours
        neighbour = False
        neighbours = []
        valid = False
        for i in range(max(0,x-1),min(x+2,8)):
            for j in range(max(0,y-1),min(y+2,8)):
                if iteration_state[i][j]!=None:
                    neighbour=True
                    neighbours.append([i,j])
                    valid = valid or self.checkForAnyLine(iteration_state,colour, x, y, i, j)
        #If there's no neighbours, it's an invalid move
        if not neighbour:
            return False
        else:
            return valid