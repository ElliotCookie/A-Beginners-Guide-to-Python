board = []
""" for coordinates in range(0, 4):
    board.append(["O"] * 5) """

for coordinates in range(0, 5):
  board.append(['O'] * 5)
#print(board)

def print_board(board):
  for rows in board:
    #print(rows)
    print(" ".join(rows))

print_board(board)


""" letters = ['a', 'b', 'c', 'd']
print " ".join(letters)
print "---".join(letters)

Then, we print a b c d. The .join method uses the string to combine the items in the list.
Finally, we print a---b---c---d. We are calling the .join function on the "---" string.


Now edit our function, similarly
 """

from random import randint
coin = randint(0, 1)
dice = randint(1, 6)


def random_row(board_in):
  return randint(0, len(board_in) - 1)
  
def random_col(board_in):
  return randint(0, len(board_in) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(4):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!")   
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      if (turn == 3):
        print("Game over")
    print_board(board)
