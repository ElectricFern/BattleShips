# Guess.py
# author: David
# date: 04/12/2018
from Board import Board


class Guess:

    player1 = Board()
    player2 = Board()
    # while loop to guess where ships are

    def player_guess(self, player_number, board):
        while "S" != 0:
            if player_number == 2:
                self.player1 = board
                guess_x = int(input("Guess row\n"))
                guess_y = int(input("Guess column\n"))
                if self.player1.board[guess_x][guess_y] == "S":
                    board.change_to_h(guess_x, guess_y)
                    board.print_board()
                    print("You hit one")
                elif self.player1.board[guess_x][guess_y] == "X":
                    print("You already tried there, try again.")
                elif self.player1.board[guess_x][guess_y] != "S":
                    board.change_to_x(guess_x, guess_y)
                    board.print_board()
                    print("You missed.")
                elif self.player1.board[guess_x] > 4 or self.player1.board[guess_y] > 4:
                    print("That's not even in the ocean.")
                    self.player_guess(player_number, board)


'''
Test outputs:

"C:\Program Files (x86)\Python35-32\python.exe" "H:/Documents/PyCharm Projects/battleship/MainProgram.py"

//     ___  ___ ______________   __________ _________  ______
//    / _ )/ _ /_  __/_  __/ /  / __/ __/ // /  _/ _ \/ __/ /
//   / _  / __ |/ /   / / / /__/ _/_\ \/ _  // // ___/\ \/_/
//  /____/_/ |_/_/   /_/ /____/___/___/_//_/___/_/  /___(_)
//
//By The Best Team
Welcome to battle ships!
Coordinates run from 0 to 4.
Ships are placed from the bow
horizontal ships face left and verticail ships face up

Place your ships then the game will begin! Good luck!

player 1 Please place your 1 ship
what orientation would you like to place the ship
(h for horizontal and v for vertical):h
what is the "X" of  the bow where you want to place your ship (horizontal ships face left): 0
what is the "y" of  the bow where you want to place your ship (horizontal ships face left): 0
S  S  S  0  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
player 1 Please place your 2 ship
what orientation would you like to place the ship
(h for horizontal and v for vertical):h
what is the "X" of  the bow where you want to place your ship (horizontal ships face left): 1
1what is the "y" of  the bow where you want to place your ship (horizontal ships face left):
S  S  S  0  0
0  S  S  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
player 2 Please place your 1 ship
what orientation would you like to place the ship
(h for horizontal and v for vertical):h
what is the "X" of  the bow where you want to place your ship (horizontal ships face left): 1
what is the "y" of  the bow where you want to place your ship (horizontal ships face left): 1
0  0  0  0  0
0  S  S  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
player 2 Please place your 2 ship
what orientation would you like to place the ship
(h for horizontal and v for vertical):h
what is the "X" of  the bow where you want to place your ship (horizontal ships face left): 0
what is the "y" of  the bow where you want to place your ship (horizontal ships face left): 0
S  S  S  0  0
0  S  S  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
Guess row
0
Guess column
0
H  S  S  0  0
0  S  S  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
You hit one
Guess row
1
Guess column
1
H  S  S  0  0
0  H  S  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
You hit one
Guess row
0
Guess column
1
H  H  S  0  0
0  H  S  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
You hit one
Guess row
0
Guess column
2
H  H  H  0  0
0  H  S  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
You hit one
Guess row
1
Guess column
2
H  H  H  0  0
0  H  H  S  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
You hit one
Guess row
1
Guess column
3
H  H  H  0  0
0  H  H  H  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  0
You hit one
Guess row
4
Guess column
4
H  H  H  0  0
0  H  H  H  0
0  0  0  0  0
0  0  0  0  0
0  0  0  0  X
You missed.
Guess row
'''
