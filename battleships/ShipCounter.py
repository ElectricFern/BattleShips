#ShipCounter
#author Thomas Dalzell
#dec2018
# testing ship sinking by counting the remaining peice of a ship. ships would be represented as objects if implemented.

class Board():
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    #calls a copy of the board
    def call_Board(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                         for row in Board.board]))
Board.call_Board(1)

Board.board[0][1] = 1
Board.board[0][2] = 1
Board.board[0][3] = 1
print('places some ships which are repesented by 1')
Board.call_Board(1)


sink = input(print('enter anything to test ship distruction'))

print('replaces 1(or ships) values with 2 to represent damaged ships')

Board.board[0][1] = 2
Board.board[0][2] = 2
Board.board[0][3] = 2
Board.call_Board(1)

#counts to see how many parts of the ship are damaged. if all are damaged then the ships is sunk.
for row in range(0, 5):
    Board.board.append(["0"] * 5)
count = Board.board.count(2)
if count == 0:
    print('Your battle ship has been sunk!')


'''
  0  0  0  0  0
  0  0  0  0  0
  0  0  0  0  0
  0  0  0  0  0
  0  0  0  0  0
places some ships which are repesented by 1
  0  1  1  1  0
  0  0  0  0  0
  0  0  0  0  0
  0  0  0  0  0
  0  0  0  0  0
enter anything to test ship distruction
Noneg
replaces 1(or ships) values with 2 to represent damaged ships
  0  2  2  2  0
  0  0  0  0  0
  0  0  0  0  0
  0  0  0  0  0
  0  0  0  0  0
Your battle ship has been sunk!
'''

