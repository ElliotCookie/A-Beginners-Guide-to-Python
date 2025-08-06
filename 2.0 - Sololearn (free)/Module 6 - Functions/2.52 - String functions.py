""" Correctly handling text data is a key skill all coders need to master.
String functions will enhance your productivity when working with text.

In this lesson, you'll learn to use built-in string functions. """

#String functions make it easier to work with text. The functions upper()
#  and lower() allow you to quickly change the case
#  of a string to all in uppercase or lowercase, respectively.

""" upper() and lower() functions can only be used on strings. 

Functions that only work on certain objects (strings, lists, etc.)
 are called using dot . notation.

Complete the line of code to call the lower() function using the dot notation """

print('LaPtOp'.lower())
#everything in python is an object, and objects all have data and behaviours
#the behaviours are methods
#so dot notation is just asking our object to use it's behaviour to do something
# e.g. dog.bark(), dog.run(), bark() isn't an external thing, it's innate to dog

""" The find() function checks if a character (or a pattern of characters)
is present in a string. The function returns the index (position)
 of the given value. If the given value is present multiple times, 
 the function will return the first occurrence (the lowest index). """

print("Bee".find("e")) #find() will return -1 if the value can't be found in the string.

word = 'vehicle'
#print(word.find())  --> ERRORS, NO ARGUMENT

""" Lesson Takeaways
Great job! You learned that:


🌟 upper(), lower(), and capitalize() functions are used to change
 the case of a string

🌟 The find() function searches for a value in a string and
 returns the index of the first time it appears """