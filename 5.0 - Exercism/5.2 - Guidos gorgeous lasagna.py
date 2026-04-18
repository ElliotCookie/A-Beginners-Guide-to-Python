"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 30


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining():
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """


    REMAINING_BAKE_TIME = EXPECTED_BAKE_TIME - elapsed_time_in_minutes()
    return REMAINING_BAKE_TIME
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), 
# you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes():
    return PREPARATION_TIME



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes():
    return int(input("Enter elapsed time: "))


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)



""" THIS IS INSANE?!
SO MUCH TO TAKE IN ON STEP 2?!
THIS IS AN OVERLOAD FOR HUMBLE LITTLE OLD ME """


print(bake_time_remaining())




# okay so the instructions in the code are much less clear than the website
# but lets be real here, I've not been taught what a function is yet so asking the user to create 4 is a tall order
# the instructions are asking new things so I'll try again

print("new try:")


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 30


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time_in_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """


    REMAINING_BAKE_TIME = EXPECTED_BAKE_TIME - time_in_oven
    return REMAINING_BAKE_TIME
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), 
# you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers."""
    PREPARATION_TIME = 2
    return number_of_layers * PREPARATION_TIME



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time."""
    time_in_kitchen = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    # A hashtag to see if this makes it
    """Another block comment"""
    return time_in_kitchen

# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)


print(elapsed_time_in_minutes(1,3))
print(elapsed_time_in_minutes(15,20))

help(preparation_time_in_minutes)

preparation_time_in_minutes.__doc__ = "This is a new docstring"
help(preparation_time_in_minutes)

print(bake_time_remaining(23))