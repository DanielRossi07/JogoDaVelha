from piece import Piece
from pieceType import PieceType
from random import randint


class Player:
    pieces: list[Piece]
    current_piece: Piece
    is_computer: bool = False

    def __init__(self, name: str, piece_type: str):
        self.name = name
        self.pieces = []
        self.pieceType = PieceType(piece_type)

    def play(self):
        row = None
        col = None

        while not row:
            row = input(f"{self.name}, qual a linha da sua próxima jogada? ")
            row = self.validate_input(row)

        while not col:
            col = input(f"{self.name}, qual a coluna da sua próxima jogada? ")
            col = self.validate_input(col)

        print("\n\n")
        self.current_piece = Piece(self.pieceType, row - 1, col - 1)

    @staticmethod
    def validate_input(_input: str) -> int or None:
        try:
            _input = int(_input)

            if _input > 3 or _input < 1:
                print("Precisa ser um número de 1 a 3")
                return None

            return _input
        except:
            print("Precisa ser um número")
            return None


class ComputerPlayer(Player):
    is_computer: bool = True

    def __init__(self, name: str, piece_type: str):
        super().__init__(name, piece_type)

    def play(self):
        row = randint(0, 2)
        col = randint(0, 2)

        self.current_piece = Piece(self.pieceType, row, col)
