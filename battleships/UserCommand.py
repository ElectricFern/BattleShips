# UserCommand.py
# author: Thomas Dalzell
# date: 04/12/2018


class UserCommand:

    # to get the orientation for the ship
    def place_ship_validation(self, board):

        orientation = input('what orientation would you like to place the ship\n'
                            '(h for horizontal and v for vertical):')
        if orientation == 'h':
            self.coordinateplacement_x_h(board)
        elif orientation == 'v':
            self.coordinateplacement_x_v(board)
        else:
            print('invalid orientation')
            self.place_ship_validation(board)

    # if the ship is horizontal, ask user for the coordinates,
    # correct invalid input, change the board and display the board.
    def coordinateplacement_x_h(self, board):
        ship_x = int(input('what is the "X" of  the bow where you want to place your ship'
                           ' (horizontal ships face left): '))
        if ship_x > 2:
            print('invalid X coordinate')
            self.coordinateplacement_x_h(board)
        else:
            ship_y = int(input('what is the "y" of  the bow where you want to place your ship '
                               '(horizontal ships face left): '))
            if ship_y > 4:
                print('invalid y coordinate')
                self.coordinateplacement_x_h(board)
            else:
                board.change_board("h", ship_x, ship_y)
                board.print_board()

    # if the ship is vertical, ask user for the coordinates,
    # correct invalid input, change and display the board.
    def coordinateplacement_x_v(self, board):
        ship_x = int(input('what is the "X" of  the bow where you want to place your ship '
                           '(vertical ships face up): '))
        if ship_x > 4:
            print('invalid ship_X coordinate')
            self.coordinateplacement_x_v(board)
        else:
            ship_y = int(input('what is the "Y" of  the bow where you want to place your ship '
                               '(vertical ships face up): '))
            if ship_y > 2:
                print('invalid y coordinate')
                self.coordinateplacement_x_v(board)
            else:
                board.change_board("v", ship_x, ship_y)
                board.print_board()


'''
    def place_ship(self,board):
        orientation = input("please decide the orientation you would like to place your ship\n"
                            "h for horizontal and v for vertical\n")
        if orientation != "h" and orientation != "v":
            print("Sorry, invalid input, please try again.\n")
            self.place_ship(board)
        else:
            if orientation == "h":
                ship_X = int(input("please enter the start of your ship row here.\n "))
                if ship_X > 2:
                    print("Oops! that is outside the ocean. Please try again.\n")
                    self.place_ship(board)
                else:
                    ship_Y = int(input("please enter the start of your ship column here.\n "))
                    if ship_Y < 3:
                        board.change_board("h", ship_X, ship_Y)
                        board.print_board()
                    else:
                        print("Oops! that is outside the ocean. Please try again.\n")
                        self.place_ship(board)
            elif orientation == "v":
                ship_Y = int(input("please enter the start of your ship column here.\n "))
                if ship_Y < 4:
                    ship_X = int(input("please enter the start of your ship row here.\n "))
                    if ship_X < 3:
                        board.change_board("v", ship_X, ship_Y)
                        board.print_board()
                    else:
                        print("Oops! that is outside the ocean. Please try again.\n")
                        self.place_ship(board)
                else:
                    print("Oops! that is outside the ocean. Please try again.\n")
                    self.place_ship(board)

'''




