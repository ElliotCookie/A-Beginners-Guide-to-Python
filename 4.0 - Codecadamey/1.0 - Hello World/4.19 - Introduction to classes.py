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
class Fruit(object):
  """A class that makes various tasty fruits."""

  # This is the constructor and runs when an object is created
  # e.g. lemon = Fruit("lemon", "yellow", "sour", False)
  # We will come on to creating a class but not populating it with data I am sure
  def __init__(self, name, color, flavor, poisonous):
    # self is the actual object instance, and lets us refer to specific items
    # self is not a keyword but the community uses it as the current instance 
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous
  # without init, we'd have to do:
  # lemon = fruit()
  # lemon.name = "lemon"
  # lemon.color = "red"
  # Not only is this untidy, but it prevents us forgetting things and makes sure set up is correct

  # There is a way to help reading when initiating classes:
  # def __init__(self, name: str, color: str, flavor: str, poisonous: bool):


  def description(self):
    print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

  def is_edible(self):
    if not self.poisonous: # accessing an attribute, not calling a function
      print ("Yep! I'm edible.")
    else:
      print ("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()




# 2 / 18 - Class syntax
# Pass is a useful keyword where you're expecting to put in an expression later 

class Animal(object):
   # Note that using (Object) is python 2 formatting, you can miss the brackets for now

   # Python will use the first parameter that __init__() receives to refer to the object being created; 
   # this is why it’s often called self, since this parameter gives the object being created its identity.
   def __init__(self, name):
      self.name = name
      pass

# We'e skipped 3 - 4 from just pressing 'run code' 
# 5 / 18 - Instantiating out first class

zebra = Animal("Jeffrey") # Parsing Jeffrey
print(zebra.name) #Jeffrey

# I really love the 'pass' keyword btw





# 6 / 18 - The first argument __init__() gets is used to refer to the instance object, 
# and by convention, that argument is called self.

# add a 3rd attribute to Animal below

class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print (zebra.name, zebra.age, zebra.is_hungry)
print (giraffe.name, giraffe.age, giraffe.is_hungry)
print (panda.name, panda.age, panda.is_hungry)
