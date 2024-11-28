from board import Board
from services import Play


class StartGame:
    def __init__(self):
        self.board = Board()
        self.play = Play(self.board)

    @staticmethod
    def displayGameRules():
        print("Welcome to Nine Men's Morris!\n"
              "You play against the computer, your symbol is X and the computer is O. \n")

    def millFormedPlayer(self, chosenField):
        if self.play.checkIfMillOnBoard('X', chosenField):
            print("You have formed a mill!\n")
            pieceToRemove = input("Pick the piece you'd like to remove: ")
            self.play.removePieceFromBoard('X', pieceToRemove)

    def millFormedComputer(self, chosenField):
        if self.play.checkIfMillOnBoard('O', chosenField):
            print("The computer has formed a mill!\n"
                  "You will have one piece removed.\n")
            pieceToRemove = self.play.chooseOpponentPieceToRemove()
            self.play.removePieceFromBoard('O', pieceToRemove)
            print(f"The computer chose to remove your piece from field {pieceToRemove}")

    def start(self):
        self.displayGameRules()
        piecesToPlace = 9

        print(self.board)
        while piecesToPlace > 0:
            piecePlaced = False
            while not piecePlaced:
                try:
                    chosenField = input("Please pick a field: ")
                    self.play.makeAMove('X', chosenField)
                    print(self.board)
                    piecePlaced = True
                    self.millFormedPlayer(chosenField)

                except Exception as gameException:
                    print(gameException)

            computerMove = self.play.makeMoveNotRandom()
            print(f"The computer's move: {computerMove}")
            self.play.makeAMove('O', computerMove)
            self.millFormedComputer(computerMove)
            print(self.board)
            piecesToPlace -= 1

        print("Now you can move your pieces.\n")

        while True:
            pieceMoved = False
            while not pieceMoved:
                try:
                    pieceToMove = input("Please choose a piece to move: ")
                    fieldToMoveTo = input("Please choose a field to move to: ")
                    self.play.movePiece('X', pieceToMove, fieldToMoveTo)
                    print(self.board)
                    self.millFormedPlayer(fieldToMoveTo)
                    pieceMoved = True
                except Exception as moveException:
                    print(moveException)

            if self.play.getComputerPieces() < 3:
                print("You won the game!")
                break

            moves = self.play.choosePieceToMove()
            fieldToMoveFromByComputer = moves[0]
            fieldToMoveToByComputer = moves[1]

            print(f"The computer will move from {fieldToMoveFromByComputer} to {fieldToMoveToByComputer}")
            self.play.movePiece('O', fieldToMoveFromByComputer, fieldToMoveToByComputer)
            print(self.board)
            self.millFormedComputer(fieldToMoveToByComputer)

            if self.play.getPlayerPieces() < 3:
                print("You lost!")
                break


if __name__ == '__main__':
    nineMensMorris = StartGame()
    nineMensMorris.start()
