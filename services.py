from board import Board
import random


class Play:
    def __init__(self, gameBoard: Board):
        self.board = gameBoard

    def makeAMove(self, symbol, field):
        rowToMoveTo = self.getRow(field)
        columnToMoveTo = self.getColumn(field)
        self.checkIfValidFieldToMoveTo(rowToMoveTo, columnToMoveTo)
        self.board.placeSymbol(symbol, rowToMoveTo, columnToMoveTo)

    def removePieceFromBoard(self, symbol, field):
        rowToDelete = self.getRow(field)
        columnToDelete = self.getColumn(field)
        self.checkIfValidPieceToRemove(rowToDelete, columnToDelete, symbol)
        self.board.deletePiece(rowToDelete, columnToDelete)

    def movePiece(self, symbol, pieceToMove, fieldToMoveTo):
        row = self.getRow(pieceToMove)
        column = self.getColumn(pieceToMove)
        rowToMoveTo = self.getRow(fieldToMoveTo)
        columnToMoveTo = self.getColumn(fieldToMoveTo)
        if row == rowToMoveTo:
            if not self.board.checkIfAdjacentFieldsInRow(row, column, columnToMoveTo):
                raise Exception("Fields must be adjacent!")
        elif column == columnToMoveTo:
            if not self.board.checkIfAdjacentFieldsInColumn(column, row, rowToMoveTo):
                raise Exception("Fields must be adjacent!")
        else:
            raise Exception("Fields must be in the same row or column!")
        self.board.deletePiece(row, column)
        self.makeAMove(symbol, fieldToMoveTo)

    @staticmethod
    def getRow(field):
        rowToMoveTo = int(field[0]) - 1
        return rowToMoveTo

    @staticmethod
    def getColumn(field):
        columnToMoveTo = ord(field[1]) - ord('A')
        return columnToMoveTo

    def getPlayerPieces(self):
        return self.board.getPiecesNumber('X')

    def getComputerPieces(self):
        return self.board.getPiecesNumber('O')

    def checkIfValidFieldToMoveTo(self, row, column):
        if self.board.getCharacterFromField(row, column) == ' ':
            raise Exception("You can only move to a field marked with *")
        if self.board.getCharacterFromField(row, column) == 'X' or self.board.getCharacterFromField(row, column) == 'O':
            raise Exception("That field is already occupied!")
        return True

    def checkIfMillOnBoard(self, symbol, field):
        row = self.getRow(field)
        column = self.getColumn(field)

        if self.board.checkForMillInRow(row, symbol, column) or self.board.checkForMillInColumn(column, symbol, column):
            return True

        return False

    def checkIfValidPieceToRemove(self, row, column, symbol):
        if self.board.getCharacterFromField(row, column) == ' ' or self.board.getCharacterFromField(row, column) == '*':
            raise Exception("Not valid field to remove!")
        if self.board.getCharacterFromField(row, column) == symbol:
            raise Exception("You can't remove your own piece!")
        return True

    @staticmethod
    def returnFieldChosenByComputer(row, column):
        field = str(row+1) + chr(column + ord('A'))
        return field

    def chooseOpponentPieceToRemove(self):
        listWithPieces = self.board.getAllFieldsOccupiedByCharacter('X')
        chosenField = random.choice(listWithPieces)
        rowChosen = chosenField[0]
        columnChosen = chosenField[1]
        fieldToReturn = self.returnFieldChosenByComputer(rowChosen, columnChosen)
        return fieldToReturn

    def makeMoveNotRandom(self):
        listWithAvailableFields = self.board.getAllFreeFields()
        for currentField in listWithAvailableFields:
            rowOfCurrentField = currentField[0]
            columnOfCurrentField = currentField[1]
            self.board.placeSymbol('X', rowOfCurrentField, columnOfCurrentField)
            if self.board.checkForMillInRow(rowOfCurrentField, 'X',
                                            columnOfCurrentField) or self.board.checkForMillInColumn(
                    columnOfCurrentField, 'X', rowOfCurrentField):
                self.board.deletePiece(rowOfCurrentField, columnOfCurrentField)
                return self.returnFieldChosenByComputer(rowOfCurrentField, columnOfCurrentField)

            self.board.deletePiece(rowOfCurrentField, columnOfCurrentField)

        for currentField in listWithAvailableFields:
            rowOfCurrentField = currentField[0]
            columnOfCurrentField = currentField[1]
            self.board.placeSymbol('O', rowOfCurrentField, columnOfCurrentField)
            if self.board.checkForMillInRow(rowOfCurrentField, 'O',
                                            columnOfCurrentField) or self.board.checkForMillInColumn(
                    columnOfCurrentField, 'O', rowOfCurrentField):
                self.board.deletePiece(rowOfCurrentField, columnOfCurrentField)
                return self.returnFieldChosenByComputer(rowOfCurrentField, columnOfCurrentField)
            self.board.deletePiece(rowOfCurrentField, columnOfCurrentField)

        for currentField in listWithAvailableFields:
            rowOfCurrentField = currentField[0]
            columnOfCurrentField = currentField[1]
            adjacentFields = self.board.getAllAdjacentFieldsOfAField(rowOfCurrentField, columnOfCurrentField)
            if adjacentFields is not None:
                for currentAdjacentField in adjacentFields:
                    if self.board.getCharacterFromField(currentAdjacentField[0], currentAdjacentField[1]) == 'O':
                        return self.returnFieldChosenByComputer(currentAdjacentField[0], currentAdjacentField[1])

        chosenField = random.choice(listWithAvailableFields)
        return self.returnFieldChosenByComputer(chosenField[0], chosenField[1])

    def choosePieceToMove(self):
        listWithPieces = self.board.getAllFieldsOccupiedByCharacter('O')

        for currentPiece in listWithPieces:
            rowOfPiece = currentPiece[0]
            columnOfPiece = currentPiece[1]
            listWithAdjacentFields = self.board.getAllAdjacentFieldsOfAField(rowOfPiece, columnOfPiece)

            for currentAdjacentField in listWithAdjacentFields:
                rowOfAdjacentField = currentAdjacentField[0]
                columnOfAdjacentField = currentAdjacentField[1]
                self.board.placeSymbol('X', rowOfAdjacentField, columnOfAdjacentField)
                if (self.board.checkForMillInRow(rowOfAdjacentField, 'X', columnOfAdjacentField) or
                        self.board.checkForMillInColumn(columnOfAdjacentField, 'X', rowOfAdjacentField)):
                    self.board.deletePiece(rowOfAdjacentField, columnOfAdjacentField)
                    return [self.returnFieldChosenByComputer(rowOfPiece, columnOfPiece),
                            self.returnFieldChosenByComputer(rowOfAdjacentField, columnOfAdjacentField)]
                self.board.deletePiece(rowOfAdjacentField, columnOfAdjacentField)

            for currentAdjacentField in listWithAdjacentFields:
                rowOfAdjacentField = currentAdjacentField[0]
                columnOfAdjacentField = currentAdjacentField[1]
                self.board.placeSymbol('O', rowOfAdjacentField, columnOfAdjacentField)
                if (self.board.checkForMillInRow(rowOfAdjacentField, 'O', columnOfAdjacentField) or
                        self.board.checkForMillInColumn(columnOfAdjacentField, 'O', rowOfAdjacentField)):
                    self.board.deletePiece(rowOfAdjacentField, columnOfAdjacentField)
                    return [self.returnFieldChosenByComputer(rowOfPiece, columnOfPiece),
                            self.returnFieldChosenByComputer(rowOfAdjacentField, columnOfAdjacentField)]
                self.board.deletePiece(rowOfAdjacentField, columnOfAdjacentField)

            chosenFieldToMoveTo = random.choice(listWithAdjacentFields)
            return [self.returnFieldChosenByComputer(rowOfPiece, columnOfPiece),
                    self.returnFieldChosenByComputer(chosenFieldToMoveTo[0], chosenFieldToMoveTo[1])]
