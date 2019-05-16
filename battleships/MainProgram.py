# MainProgram.py
# author: James, Thomas, David
# date: 04/12/2018


from UserCommand import UserCommand
from Board import Board
from Guess import Guess

# welcome message and user instructions.
guess = Guess()
print('')
print('//     ___  ___ ______________   __________ _________  ______')
print('//    / _ )/ _ /_  __/_  __/ /  / __/ __/ // /  _/ _ \/ __/ /')
print('//   / _  / __ |/ /   / / / /__/ _/_\ \/ _  // // ___/\ \/_/ ')
print('//  /____/_/ |_/_/   /_/ /____/___/___/_//_/___/_/  /___(_)  ')
print('//                                                           ')
print('//By The Best Team')
print('Welcome to battle ships!\nCoordinates run from 0 to 4.\nShips are placed from the bow')
print('horizontal ships face left and vertical ships face up')
print('\nPlace your ships then the game will begin! Good luck!\n')


# function for one user to place ships twice.
def play_board(board, player_number):
    play_times = 0
    while play_times < 2:
        print("player", player_number, "Please place your", play_times + 1, "ship")
        play = UserCommand()
        play.place_ship_validation(board)
        play_times += 1


# function to let second user to play
def place_ship():
    player_number = 1
    while player_number < 3:
        if player_number == 1:
            player1_board = Board()
            play_board(player1_board, player_number)
            player_number += 1
        else:
            player2_board = Board()
            play_board(player2_board, player_number)
            guess.player_guess(player_number, player2_board)
place_ship()


# if i input 1 to the guess row and guess column, expecting hit one and the board would show where i hit
# if i input 4 to the guess row and guess column, expecting message tells me that i missed and shows me where i hit
# if i input 4 to the guess row and guess column again, expecting message tells me that i already hit there before


# import sys
# restart function
# def playagain():
#     restart = input("Would you like to play again?: ")
#     if restart == "yes" or restart == "y":
#         place_ship() #change this to run the main code functionh
#     elif restart == "no" or restart == "n":
#         print ("Script terminating. Goodbye.")
#         sys.exit() # uses import sys yo import the exit function
#     else:
#         print("y, or yes and n, or no")
#         playagain() # invalid input results in a message to clarify options for the user


# test code:
# first player's first ship input: h for orientation, 0 for row, 0 for column
# first player's second ship in put: v for orientation, 1 for row and 2 for column
# second player's first ship input: v for orientation, 2 for row and 2 for column
# Guess row 1 and column 1
# Return: You hit one.
