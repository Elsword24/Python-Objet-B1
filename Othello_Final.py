from aenum import Enum
from dataclasses import dataclass

# Classe Case (Enum) 
class Box(Enum):
    emptySpace = "."

    # Classe Pion (Enum)
    class Pawn(Enum):
        firstPlayer = "0"
        secondPlayer = "X"

        # @Property c'est pour retourner une valeur, utilisation de opponentPlayer pour savoir l'adversaire
        @property
        def opponentPlayer(self):
            if self == Box.Pawn.firstPlayer:
                return Box.Pawn.secondPlayer
            else:
                return Box.Pawn.firstPlayer

# @dataclass c'est une struct (une classe de données)
@dataclass
class Coordinate:
    x: int
    y: int

# cette classe c'est pour stocker les coordonnées d'une diagonale et changer les pions si nécessaire
@dataclass
class Diagonal:
    coordinates: [Coordinate]
    positionToChange: (int, int)

# Cette classe est sert à remplacer les pions à retourner
@dataclass
class ReplaceAxe:
    row: (int, int)
    col: (int, int)
    diagonalFromLeft: Diagonal
    diagonalFromRight: Diagonal

# Cette classe sert à afficher le plateau, vérifier les pions et les changer
class Board:

    board = [[str]] # plateau
    maxSize: int # Taille max du plateau

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.board = self.getInitBoard()

        # Les coordonnées par default des pions centraux
        halfMaxSize = int(maxSize / 2)
        self.addPositionPlayer(coordinate=Coordinate(
            x=halfMaxSize, y=halfMaxSize), pawn=Box.Pawn.firstPlayer)
        self.addPositionPlayer(coordinate=Coordinate(
            x=halfMaxSize, y=halfMaxSize - 1), pawn=Box.Pawn.secondPlayer)
        self.addPositionPlayer(coordinate=Coordinate(
            x=halfMaxSize - 1, y=halfMaxSize), pawn=Box.Pawn.secondPlayer)
        self.addPositionPlayer(coordinate=Coordinate(
            x=halfMaxSize - 1, y=halfMaxSize - 1), pawn=Box.Pawn.firstPlayer)

        self.drawBoard()

    ##### Dessiner le plateau
    def getInitBoard(self):
        return [[Box.emptySpace.value for j in range(self.maxSize)] for i in range(self.maxSize)]

    def drawBoard(self):
        xGrad = self.getGraduation(size=self.maxSize, offset=1) # Recuperer les noms des abscisses 
        yGrad = self.getGraduation(size=self.maxSize + 1, start=1) # Recuperer les noms des ordonnées

        finalBoard: [[str]] = [xGrad] + list(map(lambda i: [yGrad[i[0]]] + i[1], enumerate(self.board))) # abscisses + dans chaque 1er ligne du plateau on met une ordonnée

        for row in finalBoard:
            print(*row)

    def getGraduation(self, size: int, start: int = 0, offset: int = 0):
        numbers = range(start, size + offset)
        return list(map(lambda i: " " if (i == 0) else str(i), numbers))

    ##### Change Position des pions
    def addPositionPlayer(self, coordinate: Coordinate, pawn: Box.Pawn):
        self.board[coordinate.x][coordinate.y] = pawn.value

    def setEmptyPosition(self, coordinate: Coordinate):
        self.board[coordinate.x][coordinate.y] = Box.emptySpace.value

    #### Position

    # Cette fonction sert à valider la position du pion et les coordonnées compris dans le min et max du plateau
    def isValidPawnPosition(self, x: int, y: int, pawn: Box.Pawn) -> bool:
        def isOutOfIndex(position: int) -> bool:
            return position < 0 or position >= self.maxSize

        if isOutOfIndex(x) or isOutOfIndex(y):
            return False

        if self.board[x][y] != Box.emptySpace.value:
            return False

        return True

    # Cette fonction vérifie si le pion est entre un pion adverse (ex: X 0 X ou 0 X X 0....)
    def getPositionToReplace(self, array: [str], pawn: Box.Pawn) -> (int, int):
        rangePosition: (int, int) = None

        for (index, value) in enumerate(array):
            if value == pawn.value:
                if rangePosition != None and rangePosition[0] != None and rangePosition[0] + 1 != index:
                    return (rangePosition[0], index)
                rangePosition = (index, 0)

            if value == Box.emptySpace.value:
                rangePosition = None

        return None

    # Cette fonction recupere toute la ligne, colonne et diagonale (diagonal à droite et à gauche)
    def findPositionsToReplace(self, coordinate: Coordinate, pawn: Box.Pawn) -> ReplaceAxe:
        # Récuperer les positions X
        row = self.board[coordinate.x]
        rangeXPosition = self.getPositionToReplace(array=row, pawn=pawn)

        # Récuperer les positions Y
        cols = list(map(lambda col: col[coordinate.y], self.board))
        rangeYPosition = self.getPositionToReplace(array=cols, pawn=pawn)

        # Récuperer les diagonales
        x = coordinate.x
        y = coordinate.y

        leftNegativeDia: [Coordinate] = []
        leftPositifDia: [Coordinate] = []
        rightNegativeDia: [Coordinate] = []
        rightPositifDia: [Coordinate] = []

        for i in range(1, self.maxSize - 1):
            if x + i <= (self.maxSize - 1) and y + i <= (self.maxSize - 1):  # R - 1
                rightNegativeDia.append(Coordinate(x=x + i, y=y + i))

            if (x - i) >= 0 and (y - i) >= 0:  # L + 1
                leftPositifDia.append(Coordinate(x=x - i, y=y - i))

            if (x - i) >= 0 and y + i <= (self.maxSize - 1):  # R + 1
                rightPositifDia.append(Coordinate(x=x - i, y=y + i))

            if x + i <= (self.maxSize - 1) and (y - i) >= 0:  # L - 1
                leftNegativeDia.append(Coordinate(x=x + i, y=y - i))

        def getBoxFrom(coordinate: Coordinate) -> str:
            return self.board[coordinate.x][coordinate.y]
        
        # ça fusionne la diagonale montante et descendant et avec votre pion jouer
        rightDiagonalCoordinates = rightPositifDia + [coordinate] + leftNegativeDia
        rightDiagonalPositionToChange = self.getPositionToReplace(
            array=list(map(lambda coordinate: getBoxFrom(
                coordinate), rightDiagonalCoordinates)),
            pawn=pawn)

        leftDiagonalCoordinates = leftPositifDia + [coordinate] + rightNegativeDia
        leftDiagonalPositionToChange = self.getPositionToReplace(
            array=list(map(lambda coordinate: getBoxFrom(
                coordinate), leftDiagonalCoordinates)),
            pawn=pawn)

        return ReplaceAxe(
            row=rangeXPosition,
            col=rangeYPosition,
            diagonalFromLeft=Diagonal(
                coordinates=leftDiagonalCoordinates, positionToChange=leftDiagonalPositionToChange),
            diagonalFromRight=Diagonal(coordinates=rightDiagonalCoordinates, positionToChange=rightDiagonalPositionToChange))

    # Replacement d'un pion
    def replacePawn(self, replaceAxe: ReplaceAxe, coordinate: Coordinate, pawn: Box.Pawn):

        if replaceAxe.row != None:
            for i in range(replaceAxe.row[0], replaceAxe.row[1]):
                self.board[coordinate.x][i] = pawn.value

        if replaceAxe.col != None:
            for i in range(replaceAxe.col[0], replaceAxe.col[1]):
                self.board[i][coordinate.y] = pawn.value

        diagLeft = replaceAxe.diagonalFromLeft.positionToChange
        if diagLeft != None:
            for i in range(diagLeft[0], diagLeft[1]):
                coor = replaceAxe.diagonalFromLeft.coordinates[i]
                self.board[coor.x][coor.y] = pawn.value

        diagRight = replaceAxe.diagonalFromRight.positionToChange
        if diagRight != None:
            for i in range(diagRight[0], diagRight[1]):
                coor = replaceAxe.diagonalFromRight.coordinates[i]
                self.board[coor.x][coor.y] = pawn.value

    # action lorsque le joueur joue
    def playerMoveAction(self, position: (int, int), pawn: Box.Pawn) -> bool:
        x = position[0] - 1
        y = position[1] - 1

        if not self.isValidPawnPosition(x=x, y=y, pawn=pawn):
            print("Votre Position : ",
                  position[0], ",", position[1], " n'est pas valide !")
            return False

        coordinate = Coordinate(x=x, y=y)
        self.addPositionPlayer(coordinate=coordinate, pawn=pawn)

        replaceAxe = self.findPositionsToReplace(
            coordinate=coordinate, pawn=pawn)

        # Vérifier s'il y a une position à remplacer, sinon on suppime le pion en cours du joueur
        if (replaceAxe.col == None and replaceAxe.row == None and
                replaceAxe.diagonalFromLeft.positionToChange == None and replaceAxe.diagonalFromRight.positionToChange == None):
            self.setEmptyPosition(coordinate=coordinate)
            print("Votre Position : ",
                  position[0], ",", position[1], " n'est pas valide !")
            return False

        self.replacePawn(replaceAxe=replaceAxe,
                         coordinate=coordinate, pawn=pawn)

        self.drawBoard()
        return True

    def isPawnWin(self, pawn: Box.Pawn) -> bool:
        for row in self.board:
            if pawn.opponentPlayer.value in row:
                return False
        return True

# Class Partie


class Game:
    board = [[str]]

    def __init__(self):
        bordMaxSize = int(
            input("Veuillez entrer la taille du tableau : "))
        self.board = Board(maxSize=bordMaxSize)
        self.askPlayerPostion(pawn=Box.Pawn.firstPlayer)

    def askPlayerPostion(self, pawn: Box.Pawn):
        playerName = "premier" if pawn == Box.Pawn.firstPlayer else "deuxième"
        print("\n C'est au", playerName,
              "joueur de jouer (pion", pawn.value, ")")
        row = int(input("\n Entrer une ligne : "))
        col = int(input("Entrer une colonne : "))

        isValid = self.board.playerMoveAction(position=(row, col), pawn=pawn)

        if isValid and self.board.isPawnWin(pawn=pawn):
            print("Le joueur", playerName, "a gagné !")
            return

        self.askPlayerPostion(pawn.opponentPlayer if isValid else pawn)


if __name__ == '__main__':
    g = Game()

