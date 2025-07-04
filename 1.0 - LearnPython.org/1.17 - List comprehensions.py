#List comprehensions allow you to create a new list based on an existing one
#all in a single, readable line!? very cool
#There isn't a keyword to learn for this one, it is a syntax pattern containing
#square brackets [], a for loop, and an optional if condition

numbertest = [1, 5, 6, 74, 4, 456, 2335, 3546, 45657, 2, 2456, 573, 3567, 8645, 2456]
#these are random tehe 
myFirstListComprehension = [number for number in numbertest if number > 2300]
#“Make a list of number for each number in numbers if number > 2300.”
#[expression for variable in iterable if condition]
print(myFirstListComprehension)

""" Exercise
Using a list comprehension, create a new list called "newlist" 
out of the list "numbers", which contains only the positive numbers
from the list, as integers. """
#oh, looks like my spin on the first example is actually the exercise
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]
print(newlist)