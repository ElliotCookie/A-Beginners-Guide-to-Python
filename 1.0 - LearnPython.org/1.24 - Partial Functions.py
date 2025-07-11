#A partial function is a funtion with some of the stuff you need already filled in (partially applied)
#This saves repeating code, making it more modular and easily readable
#This also means it links into higher-order functions more readily
# (Higher functions are functions that take arguments as functions)

from functools import partial

def multiply(x, y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply, 2) #this is our partial that locs in x = 2 (multiply being the base function)
print(dbl(4)) #this parses y as 4, which is doubled
#it is important to note that functiones 

"""Exercise
Edit the function provided by calling partial() and replacing the first three variables in func().
Then print with the new partial function using only one input variable so that the output equals 60."""

#Following is the exercise, function provided:
from functools import partial

def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

#ooo, bit of spicy logic with this one
#but I think it can be cheesed
newPartial = partial(func, 0, 0, 0)
print(newPartial(60))
