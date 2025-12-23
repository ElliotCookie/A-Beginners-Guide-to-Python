count = 0

if count < 5:
  print ("Hello, I am an if statement and count is"), count

while count < 10:
  print ("Hello, I am a while and count is"), count
  count += 1


  #conditions
  loop_condition = True

while loop_condition:
  print ("I am a loop")
  loop_condition = False

#maths in a while loop
num = 1

while num < 11:  # Fill in the condition
  # Print num squared
  print(num*num)
  # Increment num (make sure to do this!)
  num += 1


#errors
choice = (input('Enjoying the course? (y/n)'))

while choice != 'y' and choice != 'n':   # Fill in the condition (before the colon)
  choice = input("Sorry, I didn't catch that. Enter again: ")


#infinite loops
count = 0

while count < 10:
  print (count)
  count += 5
  # Increment count - although you mean by one, but you it didn't mention this


  #Using breaks
count = 0

while True:
  print (count)
  count += 1
  if count >= 10:
    break

import random

print ("Lucky Numbers! 3 numbers will be generated.")
print ("If one of them is a '5', you lose!")

count = 0
while count < 3:
  num = random.randint(1, 6)
  print (num)
  if num == 5:
    print ("Sorry, you lose!")
    break
  count += 1
else:
  print ("You win!")


#else within while, my turn
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
while guesses_left > 0:
  guess = input("Please guess")
  if guess == random_number:
    print("You win!")
    break
  guesses_left -= 1
else:
  print("You lose!")
