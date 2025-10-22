def clinic():
    print ("You've just entered the clinic!")
    print ("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print ("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif answer == "right" or answer == "r":
        print ("Of course this is the Argument Room, I've told you that already!")
    else:
        print ("You didn't pick left or right! Try again.")
        clinic()

clinic() #you can't preload an answer and clinic hasn't been defined with a variable for it


""" There are six comparators """
# Equal to
# 2 == 2 - True
# 2 == 5 - False

# Not equal to
# 2 != 5 >>> True
# 2 != 2 >>> False

#I'm not explaining less than, or greter than (up to 4 / 6 now)
# <, >

# With the less than/greater than OR equal to, be careful with syntax
# 2 <= 2 >>> True
# 5 <= 2 >>> False
# 
# 5 >= 5 >>> True
# 2 >= 5 >>> False
# Maybe one to check with a console print in your runtime 

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = (-22 >= -18)

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five =  99 != (98 + 1)

#Making a mental note that even though my code is the same as the example solution, the website won't let me pass

