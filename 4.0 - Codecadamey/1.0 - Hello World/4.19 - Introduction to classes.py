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





# 7 / 18 - Scope of variables

print("Scope of variables")
class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print (zebra.name, zebra.age, zebra.is_alive) #Jeffrey 2 True
print (giraffe.name, giraffe.age, giraffe.is_alive)
print (panda.name, panda.age, panda.is_alive)

# the takeaway is that we define is_alive in the function and can therefore pull it
# but as we know, not everything is global...




# 8 / 18 - Methods (functions but within a class)
# Adding our own method to the below:class Animal(object):
print("Adding our own method.....")

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  """   def description(): # trying without parsing first 
    print(self.name, self.age) # tried without the self. and it didn't like it """
  def description(self):
    print(self.name, self.age)
  
  #I need to somehow call the description method

hippo = Animal("Jeff", 17)
#hippo.description # not this
hippo.description() 

#hippo = Animal.description("Bob", 12) # okay this is it, or this prints at least
#lets check if it has been initialised as an object properly
#print(hippo.name) # okay this error, which is weird, as I thought it would at least be Jeff
#try again but move it lower
hippo = Animal("Charlie", 19)
print(hippo.name) # so this is initialised properly
# lets try this
#Animal.description(hippo) # okay this is missing the age argument, taking line out as errors

# I've added self to the function, taking out bob line now
# okay that doesn't work, reverting
# adding self into the description method again
# ahh, and then taking away name and age


#SOLUTION
hippo = Animal("Elliot", 8)
hippo.description() #behind the scenes this is: Animal.description(hippo)
# so therefore self becomes hippo, self = hippo as it's the current object
# self doesn't parse data, it's almost a key to say "this is the hippo instance"
# then hippo.name would find the hippo instance and find the name within that, only when called



# 9 / 18 - Member variables, ones that are available to all members of a class 
print("Member variables...")
cat = Animal("Boots", 3)
print (hippo.is_alive) # printing out true, the default value
hippo.is_alive = False # setting it to false
print (hippo.is_alive) # printing it as proof
print (cat.is_alive) # proof that we only changed Hippo, not Cat (morbid btw)


class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "Good" 
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)

hippo = Animal("Elliot", 8)
sloth = Animal("ben", 47)
ocelot = Animal("Zeus", 2)

print(hippo.health)
print(sloth.health)
print(ocelot.health)

# rejected over my solution as I spelt Good with a G, not a g




# 10 / 18 - Modelling real world objects

print("Shopping cart example...")

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print (product + " added.")
    else:
      print (product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print (product + " removed.")
    else:
      print (product + " is not in the cart.")

my_cart = ShoppingCart("Elliot")
my_cart.add_item("Bananas", 2) # I think JSON or react guards against this potential error happening - the dots are aligning!!!




# 11 / 18 - Starting inheritance

# Where a class takes on the ayyributes and methods of another
# used to express an is-a relationship
# This is to say a bear class or a bird class could inherit from an animal class, but not from each other


class Customer(object):
  """Produces objects that represent customers."""
  def __init__(self, customer_id):
    self.customer_id = customer_id

  def display_cart(self):
    print ("I'm a string that stands in for the contents of your shopping cart!")

class ReturningCustomer(Customer):
  """For customers of the repeat variety."""
  def display_order_history(self):
    print ("I'm a string that stands in for your order history!")

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()




# 12 / 18 - Inheritance syntax
# syntax is:
# class DerivedClass(BaseClass):
print("Inheritance with shape classes")

class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    super().__init__(3) #added this back in
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3


# print(Triangle.number_of_sides)    # this one errors

#wrong
""" t = Triangle(3)
print(t.number_of_sides)    # this also errors """

#wrong
""" t = Triangle(1,2,4)
t.Shape.__init__(3) """

# also wrong
""" t=Triangle((Shape,3), 3, 4, 5) """


# right, I did have it basically, it was the super() I was missing
t = Triangle(3, 4, 5)
print(t.number_of_sides)

# the way without the super clause is 
Shape.__init__(t, 3) # so I was actually close on line 337






# 13 / 18 - Overriding methods and attributes
# When you want a new class to take something on, but re-define it

class Employee(object): # objectively a hilarious line, (object is legacy from Py 2 btw)
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
      self.hours = hours
      return hours * 12.00
    
e1023 = Employee("Bob") # numbers are values, not containers, so need the 'e'
print(e1023.employee_name)
print("And this should print their wage...")
print(e1023.calculate_wage(40)) #800.0

e2059 = PartTimeEmployee("Charlie")
print(e2059.employee_name)
print(int(e2059.calculate_wage(20))) #240



# 14 / 18 - Exploring the use of Super
# how it has been sold is that it can be used at any time 
# and allows the derived class can have a method or attribute 'reset'
# terminology is base class or superclass btw

print("amending our part time employee class...")
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
      self.hours = hours
      return hours * 12.00
    
    def full_time_wage(self, hours):
      return super().calculate_wage(hours)

milton = PartTimeEmployee("Milton")
print("Full time equivalent rate is... ")
print(milton.full_time_wage(10))


# super() is important as when you have a chain of classes, it just jumps up once
# hard coding above might not be what you actually want]

# it's changed between Py 2 and Py 3 to become much simpler btw


# 15 / 18 - Making out own class (again)
print("15/18...")
class Triangle(): # don't forget (object) if in Python 2
  print("For debugging, you have entered the Triangle class")

  number_of_sides = 3 # 16 / 18

  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3

  def check_angles(angle1, angle2, angle3):
    if((angle1+angle2+angle3) == 180): return True
    return False
  
  def self_check_angles(self, angle1, angle2, angle3):
    if((self.angle1+self.angle2+self.angle3) == 180): return True
    return False
  
  def self2_check_angles(self):
    if((self.angle1+self.angle2+self.angle3) == 180): return True
    return False
  
  


# 16 / 18 - adding a member variable and method
# this is to the Triangle class below

print("Checking out our new check angle function...")
print(Triangle.check_angles(90, 90, 90))
print(Triangle.check_angles(90, 90, 0))

# look how neat that is! And correct first try, this is absolutely progress
# although I did set it up the wrong way round but did notice the error
# obviously Codeacademy didn't like my answer, they even used an "else"!


# 17 / 18 - getting personal, making my own one
print("17/18...")
my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
#print(my_triangle.check_angles())
#print(my_triangle.self_check_angles(my_triangle))
print(my_triangle.self2_check_angles())

# okay, I think we learned something there
# by parsing self, you give the function acess to all the vars in that instance