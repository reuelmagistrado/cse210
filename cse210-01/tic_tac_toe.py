from os import system
import random

__assignment__ = "Week 1: Tic-Tac-Toe"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


class TicTacToe:
    """
    A class to represent a TicTacToe game.

    ...

    Methods
    -------
    create_board(size):
        Creates the tic tac toe board according to the size.

    get_random_first_player():
        Returns 0 or 1.

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
        """Constructs all the necessary attributes for the TicTacToe object."""

        self.board = []

    def create_board(self, size: int):
        """Creates the tic tac toe board according to the size.

        Parameters
        ----------
        size: int
            Size chosen of the user for the board.
        """

        for _ in range(size):
            row = []
            for _ in range(size):
                row.append("-")
            self.board.append(row)

    def get_random_first_player(self):
        """Returns 0 or 1."""

        return random.randint(0, 1)

    def mark_spot(self, row: int, col: int, player: str):
        """Marks a cell with 'X' or 'O'.

        Parameters
        ----------
        row: int
            Row number for marking the cell.
        col: int
            Column number for marking the cell.
        player: str
            A string of 'X' or 'O'.
        """

        self.board[row][col] = player

    def is_marked(self, row: int, col: int) -> bool:
        """Returns a boolean if the cell is marked or not.

        Parameters
        ----------
        row: int
            Row number for marking the cell.
        col: int
            Column number for marking the cell.

        Returns
        -------
        True - if the cell in the board is marked by 'X' or 'O'

        False - if the cell in the board is empty
        """

        return self.board[row][col] != "-"

    def check_rows(self, player: str) -> bool:
        """Returns a boolean if a row is marked by a player.

        Parameters
        ----------
        player: str
            A string of either 'X' or 'O'.
        """

        for row in range(len(self.board)):
            is_row_marked = True
            for column in range(len(self.board)):
                if self.board[row][column] != player:
                    is_row_marked = False
                    break

            if is_row_marked:
                return is_row_marked

    def check_columns(self, player: str) -> bool:
        """Returns a boolean if a column is marked by a player.

        Parameters
        ----------
        player: str
            A string of either 'X' or 'O'.
        """

        for row in range(len(self.board)):
            is_column_marked = True
            for column in range(len(self.board)):
                if self.board[column][row] != player:
                    is_column_marked = False
                    break

            if is_column_marked:
                return is_column_marked

    def check_diagonals(self, player: str) -> bool:
        """Returns a boolean if a diagonal is marked by a player.

        Parameters
        ----------
        player: str
            A string of either 'X' or 'O'.
        """

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

    def is_player_win(self, player: str) -> bool:
        """Returns a boolean if a player has marked a row or a column or a diagonal.

        Parameters
        ----------
        player: str
            A string of either 'X' or 'O'.
        """

        has_won = True
        if self.check_rows(player) or self.check_columns(player) or self.check_diagonals(player):
            return has_won

        return False

    def is_board_filled(self):
        """Returns a boolean if the cells are all marked by the players."""

        for row in self.board:
            for item in row:
                if item == "-":
                    return False

        return True

    def swap_player_turn(self, player: str) -> str:
        """Returns a string of 'X' or 'O'."""

        return "X" if player == "O" else "O"

    def show_board(self):
        """Outputs the board in the terminal."""

        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
