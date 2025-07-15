# Seems pretty huge, allow you to modify callable objects like classes, methods or funcitons
# It uses some more keyword-like notation

def decorator(fn):
    def nested(*args, **kwargs):
        return fn(*args, **kwargs)
    return nested


# Instead of writing
def function(argument):
    return "value"
function = decorator(function)
# passing the function to the decorator, reassigning it

# We can write:
@decorator #the @ symbol is the decorator, not the word
def anotherFunction(argument):
    return "value"

#so basically a decorator is just a function that takes another funcion
#and also returns a function 
#This is useful for:
# - wrapping any function to log entry/exit times or measure performance,
# without touching the function itself
# - wrapping expensive computations to store results instantly
# - consistency and enabling access control

# Core logic remains focused, and 'extra features' get layered on top in a reusable way

""" Exercise
Make a decorator factory which returns a decorator that decorates functions
with one argument. The factory should take one argument, a type, and then
returns a decorator that makes function should check if the input is the 
correct type. If it is wrong, it should print("Bad Type") 
(In reality, it should raise an error, but error raising isn't in this tutorial).
Look at the tutorial code and expected output to see what it is if you
are confused (I know I would be.) Using isinstance(object, type_of_object)
or type(object) might help."""


def type_check(correct_type):
    #put code here
    def new_nested(arg):
        if arg >< int:
            raise (ValueError, "Bad type")
        correct_type(arg)
    return new_nested
           

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])