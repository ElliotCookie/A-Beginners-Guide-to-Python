# A closure in python is a weird little phenomonom, that happens when:
# A nested function (a function within a function) 
# Refers to variables from the enclosing function that's already finished running
# but the inner function still remembers those variables 

def enclosingFunction(message1):
	print("This is the enclosing function")
	def nestedFunction(message2):
		print("this is the nested function")
		print(f"{message1} is first and {message2} is second")
	return nestedFunction


testMessage = enclosingFunction(input())
print(testMessage)






"""Exercise
Make a nested loop and a python closure to make functions to get multiple multiplication
functions using closures. That is using closures, one could make functions to create
multiply_with_5() or multiply_with_4() functions using closures."""

# your code goes here

multiplywith5 = multiplier_of(5)
multiplywith5(9)