from board import Board
from player import Player
from random import randint
from piece import Piece


class GameLogic:
    current_player = None
    winner = False
    tie = False

    def __init__(self, player1: Player, player2: Player, game_board: Board):
        self.player1 = player1
        self.player2 = player2
        self.game_board = game_board
        self.start()

    def start(self):
        self.draw_player()
        stop = False

        while not stop:
            self.next_player()
            self.current_player.play()

            while not self.register_play():
                if not self.current_player.is_computer:
                    print("Essa casa já está ocupada. Escolha outra...\n")
                self.current_player.play()

            print(f"{self.current_player.name} jogou...\n\n")

            self.verify_if_winner_or_tie()

            if self.winner:
                print(f"The winner is: {self.winner.name}")
                stop = True
            if self.tie:
                print("It is a tie!")
                stop = True

    def draw_player(self):
        number = randint(0, 1)
        if number == 0:
            self.current_player = self.player1
        else:
            self.current_player = self.player2

    def next_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def verify_if_winner_or_tie(self):
        self.verify_win_by_rows()
        self.verify_win_by_columns()
        self.verify_win_by_diagonal()
        self.verify_if_tie()

    def verify_win_by_rows(self):
        for row in self.game_board.board:
            last_piece = None
            row_winner = True
            for col in row:
                piece = col[0]
                if self.game_board.is_default_piece(piece):
                    row_winner = False
                    break

                if last_piece is None:
                    last_piece = piece
                    continue

                if piece.type != last_piece.type:
                    row_winner = False
                    break

            if row_winner:
                self.winner = self.current_player

    def verify_win_by_columns(self):
        for col in range(len(self.game_board.board)):
            last_piece = None
            col_winner = True
            for row in range(len(self.game_board.board)):
                piece = self.game_board.board[row][col][0]
                if self.game_board.is_default_piece(piece):
                    col_winner = False
                    break

                if last_piece is None:
                    last_piece = piece
                    continue

                if piece.type != last_piece.type:
                    col_winner = False
                    break

            if col_winner:
                self.winner = self.current_player

    def verify_win_by_diagonal(self):
        pass

    def verify_if_tie(self):
        pass

    def register_play(self):
        new_piece_position = self.current_player.current_piece.position
        if not self.game_board.is_default_piece_on_position(new_piece_position):
            return False

        self.game_board.add_piece_to_board(self.current_player.current_piece)
        return True
