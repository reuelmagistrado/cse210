from art import logo
from os import system
from tic_tac_toe import TicTacToe

__assignment__ = "Week 1: Tic-Tac-Toe"
__course__ = "CSE 210: Programming with Classes"
__author__ = "Reuel Magistrado"
__version__ = "1.0.0"
__maintainer__ = "Reuel Magistrado"
__email__ = "mag21010@byui.edu"


def main():
    '''Main Program of Tic-Tac-Toe game.'''
    # Clear terminal screen and show logo.
    system('cls')
    print(logo)

    start_game = int(input('Press 1 to START: '))
    if start_game == 1:
        system('cls')
        tic_tac_toe = TicTacToe()

        is_size_valid = False
        while not is_size_valid:
            board_size = [3, 4, 5, 6]
            size_choice = int(input("Choose board size [3, 4, 5, 6]: "))

            if size_choice in board_size:
                is_size_valid = True

        system('cls')
        tic_tac_toe.create_board(size_choice)

        player = "X" if tic_tac_toe.get_random_first_player() == 1 else "O"

        is_game_end = False
        while not is_game_end:
            print(f"Player {player} turn")

            tic_tac_toe.show_board()

            is_cell_not_marked = True
            while is_cell_not_marked:

                is_row_valid = False
                while not is_row_valid:
                    row = int(
                        input(f"Enter row number [1 - {len(tic_tac_toe.board)}]: "))
                    if row in range(1, len(tic_tac_toe.board) + 1):
                        is_row_valid = True

                is_col_valid = False
                while not is_col_valid:
                    col = int(
                        input(f"Enter column number [1 - {len(tic_tac_toe.board)}]: "))
                    if col in range(1, len(tic_tac_toe.board) + 1):
                        is_col_valid = True
                print()

                if tic_tac_toe.is_marked(row - 1, col - 1):
                    print("CELL ALREADY MARKED ❗❗❗")
                else:
                    tic_tac_toe.mark_spot(row - 1, col - 1, player)
                    is_cell_not_marked = False

            system('cls')
            if tic_tac_toe.is_player_win(player):
                print(f"Player {player} WINS! 🎉✨")
                is_game_end = True

            if tic_tac_toe.is_board_filled():
                print("Match Draw! 🤝")
                is_game_end = True

            player = tic_tac_toe.swap_player_turn(player)

        print()
        tic_tac_toe.show_board()


# Code to execute if called from command-line.
if __name__ == "__main__":
    main()
