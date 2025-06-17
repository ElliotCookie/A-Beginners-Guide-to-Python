print("This line will be printed.")

x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")

""" #Four spaces seems cool, but what happens if we do 0 or 8    
if x == 1:
    # indented four spaces
print("0 spaces")
        print("8 spaces")
#Right, it throws an error so lets look at the debug thingy """

#Indentation isn't just a style, it's part of syntax
#This enables it to get away from constant {use} which is nice 
#They need to be used anytime we use a COMPOUND STATEMENT, basically...
     #if, for, while, when, classes, functions, etc

x = 10
if x > 0:          # level 0
  if x % 2 == 0:   # level 1 (2 spaces)
    print("x is positive and even")   # level 2 (4 spaces), but note that this can be 2 or 6 or idk 10
  else:
    print("x is positive and odd")    # level 2 (4 spaces), MUST match above
else:
  print("x is zero or negative")      # level 1 (4 spaces), MUST match Level 1 spaces

#This function used a % and a ==, no idea what they mean. Will writeup in 1.0.
#Found PEP 8, that tell you what style is permissable "Code is read more than it is written"
#Similar vibe to "You have two ears but one mouth"

#Exploring the idea of % and ==
#Lets also try and nest the function in the print?
""" 
print("The restult of 14 % 5 is " & 14%5) """
# Okay we tried this and it flagged an error, you can only add together strings to strings with +
# not & (!)
# Two real options, the first is below and less clean, but works:
#print("The result of 14 % 5 is " + str(14 % 5))

#What is best and clean and what we need is:
print(f"The result of 14 % 5 is {14 % 5}")
#my understanding of the f is that it allows you to run anything in the curly brackets as its own code
#it will evaluate the above answer as 4 (int), but then the 'f' effectively does the str(4) for you
#so the error for str + int doesn't happen, as it's str + str, without having to use "+" 

#lets update this (now known) rubbish:
""" print("The restult of 14 % 6.5 is " & 14%6.5)
print("The result of 14.4 % 12 is " & 14.4 % 12)

BooleanTestTR = True
IntegerTestONE = 1
DecimalVariable = 1.00


print("The restult of BT1 == IT1 is " & BooleanTestTR==IntegerTestONE)
print("The restult of DV1 == IT1 is " & DecimalVariable==IntegerTestONE)

print("This is the end of your funny testing") """

#_________________________________________Uppdated set:

print(f"The restult of 14 % 6.5 is {14%6.5}") #dont forget to adjust "" 
print(f"The result of 14.4 % 12 is {14.4 % 12}")

BooleanTestTR = True
IntegerTestONE = 1
DecimalVariable = 1.00
#We know the & symbol is actually its own function, so should change these too

print(f"The restult of BT1 == IT1 is {BooleanTestTR==IntegerTestONE}")
print(f"The restult of DV1 == IT1 is {DecimalVariable==IntegerTestONE}")

print("This is the end of your f funny testing")

#Repo time!