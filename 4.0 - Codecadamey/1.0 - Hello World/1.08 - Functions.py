def spam():
  """ prints 'Eggs!' to the console """
  print ("Eggs!")

spam() 


#Another example, parsing values
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print (f"length = {len(str(result))}")
  print ("%d to the power of %d is %d." % (base, exponent, result))

base_input = int(input("base: "))
power_input = int(input("power: "))
power(base_input, power_input) 

#Functions calling functions
def one_good_turn(n):
  return n + 1
    
def deserves_another(n):
  return one_good_turn(n) + 2

def shout(phrase):
  if phrase == phrase.upper():
    return "YOU'RE SHOUTING!"
  else:
    return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")

def cube(number):
  return number*number*number

print(cube(1))

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False

import math   
root = math.sqrt(25) #using the dot so it knows where to look
print(root)

from math import sqrt
root = sqrt(32) #because we've imported the function we don't need to declare it
print(root)

from math import * #this lazily brings in everything
print (dir(math)) #(everything, to see all functions)

#note to self, quite enjoying this bit of the course


#okay, moving onto another bit of the course
maximum = max (3, 5, -9)
print(maximum) # prints 5

minimum = min(-2, 4, 0)
print(minimum) # prints -2

absolute = abs(maximum, minimum) #although apparently this only takes a single number, so this will error
