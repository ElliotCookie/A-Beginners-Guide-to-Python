""" Custom (or user-defined) functions help to break a large 
program down into small segments to make it easy to understand, 
maintain and debug.

In this lesson, you’ll learn to build more advanced custom functions. """

def greet(name):
    print("Hello", name)
greet("David")

#A function can return multiple values. The function rect() helps a real 
# estate agency calculate the area and perimeter of a rectangular parcel of land.
#  It takes the two dimensions of the parcel as arguments

""" Multiple return values need to be separated by commas. 
When a function returns multiple values,
they can be stored in multiple variables (on 1 line).  """

#To create multiple variables in 1 statement, separate them with commas.
#I think we've done this?

#feel like there is more than the fair share of paywalls here
#yep, and another


def rect(d1, d2):
  area = 0
  return area
  area = d1 * d2

""" Python allows function arguments to have default values. 
If the function is called without the argument, the argument
 gets its default value """

def greet(name="Guest"):
  print("Welcome", name)
greet("Anna") #that's cool, I didn't know that


""" Lesson Takeaways
Congratulations! In this lesson you learned that:
 
🌟 A function can return multiple values

🌟 Defining a function also decides the data types it can take in, handle and return

🌟 Default values make arguments optional """
