from piece import Piece
from pieceType import PieceType
from boardPosition import BoardPosition


class Board:
    amount_of_rows = 3
    amount_of_columns = 3

    def __init__(self):
        self.__pieces_on_board = []
        self.__board = [[], [], []], \
                       [[], [], []], \
                       [[], [], []],
        self.init_board()

    def init_board(self):
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                default_piece = Piece(PieceType.d, row, col)
                self.__board[row][col].append(default_piece)

    def draw_board(self):
        print("###################")
        for row in self.__board:
            print(f"{row[0][0].type.value} {row[1][0].type.value} {row[2][0].type.value}")
        print("###################")

    def update_board(self):
        for piece in self.__pieces_on_board:
            self.__board[piece.position.row][piece.position.col][0] = piece
        self.draw_board()

    def add_piece_to_board(self, piece: Piece):
        self.__pieces_on_board.append(piece)
        self.update_board()

    def is_default_piece_on_position(self, position: BoardPosition):
        piece = self.__board[position.row][position.col][0]
        if piece.type == PieceType.d:
            return True
        return False

    def get_piece_on_position(self, position: BoardPosition):
        return self.get_piece_on_position(position.row, position.col)

    def get_piece_on_position(self, row: int, col: int):
        return self.__board[row][col][0]

    @property
    def board(self):
        return self.__board

    @staticmethod
    def is_default_piece(piece: Piece):
        if piece.type == PieceType.d:
            return True
        else:
            return False
