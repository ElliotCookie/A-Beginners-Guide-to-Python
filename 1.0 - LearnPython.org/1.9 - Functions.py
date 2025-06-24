#Functions are the writers way of making their own little code blocks
#They make it more readable and thus easier to share with other coders and reuse

#An important concept is that Python syntax makes use of blocks:
""" block_head:
    1st block line
    2nd block line """ #The block lines can be code, or even other blocks

#The block head has a special format:
#block_keyword, block_name(argument 1, argument 2)
#arguments are just variables that gets handed to a function. E.g f(x) = x + 2
#keywords we know are while, for and if (we are about to learn another)

#The block keyword for functions is "def"
def first_function():
    while True:
        print("we are in the first function block! We could do stuff here...")
        break

first_function() #don't forget that you need to call it, and also add the ()

#as well as Arguments, there is a thing called Return
#This passes back info to the caller:

def second_function(a, b):
    return a + b
result = second_function(1,2)
print(f"This is the result, using return {result}")



def print_add_function(x, y):
    print(f"this is in the function, printing {x + y}")  # This does NOT return anything
output = print_add_function(2, 3)  # prints 5, but output is None


""" Exercise
In this exercise you'll use an existing function, 
and while adding your own to create a fully functional program.

Add a function named list_benefits() that returns the following list
of strings: "More organized code", "More readable code", "Easier code reuse",
 "Allowing programmers to share and connect code together"

Add a function named build_sentence(info) which receives a single argument 
containing a string and returns a sentence starting with the given string 
and ending with the string " is a benefit of functions!"

Run and see all the functions work together! """

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code",
            "More readable code", 
            "Easier code reuse", 
            "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + "is a benefit of functions!"
#dont forget the f(x) = x + 2 syntax. You need x on both sides!
#I say this as I forget to put 'benefit' in front of it 

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()