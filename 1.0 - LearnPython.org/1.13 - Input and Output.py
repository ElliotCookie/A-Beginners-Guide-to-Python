#Taking input and output is obviously a huge part of a useful computer programme
#Lets get into the big secret

myFirstInput = input() #yeah it's that easy
print(f"your first input was: {myFirstInput}")
#there is notes about spaces causing error but I reckon that was for 2.0

#it's probably good practise to sort your inputs into a data type
myFirstNumberInput = int(input())
print (myFirstNumberInput)
print("Lets try a decimal input and type a string!") #shock, we got an error and crash
decimalInput = float(input())
print(decimalInput)
print("end of that second bit")

#We can take more than 1 data type from a single line apparently 
total = 0 #defining an int variable
a, b = map(int, input("we'll just print these two, enter and submit ").split()) #input().split(), not input.split()
#MAP is a super useful function that isn't explained in the notes
#it allows you to apply a function to every item in an iterable (funciton, iterable)
#SPLIT() breaks a string up by whitespace
newArrayFromUserInput = input("We'll add these two, enter and sumbit").split()
for everyLine in newArrayFromUserInput:
    total += int(everyLine)
print(a, b, total)
#They've gone about this in a chaotic order 

#There is a note on formatting but I think f strings covers this
print(f"testing {total} and if we can print weird {myFirstNumberInput} stuff")

""" EXERCISE _________________________________________________
Write a program that asks the user to input their name, age, and country.
The program should then print out a message that includes this information
in a sentence. The program should include:

Taking a name as input using input().
Taking an age as input using input(), and converting it to an integer.
Taking a country name as input using input().
Formatting the output to display a sentence that includes the name, age, and country.
The program should demonstrate input handling and string formatting in Python. """

# Taking the name input using input()
name = input("Enter your name: ")

# Taking the age input using input() and converting it to integer
age = int(input("Enter your age: "))

# Taking the country input using input()
country = input("Enter your country: ")

# Displaying the formatted sentence with name, age, and country
print("Hello, my name is %s, I am %d years old, "
"and I am from %s." % (name, age, country))