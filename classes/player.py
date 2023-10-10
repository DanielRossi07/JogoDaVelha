from piece import Piece
from pieceType import PieceType
import random


class Player:
    def __init__(self, name: str, piece_type: str):
        self.name = name
        self.pieces = []
        self.pieceType = PieceType(piece_type)
        self.current_piece = None
        self.is_computer = False

    def play(self):
        row, col = self.get_valid_move()
        self.current_piece = Piece(self.pieceType, row - 1, col - 1)

    def get_valid_move(self) -> tuple[int, int]:
        while True:
            row = input(f"{self.name}, qual a linha da sua próxima jogada? ")
            row = self.validate_input(row)
            if row:
                break

        while True:
            col = input(f"{self.name}, qual a coluna da sua próxima jogada? ")
            col = self.validate_input(col)
            if col:
                break

        return row, col

    @staticmethod
    def validate_input(_input: str) -> int:
        try:
            _input = int(_input)

            if 1 <= _input <= 3:
                return _input
            else:
                print("As coordenadas precisam estar entre 1 e 3.")
        except ValueError:
            print("As coordenadas precisam ser números inteiros.")


class ComputerPlayer(Player):
    def __init__(self, name: str, piece_type: str):
        super().__init__(name, piece_type)
        self.is_computer = True

    def play(self):
        row = random.randint(1, 3)
        col = random.randint(1, 3)
        self.current_piece = Piece(self.pieceType, row - 1, col - 1)