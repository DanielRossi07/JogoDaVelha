from piece import Piece
from pieceType import PieceType
from boardPosition import BoardPosition


class Board:
    amount_of_rows = 3
    amount_of_columns = 3

    def __init__(self):
        self.__pieces_on_board = []
        self.__board = [
            [Piece(PieceType.d, row, col) for col in range(3)]
            for row in range(3)
        ]

    def draw_board(self):
        print("###################")
        for row in self.__board:
            print(" ".join(piece.type.value for piece in row))
        print("###################")

    def update_board(self):
        for piece in self.__pieces_on_board:
            self.__board[piece.position.row][piece.position.col] = piece
        self.draw_board()

    def add_piece_to_board(self, piece: Piece):
        self.__pieces_on_board.append(piece)
        self.update_board()

    def is_default_piece_on_position(self, position: BoardPosition):
        piece = self.__board[position.row][position.col]
        if piece.type == PieceType.d:
            return True
        return False

    def get_piece_on_position(self, position: BoardPosition):
        return self.get_piece_on_position(position.row, position.col)

    def get_piece_on_position(self, row: int, col: int):
        return self.__board[row][col]

    @property
    def board(self):
        return self.__board

    @staticmethod
    def is_default_piece(piece: Piece):
        if piece.type == PieceType.d:
            return True
        else:
            return False
