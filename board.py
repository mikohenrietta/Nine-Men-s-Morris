from texttable import Texttable


class Board:
    def __init__(self):
        self.__width = 7
        self.__height = 7
        self.__board = [[' ' for row in range(self.__width)] for column in range(self.__height)]
        self.__initialiseBoard()

    def __str__(self):
        visualBoard = Texttable()
        row = ['/']
        for currentRow in range(self.__height):
            row.append(chr(ord('A') + currentRow))

        visualBoard.header(row)

        for currentColumn in range(self.__width):
            visualBoard.add_row([currentColumn + 1] + self.__board[currentColumn])

        return visualBoard.draw()

    def __initialiseBoard(self):
        fields = [[0, 0], [0, 3], [0, 6], [1, 1], [1, 3], [1, 5], [2, 2], [2, 3], [2, 4],
                          [3, 0], [3, 1], [3, 2], [3, 4], [3, 5], [3, 6], [4, 2], [4, 3], [4, 4],
                          [5, 1], [5, 3], [5, 5], [6, 0], [6, 3], [6, 6]]
        for field in fields:
            row, col = field
            self.__board[row][col] = '*'

    def getCharacterFromField(self, row, column):
        return self.__board[row][column]

    def placeSymbol(self, symbol, row, column):
        self.__board[row][column] = symbol

    def checkForMillInRow(self, row, symbol, column):
        piecesPlaced = 0
        threePiecesInARow = 3
        if row == threePiecesInARow:
            if (column < threePiecesInARow and self.__board[3][0] == symbol and self.__board[3][1] == symbol and
                    self.__board[3][2] == symbol):
                return True
            elif (column > threePiecesInARow and self.__board[3][4] == symbol and self.__board[3][5] == symbol and
                  self.__board[3][6] == symbol):
                return True

        else:
            for currentColumn in range(0, self.__width):
                if self.__board[row][currentColumn] == symbol:
                    piecesPlaced += 1
            if piecesPlaced == threePiecesInARow:
                return True
        return False

    def checkForMillInColumn(self, column, symbol, row):
        threePiecesInARow = 3
        piecesPlaced = 0
        if column == threePiecesInARow:
            if (row < threePiecesInARow and self.__board[0][3] == symbol and self.__board[1][3] == symbol and
                    self.__board[2][3] == symbol):
                return True
            elif (row > threePiecesInARow and self.__board[4][3] == symbol and self.__board[5][3] == symbol and
                  self.__board[6][3] == symbol):
                return True
        else:
            for currentRow in range(0, self.__height):
                if self.__board[currentRow][column] == symbol:
                    piecesPlaced += 1
            if piecesPlaced == threePiecesInARow:
                return True

    def deletePiece(self, rowToDelete, columnToDelete):
        self.__board[rowToDelete][columnToDelete] = '*'

    def getPiecesNumber(self, symbol):
        numberOfPieces = 0
        for currentRow in range(0, self.__height):
            for currentColumn in range(0, self.__width):
                if self.__board[currentRow][currentColumn] == symbol:
                    numberOfPieces += 1

        return numberOfPieces

    def checkIfAdjacentFieldsHaveSameSymbolRow(self, symbol, startColumn, endColumn, rowToCheck):
        for currentColumn in range(startColumn, endColumn):
            if self.__board[rowToCheck][currentColumn] != symbol or self.__board[rowToCheck][currentColumn] != ' ':
                return False
        return True

    def checkIfAdjacentFieldsHaveSameSymbolColumn(self, symbol, startRow, endRow, columnToCheck):
        for currentRow in range(startRow, endRow):
            if self.__board[currentRow][columnToCheck] != symbol or self.__board[currentRow][columnToCheck] != ' ':
                return False
        return True

    def getAllFieldsOccupiedByCharacter(self, symbol):
        listWithFields = []
        for currentRow in range(0, self.__width):
            for currentColumn in range(0, self.__height):
                if self.__board[currentRow][currentColumn] == symbol:
                    listWithFields.append([currentRow, currentColumn])

        return listWithFields

    def checkIfAdjacentFieldsInRow(self, row, firstColumn, secondColumn):
        adjacent = True
        if firstColumn < secondColumn:
            columnToCheck = firstColumn + 1
        else:
            columnToCheck = secondColumn + 1
        while adjacent and columnToCheck < secondColumn:
            if self.__board[row][columnToCheck] != ' ':
                return False
            columnToCheck += 1

        return True

    def checkIfAdjacentFieldsInColumn(self, column, firstRow, secondRow):
        adjacent = True
        if firstRow < secondRow:
            rowToCheck = firstRow + 1
        else:
            rowToCheck = secondRow + 1

        while adjacent and rowToCheck < secondRow:
            if self.__board[rowToCheck][column] != ' ':
                return False
            rowToCheck += 1

        return True

    def getAllAdjacentFieldsOfAField(self, rowOfField, columnOfField):
        listWithFields = []
        rowToCheck = rowOfField
        columnToCheck = columnOfField
        if rowToCheck < self.__height - 1:
            rowToCheck += 1
            while self.__board[rowToCheck][columnToCheck] == ' ' and rowToCheck < self.__width - 1:
                rowToCheck += 1
            if self.__board[rowToCheck][columnToCheck] == '*':
                listWithFields.append([rowToCheck, columnToCheck])

        rowToCheck = rowOfField
        columnToCheck = columnOfField
        if columnToCheck < self.__width - 1:
            columnToCheck += 1
            while self.__board[rowToCheck][columnToCheck] == ' ' and columnToCheck < self.__height - 1:
                columnToCheck += 1

            if self.__board[rowToCheck][columnToCheck] == '*':
                listWithFields.append([rowToCheck, columnToCheck])

        rowToCheck = rowOfField - 1
        columnToCheck = columnOfField
        while self.__board[rowToCheck][columnToCheck] == ' ' and rowToCheck >= 0:
            rowToCheck -= 1

        if self.__board[rowToCheck][columnToCheck] == '*' and rowToCheck > -1:
            listWithFields.append([rowToCheck, columnToCheck])

        rowToCheck = rowOfField
        columnToCheck = columnOfField - 1
        while self.__board[rowToCheck][columnToCheck] == ' ' and columnToCheck >= 0:
            columnToCheck -= 1
        if self.__board[rowToCheck][columnToCheck] == '*' and columnToCheck > -1:
            listWithFields.append([rowToCheck, columnToCheck])

        return listWithFields

    def getAllFreeFields(self):
        listWithFields = []
        for currentRow in range(0, self.__width):
            for currentColumn in range(0, self.__height):
                if self.__board[currentRow][currentColumn] == '*':
                    listWithFields.append([currentRow, currentColumn])

        return listWithFields
