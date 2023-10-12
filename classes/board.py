from piece import Piece
from pieceType import PieceType
from boardPosition import BoardPosition

import copy


class Board:
    board_size = 3

    def __init__(self):
        self.__pieces_on_board = []
        self.__board = [
            [Piece(PieceType.d, row, col) for col in range(3)]
            for row in range(3)
        ]

    def draw_board(self):
        print("###################")
        for row in self.board:
            print(" ".join(piece.type.value for piece in row))
        print("###################")

    def update_board(self):
        for piece in self.__pieces_on_board:
            self.board[piece.position.row][piece.position.col] = piece
        self.draw_board()

    def add_piece_to_board(self, piece: Piece):
        self.__pieces_on_board.append(piece)
        self.update_board()

    def is_default_piece_on_position(self, position: BoardPosition):
        piece = self.board[position.row][position.col]
        if piece.type == PieceType.d:
            return True
        return False

    def get_piece_on_position(self, position: BoardPosition):
        return self.get_piece_on_position(position.row, position.col)

    def get_piece_on_position(self, row: int, col: int):
        return self.board[row][col]

    @property
    def rows(self):
        return self.board

    @property
    def columns(self):
        cols = copy.deepcopy(self.__board)
        for row in range(self.board_size):
            for col in range(self.board_size):
                cols[col][row] = self.board[row][col]
        return cols

    @property
    def diagonals(self):
        diagonals = [[], []]

        for pos in range(self.board_size):
            diagonals[0].append(self.get_piece_on_position(pos, pos))
            diagonals[1].append(self.get_piece_on_position(pos, 2 - pos))
        return diagonals


    @property
    def board(self):
        return self.__board

    @staticmethod
    def is_default_piece(piece: Piece):
        if piece.type == PieceType.d:
            return True
        else:
            return False
