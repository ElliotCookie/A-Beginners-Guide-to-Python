board = []
""" for coordinates in range(0, 4):
    board.append(["O"] * 5) """

for coordinates in range(5):
  board.append(['O'] * 5)
#print(board)

def print_board(board_in):
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