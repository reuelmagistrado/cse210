from os import system
import random


class TicTacToe:
    """
    A class to represent a TicTacToe game.

    ...

    Methods
    -------
    create_board(size):
        Creates the tic tac toe board according to the size.

    get_random_first_player():
        Returns a random number between 0 and 1.

    mark_spot(row, col, player):
        Marks a cell with 'X' or 'O'.

    is_marked(row, col):
        Returns a boolean if the cell is marked or not.

    check_rows(player):
        Returns a boolean if a row is marked by a player.

    check_columns(player):
        Returns a boolean if a column is marked by a player.

    check_diagonals(player):
        Returns a boolean if a diagonal is marked by a player.

    is_player_win(player):
        Returns a boolean if a player has marked a row or a column or a diagonal.

    is_board_filled():
        Returns a boolean if the cells are all marked by the players.

    swap_player_turn(player):
        Returns a string of 'X' or 'O'.

    show_board():
        Outputs the board in the terminal.
    """

    def __init__(self):
        self.board = []

    def create_board(self, size):
        for _ in range(size):
            row = []
            for _ in range(size):
                row.append("-")
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def mark_spot(self, row, col, player):
        self.board[row][col] = player

    def is_marked(self, row, col):
        return self.board[row][col] != "-"

    def check_rows(self, player):
        # checking rows

        for row in range(len(self.board)):
            is_row_marked = True
            for column in range(len(self.board)):
                if self.board[row][column] != player:
                    is_row_marked = False
                    break

            if is_row_marked:
                return is_row_marked

    def check_columns(self, player):
        # checking columns
        for row in range(len(self.board)):
            is_column_marked = True
            for column in range(len(self.board)):
                if self.board[column][row] != player:
                    is_column_marked = False
                    break

            if is_column_marked:
                return is_column_marked

    def check_diagonals(self, player):
        # checking diagonals

        is_diagonal_marked = True
        for i in range(len(self.board)):
            if self.board[i][i] != player:
                is_diagonal_marked = False
                break
        if is_diagonal_marked:
            return True

        is_diagonal_marked = True
        for i in range(len(self.board)):
            if self.board[i][len(self.board)-1 - i] != player:
                is_diagonal_marked = False
                break

        if is_diagonal_marked:
            return True

        return False

    def is_player_win(self, player):

        has_won = True

        if self.check_rows(player) or self.check_columns(player) or self.check_diagonals(player):
            return has_won

        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == "-":
                    return False
        return True

    def swap_player_turn(self, player):
        return "X" if player == "O" else "O"

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
