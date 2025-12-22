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