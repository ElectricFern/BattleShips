# Board.py
# author: James
# date: 04/12/2018

# board created


class Board:

    board = []

    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]

# getting ships display on board as S.

    def change_board(self, orientation, row, column):
        if orientation == "h":
            self.board[row][column] = "S"
            self.board[row][column+1] = "S"
            self.board[row][column+2] = "S"
        elif orientation == "v":
            self.board[row][column] = "S"
            self.board[row+1][column] = "S"
            self.board[row+2][column] = "S"
        else:
            print("Sorry, invalid input.")

    # change S to H when user hits the ship
    def change_to_h(self, row, column):
        self.board[row][column] = "H"

    # change S to X when user misses the hit
    def change_to_x(self, row, column):
        self.board[row][column] = "X"

    # formatting and printing out the board
    def print_board(self):
            for row in self.board:
                number_list = ""
                for number in row:
                    number_list += str(number) + "  "
                print(number_list)

    # def ship_got_hit(self, guess_x, guess_y):
    #     if self.board[guess_x][guess_y] == "S":
    #         self.board[guess_x][guess_y] = "H"
    #         print("You hit one.")
    #     # elif self.board[guess_x] > 4 and self.player1.board[guess_y] > 4:
    #     #     print("That's not even in the ocean.")
    #     elif self.board[guess_x][guess_y] != "S":
    #           self.board[guess_x][guess_y] = "X"
    #           print("You missed.")
