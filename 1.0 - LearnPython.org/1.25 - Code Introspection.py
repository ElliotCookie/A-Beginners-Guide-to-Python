#Code introspection is the ability to examine keywords, functions and classes
# Doing this allows you to understand their inputs (or lack of) and their operating logic
# Python has tools that helps you with this task:

help() #this is the main one to know about
dir() 
hasattr() 
id() 
type() 
repr() 
callable() 
issubclass() 
isinstance() 
__doc__ 
__name__


"""Exercise
Print a list of all attributes of the given Vehicle object."""


# Use the help function to see what each function does.
# Delete this when you are done.
help(dir)
help(hasattr)
help(id)

# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
# Your code goes here

# thing = open up the vehicle class and have a look
#print(thing)

print(dir(Vehicle))
