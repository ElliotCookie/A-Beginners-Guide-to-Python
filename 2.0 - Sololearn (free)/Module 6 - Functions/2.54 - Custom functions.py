""" Built-in functions can save you a lot of work, 
but you’ll also need to create your own custom functions to solve specific tasks.

In this lesson, you’ll learn to create your own functions! """

#To use your own functions, you need to define them first. 
# Once a function has been defined, you can call it as many times as you need.
# The greet() function below contains code to display a nice message when called
# PAYWALL

def greet(): 
  print("Hello from a function")
  print("Have a great day")

greet()

""" The body of a function contains the reusable code
that is executed when the function is called. 
The code for the body of a function must be indented.
When a function is defined, you need to make sure parentheses () 
are added after the name. A colon : must be added at the end of the 
definition line. """

def bmi(weight, height):
    index = weight / (height * height)
    print(index)

#The result of a function can be sent back with the return statement.
# This is particularly helpful when you need to continue using the
#  result value in your program.

#being asked questions about the previous screen? Basically memory?

""" Lesson Takeaways
Great job! Now you can create your own functions! You learned that:

🌟 def defines a new function

🌟 The function body contains the code that is
 executed when the function is called

🌟 return sends values back so they can be stored and used in the program """
