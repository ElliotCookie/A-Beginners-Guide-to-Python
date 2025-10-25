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


# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 5 < 3

# Make me true!
bool_three = 5 == 5

# Make me false!
bool_four = 5!=5

# Make me true!
bool_five =  3 < 5


""" Boolean operators compare statements and result in boolean values. There are three boolean operators:

and, which checks if both the statements are True;
or, which checks if at least one of the statements is True;
not, which gives the opposite of the statement. """

#last time we found a good way to remember this
#something like and is negative, or is +ve 
#negative - N - aNd, pOstitive - O - Or

print(bool(-(-(-(-2))) == -2 and 4 >= 16 ** 0.5)) # don't forget caps
print(bool(19 % 4 != 300 / 10 / 10 and False))
print(bool(-(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2))

#same again, it won't let me submit my answer (even tho same as example solution) 

print("OR practise")
print(bool(2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'))
print(bool(100 ** 0.5 >= 50 or False))
print(bool(1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1))

#Didn't need to do this, it's already filled in!

#This is interesting:
""" Boolean 
operators
Preview: Docs Loading link description
 aren’t just evaluated from left to right. Just like 
with
Preview: Docs Loading link description
 arithmetic operators, there’s an order of operations for boolean operators:

not is evaluated first;
and is evaluated next;
or is evaluated last. """

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (10 > 5) or (3 < 1)

# Make me false!
bool_three = not (4 == 4)

# Make me true!
bool_four = (7 != 2) and not (3 > 5)

# Make me true!
bool_five = not (6 < 2) or (1 == 1)