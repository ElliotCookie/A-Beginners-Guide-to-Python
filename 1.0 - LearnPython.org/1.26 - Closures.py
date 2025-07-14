# A closure in python is a weird little phenomonom, that happens when:
# A nested function (a function within a function) 
# Refers to variables from the enclosing function that's already finished running
# but the inner function still remembers those variables 

def enclosingFunction(message1):
	print("This is the enclosing function")
	def nestedFunction(message2):
		print("this is the nested function")
		result = f"{message1} is first and {message2} is second"
		return result #need to return something or it prints "None"	
	return nestedFunction
testMessage = enclosingFunction(input(""))
print(testMessage(input("")))

#There is something fun you can do with the 'nonlocal' keyword
def outer(string):
	def nested():
		nonlocal string
		string="hello world"
		print(string)
	nested() #Calling it straight away
	print(string)
outer("new string that won't print")

#You can return the function object rather than calling the nested function, e.g:
def anotherOuter(anotherVariable):
	"This is just a line of text?"
	def anotherNested():
		"A line of text, but nested"
		print(anotherVariable)
	return anotherNested # allows for delaying execution
function2 = anotherOuter("test time")
# can do stuff here before calling the function
function2()

# Returning the nested allows you to create a reusable stateful function
# Calling immediately lets you encapsulate logic, but not use it afterwards



"""Exercise
Make a nested loop and a python closure to make functions
to get multiple multiplication functions using closures.
That is using closures, one could make functions to create
multiply_with_5() or multiply_with_4() functions using closures."""

# your code goes here
def makeMultiplierFunction(n):
	def multiplywith(x):
		result = n * x
		print(f"{n} x {x} = {result}")
		return result
	return multiplywith	

# Ask the user for the multiplier
mult = int(input("Pick your multiplier: "))
mult_fn = makeMultiplierFunction(mult)

# Ask for the value to multiply and invoke the closure
value = int(input("Enter a value to multiply: "))
mult_fn(value)