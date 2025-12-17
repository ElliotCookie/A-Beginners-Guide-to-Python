board = []
""" for coordinates in range(0, 4):
    board.append(["O"] * 5) """

for coordinates in range(5):
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

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Col: "))

if (guess_row == ship_row) & (guess_col == guess_col):
  print("Congratulations! You sank my battleship!") 
else:
  if 0 > guess_row or guess_row > 5 or 0 > guess_col or guess_row > 5:
    print("Oops, that's not even in the ocean.")
  elif (guess_row == ship_row) & (guess_col == guess_col):
    print("You guessed that one already.")
  else:
    print("You missed my battleship!")
    #find board row
    #go to location in row
    #set value there to X
    attacked_row = board[guess_row-1]
    attacked_row[guess_col-1] = "X"
    print_board(board)
    # It's saying it doesn't work, but it does?!
    #they want:1  board[guess_row][guess_col] = "X"
