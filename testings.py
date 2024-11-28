import unittest
from services import Play
from board import Board


class MyTestCase(unittest.TestCase):

    def testReturnField(self):
        board = Board()
        playGame = Play(board)
        self.assertEqual(playGame.returnFieldChosenByComputer(0, 2), '1C')
        self.assertEqual(playGame.returnFieldChosenByComputer(0, 0), '1A')

    def testGetCharacterFromBoard(self):
        board = Board()
        self.assertEqual(board.getCharacterFromField(0, 0), '*')
        self.assertEqual(board.getCharacterFromField(0, 1), ' ')

    def testPlaceSymbol(self):
        board = Board()
        board.placeSymbol('@', 0, 1)
        self.assertEqual(board.getCharacterFromField(0, 1), '@')

    def testCheckForMillInRow(self):
        board = Board()
        board.placeSymbol('@', 3, 1)
        board.placeSymbol('@', 3, 2)
        board.placeSymbol('@', 3, 4)
        self.assertEqual(board.checkForMillInRow(3, '@', 1), False)
        board.placeSymbol('@', 0, 0)
        board.placeSymbol('@', 0, 3)
        board.placeSymbol('@', 0, 6)
        self.assertEqual(board.checkForMillInRow(0, '@', 0), True)

    def testCheckForMillInColumn(self):
        board = Board()
        board.placeSymbol('@', 1, 3)
        board.placeSymbol('@', 2, 3)
        board.placeSymbol('@', 4, 3)
        self.assertEqual(board.checkForMillInRow(1, '@', 3), False)

    def testGetAllAdjacentFields(self):
        board = Board()
        self.assertEqual(board.getAllAdjacentFieldsOfAField(0, 0), [[3, 0], [0, 3]])
        self.assertEqual(board.getAllAdjacentFieldsOfAField(3, 1), [[5, 1], [3, 2], [1, 1], [3, 0]])
        self.assertEqual(board.getAllAdjacentFieldsOfAField(6, 6), [[3, 6], [6, 3]])
        self.assertEqual(board.getAllAdjacentFieldsOfAField(3, 6), [[6, 6], [0, 6], [3, 5]])
        self.assertEqual(board.getAllAdjacentFieldsOfAField(0, 6), [[3, 6], [0, 3]])

    def testMakeAMove(self):
        board = Board()
        game = Play(board)
        game.makeAMove('@', '1A')
        self.assertEqual(board.getCharacterFromField(0, 0), '@')

    def testRemovePiece(self):
        board = Board()
        game = Play(board)
        game.makeAMove('@', '1A')
        game.removePieceFromBoard('$', '1A')
        self.assertEqual(board.getCharacterFromField(0, 0), '*')

    def testMovePiece(self):
        board = Board()
        game = Play(board)
        game.makeAMove('@', '1A')
        game.movePiece('@', '1A', '1D')
        self.assertEqual(board.getCharacterFromField(0, 0), '*')
        self.assertEqual(board.getCharacterFromField(0, 3), '@')

    def testPlacePieceComputer(self):
        board = Board()
        game = Play(board)
        game.makeAMove('X', '1A')
        game.makeAMove('X', '1D')
        game.makeMoveNotRandom()
        self.assertEqual(game.makeMoveNotRandom(), '1G')

    def testMovePieceComputer(self):
        board = Board()
        game = Play(board)
        game.makeAMove('X', '1A')
        game.makeAMove('X', '1D')
        game.makeAMove('O', '4G')
        self.assertEqual(game.choosePieceToMove(), ['4G', '1G'])


if __name__ == '__main__':
    unittest.main()
