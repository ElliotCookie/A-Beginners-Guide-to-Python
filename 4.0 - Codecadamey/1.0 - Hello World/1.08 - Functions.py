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

#absolute = abs(maximum, minimum) although apparently this only takes a single number, so this will error
absolute = abs(minimum)

#this lesson is about another function
print(type(30)) # prints <class 'int'>
print(type(20.3))  # prints <class 'float'>
print(type("ten")) # prints <class 'str'>

def shut_down(s):
  if s == "yes":
    return "Shutting down"
  elif s == "no":
    return "Shutdown aborted"
  else:
    return "Sorry"
  
#so I pasted that on line 2 and not line 1, it was perfectly correct, but on the wrong line, so I got a fail

from math import sqrt #again, it's for the crechendo 
print(sqrt(13689))

def distance_from_zero(distance):
  if type(distance) == (int or float): # this bit is wrong
    return abs(distance)
  else:
    return "nope"
  
print(distance_from_zero(-9.5))  
print(distance_from_zero("seven"))#

def distance_from_zero(distance):
  if type(distance) == int or type(distance) == float:
    return abs(distance)
  else:
    return "nope"
  
print(distance_from_zero(-9.5))  
print(distance_from_zero("seven"))

""" LESSON COMPLETE!! """


def answer():
  return 42

def hotel_cost(nights):
  return 140 * nights

def plane_ride_cost(city):
  if city == "Charlotte": #errored me for the spelling
    return 183
  elif city ==  "Tampa":
    return 220
  elif city ==  "Pittsburgh":
    return 222
  elif city ==  "Los Angeles": 
    return 475
  
def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -=20
  return cost



def trip_cost(city, days):
  return hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days)

print("City cost thing")
city = input("City: ")
days = int(input("Days: "))
print(f"The total trip cost to {city}is: {trip_cost(city, days)}")


#Now with spending money
def trip_cost(city, days, spanding_money):
  return spanding_money + hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days)

print("City cost thing")
city = input("City: ")
days = int(input("Days: "))
spending = int(input("Spending: "))
print(f"The total trip cost to {city}is: {trip_cost(city, days, spending)}")

#Cost to LA
print(trip_cost("Los Angeles", 5, 600))

#MODULE COMPLETE!!