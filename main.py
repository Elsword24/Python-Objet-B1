<<<<<<< Updated upstream
#####################################################
#	Le code est écrit en anglais pour l"opensource	#
#			  Merci de continuer ainsi              #
#					  Jason                         #
#####################################################

def printGameBoard(gameBoard): # Display the gameBoard with score of players
	print("     ", end="")
	for u in range(len(gameBoard)):
		if u < 10:
			print("0" + str(u), end="  ")
		else:
			print(u, end="  ")
	print("")
	for x in range(len(gameBoard)): 
		if x < 10:
			print("0" + str(x), end=" ")
		else:
			print(str(x), end=" ")
		for y in range(len(gameBoard[x])):
			print("│ " + gameBoard[x][y], end=" ")
		if x < 10:
			print("│" + "0" + str(x))
		else:
			print("│" + str(x))
	print("     ", end="")
	for u in range(len(gameBoard)):
		if u < 10:
			print("0" + str(u), end="  ")
		else:
			print(u, end="  ")
	(xPieces, oPieces) = scorePlayer(gameBoard)


def scorePlayer(gameBoard): # counting pieces of players on gameBoard
	xPieces = 0 
	oPieces = 0 
	
	for x in gameBoard: 
		for y in x: 
			if y == "O": 
				xPieces += 1
			elif y == "X":
				oPieces += 1
	return (xPieces, oPieces)

def verifiedMoves(gameBoard, player): # Check all moves and verified them
	moves = [] # stock all verified possible moves 

	for x in range(len(gameBoard)):
		for y in range(len(gameBoard)):
			if possibleMove(gameBoard, y, x, player): 
				if len(piecesToFlip(gameBoard, x, y, player)) > 0: 
					moves.append((x, y))
	return moves

def possibleMove(gameBoard, r, c, player):
	return gameBoard[r][c] == " " 

def piecesIncluded(gameBoard, xStart, yStart, xDirection, yDirection, player): 
	included = [] # stock pieces to flip for all direction

	if player == "O":
		otherPlayer = "X"
	else:
		otherPlayer = "O"

	for distance in range(1, 8):
		xCurrent = xStart + distance * xDirection 
		yCurrent = yStart + distance * yDirection

		if xCurrent < 0 or xCurrent >= len(gameBoard) or yCurrent < 0 or yCurrent >= len(gameBoard):
			return [] 

		if gameBoard[yCurrent][xCurrent] == otherPlayer:
			included.append((xCurrent, yCurrent)) 
		elif gameBoard[yCurrent][xCurrent] == player:
			return included
		else:
			return [] 

	return [] 

def piecesToFlip(gameBoard, x, y, player): 
	flip = [] # stock pieces need to flip

	d = [-1,0,1]
	for dx in d:
		for dy in d:
			flip.extend((piecesIncluded(gameBoard, x, y, dx, dy, player))) # For all direction, check player pieces 

	return list(set(flip))

def flipPieces(gameBoard, flip, player): 
	for position in flip:
		gameBoard[position[1]][position[0]] = player # change pieces to player

	return gameBoard

def promptMove(gameBoard, player): # change player, see all possibilities and ask X, Y for play
	print(player + " turn!")
		
	possibilites = verifiedMoves(gameBoard, player) 

	if len(possibilites) == 0: # if nothing possibilities 
		return False

	xMove = -1
	yMove = -1

	while (xMove, yMove) not in possibilites:
		while xMove < 0 or xMove >= len(gameBoard):
			try:
				xMove = int(input("Enter a X coordinate (column) : "))
			except ValueError:
				xMove = -1

		while yMove < 0 or yMove >= len(gameBoard):
			try:
				yMove = int(input("Enter a Y coordinate (row) : "))
			except ValueError:
				yMove = -1
    
		if (xMove, yMove) not in possibilites:
			xMove = -1
			yMove = -1

	flip = piecesToFlip(gameBoard, xMove, yMove, player) 
	gameBoard[yMove][xMove] = player 

	gameBoard = flipPieces(gameBoard, flip, player) 

	os.system("cls")

	return gameBoard

def isgameBoardFull(gameBoard): 
	full = True

	for r in gameBoard:
		for c in r:
			if c == " ":
				full = False
	return full

def run(): 
	size = 0
	nbPlayer = 0

	while (size < 5) or (size > 30):
		try:
			size = int(input("Size of gameboard : "))
		except ValueError:
			size = 0

	while (nbPlayer < 2) or (nbPlayer > 4):
		try:
			nbPlayer = int(input("Number of player : "))
		except ValueError:
			nbPlayer = 0

	gameBoard = [] 
	for x in range(size):
		gameBoard.append([" "] * size) 
	
	gameBoard[3][3] = "X" 
	gameBoard[3][4] = "O"
	gameBoard[4][3] = "O"
	gameBoard[4][4] = "X"

	player = "O"
	otherPlayer = "X"

	while not isgameBoardFull(gameBoard):
		printGameBoard(gameBoard)

		if len(verifiedMoves(gameBoard, player)) == 0 and len(verifiedMoves(gameBoard, otherPlayer)) == 0: break

		tmp = promptMove(gameBoard, player) 
		if not tmp == False:
			gameBoard = tmp 
		(player, otherPlayer) = (otherPlayer, player)

	(xPieces, oPieces) = scorePlayer(gameBoard) 

	if xPieces > oPieces:
		print("O wins ! ")
	elif xPieces < oPieces:
		print("X wins ! ")
	else:
		print("Nobody wins ! ")

run() # run game
=======
def plateau(n):
    plateau=[]
    for i in range(0,n):
        lst=[]
        for y in range(0,n):
              lst.append(False)
        plateau.append(lst)
    return plateau
>>>>>>> Stashed changes
