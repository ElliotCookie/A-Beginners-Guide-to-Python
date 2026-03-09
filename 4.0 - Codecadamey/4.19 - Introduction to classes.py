""" Python is an object-oritented programming language,
this means it manipulates constructs called objects. These are basically a value and behaviours, e.g
"""
text = "hello world"
upper = text.upper()
# the 'behviours' are methods, things that it can do
# a class is just a way of us being able to define our own object, outside of the ones python already has

# functions come from procedural programming,, there isn't an obect involved, e.g
low = 3
high = 5
adding_them = low + high # don't use SUM, it is a protected keyword
# there is an input, a process and an output, but this isn't a 'behaviour' 
# but in python, the functions we make are actually objects, the concept of input, process, output is important though


# Python actually mixes both stypes, procedural and o-o style
# clean(data)
# data.clean()
# but everything in python is an object, eg
print(type(text)) # <class 'str'>, and the 'str' has behaviours we can make it do (not processes)
# even functions are objects!! Which will come in useful ...


# Functions can be treated like data, unlocking huge time-savers:
def add(a, b): return a + b
operation = add # parsing the function itself, not the result
print(operation(3,4)) 

# Functions can be stored in lists!! 
def multiply(a,b): return a*b

ops = {
    "+": add,
    "*": multiply
} # storing operations in a dictionary

print(ops["+"](3,4)) # at the key "+" parse 3, 4

# We can also dynamically define a function, which is called a 'closure':
def multiplier(n): # below, we basically skip this
    def other(x): # just parse 10 to this, because we are returning input
        return n * x # n and x have been defined, so we can do the operation here
    return other # for the multiplier function, return whatever the 'input' function tells us

double_this_number = multiplier(2) # this is the closure
print(double_this_number(10))









# 1 / 18 - Why use classes?