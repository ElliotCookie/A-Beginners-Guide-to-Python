#Python uses boolean logic to evaluate conditions
#Therefore a condition is either true or false 
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True


#Like with all fun boolean things, you can use and or or (and I'm imagining nand and nor)
#This allows you to build complex conditions to be met (or not)

name = "Fred"
age = 99
if name == "Fred" and age == 99:
    print("Ladies and gentlemen, we got him")
if name == "John" or name == "Fred":
    print("Congrats, you are called Fred or John.")
    pass
print (not False) #notice the capital F



#'in' allows you to check if an object is in an iterable object containter
#a string even coutns as an IOC
NumberNames = [] #[] for a list, () for a tuple, which is immutable
for x in range (1,10):
    NumberNames.append(x)
if 9 in NumberNames:
    print("Sweet, that's number 9")

if x == 2:
    print("x ==2 is true") #Removed the "is true"
    pass
elif name == "Fred": #Removed the "is true"
    print("The name is Fred")
else:
    print("We reached the else clause")
    pass

#The is function matches instances, that is comparies the identity
#rather than the value. 
y = 2
print(x is y) #not used an f string here, which is wild 


""" The task, pasted in
Change the variables in the first section,
so that each if statement resolves as True. """

number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")