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


#for loops
print ("Counting...")

for i in range(20):
  print (i)


hobbies = []

for i in range(3):
  hobbies.append(input("Enter hobby: ")) #it didn't like non-raw_input
print(hobbies)


#strings in for loops
thing = "spam!"

for c in thing:
  print (c)

word = "eggs!"

for letters in word:
  print(letters)


#string manipulation
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
  if char == "A" or char == "a":
    print("X")
  else:
    print(char)
  print  


# going through lists
numbers  = [7, 9, 12, 54, 99]

print ("This list contains: ")

for num in numbers:
  print (num)

for num in numbers:
  sq = num * num
  print(sq)


#looping a dictionary, dictionary loops
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
  print(f"{key} {d[key]}")
  #print key, d[key]


#Enumerate function
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
  print (index+1, item)


#iterating over two lists at once
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
  if a > b:
    print(a)
  else: 
    print(b)


#else statements - unclear what the ask is here...
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!') # (It actually is.)
    break
  print ('A', f)
else: #it was as simple as just deleting it
  print ('A fine selection of fruits!')


#creating a for / else statement
for nums in range(0,5):
  print(nums)
else:
  print("else statement activated")  
  #BASICALLY YOU MUST USE A NESTED IF WITH A BREAK FOR THIS TO BE USEFUL
  