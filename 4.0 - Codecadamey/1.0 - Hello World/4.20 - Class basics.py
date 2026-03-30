# 1 / 11 - Class basics (did we not just sort of do this??)
class Car(): # don't forget (object) in py 2
    condition = "new"
    def __init__(self, model, colour, mpg):
        self.model = model
        self.colour = colour # obviously the solution was rejected for this
        self.mpg = mpg

    def return_beans():
        return "beans" 
    
    def display_car(self):
        print(f"This is a {self.colour} {self.model} with {str(self.mpg)} MPG.")

    def drive_car(self):
        self.condition = "used"
        print(self.condition)
        

my_car = Car("DeLorean", "silver", 88)

# 2/ 11 - creating an instance of the object

# 3 / 11 - adding a member variable, condition

# 4 / 11 - printing member var
print(my_car.condition) # new

# 5 / 11 - Initialising a class
# do they realise we've just done this? The explanations are like it's the first we are hearing of it

# to assign a variable to the class (creating a member variable)
# use dot notation
# but then the followup example mismatches new_variable and newVariable which isn't useful
print("Checking instance variables have worked...")
print(my_car.mpg)

# solution rejected for using colour over color


# 6 / 11 - Printing those new varibales we have made
print(my_car) # <__main__.Car object at 0x000002619DB26A50>
#ahh, so there is a nice way to print everything:
print(my_car.__dict__)

#but notice how this deosn't contain "new"
print(Car.__dict__)

# this contains much more info!

print("Testing printing the items one by one...")
for item in my_car.__dict__:
    print(item) # Dictionary key name
    print(my_car.__dict__[item]) # accessing the value at that point in the dictionary

# ERROR "You should get the model of my_car by calling my_car.model."
# I've literally cracked the code, how are you not entertained
    

# I'm just going to add a function to see if it appears in dict
# the verdict was that it doesn't




# 7 / 11 - Creating class methods
# telling us again that as well as variables, classes can have methods too 
# a function offers global utility
# a method is a behaviour of an object
# a method is just a function that knows what object it belongs to


print("adding a display class method...")
my_car.display_car()
# got it right first time, which is worrying... 
# but I used an f-string and not the %s method, so my solution will be rejected
# print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))




# 8 / 11 - Modifying member variables
# adding in a drive_car method
print("Driving car and making it used...")
print(my_car.condition)
my_car.drive_car()
#print(my_car.condition)




# 9 / 11 - Inheritance 
print("Adding an electric car...")
# I'm going to add the car class again as it is so far away 

class Car(): # don't forget (object) in py 2
    condition = "new"
    def __init__(self, model, colour, mpg):
        self.model = model
        self.colour = colour # obviously the solution was rejected for this
        self.mpg = mpg

    def return_beans(self):
        return "beans" 
    
    def display_car(self):
        print(f"This is a {self.colour} {self.model} with {str(self.mpg)} MPG.")

    def drive_car(self):
        self.condition = "used"
        print(self.condition)



class ElectricCar(Car):
    def __init__(self, model, colour, mpg, battery_type):
        super().__init__(model, colour, mpg)
        self.battery_type = battery_type
        
my_car = ElectricCar("Prius","black", 80,"molten salt")       

for item in my_car.__dict__:
    print(f"{item}: {my_car.__dict__[item]}")

# There are a few ways to deal with the illogicality of passing an unwanted mpg up

#1 
dont_offer_one = ElectricCar("Benz", "green", None, "Lithium")

#2
class ParseUpNone(Car):
    def __init__(self, model, colour, mpg, battery_type):
        super().__init__(model, colour, mpg=None)
        self.battery_type = battery_type

in_the_method = ParseUpNone("A4", "black", 0, "Duracel")

#3 
# Design better - make a subclass for pertrol car, and electric car, or a vehicle parent class
# If a class is ignoring parent attributes then inheritance is likely wrong

new_cars = [my_car, dont_offer_one, in_the_method]

for car in new_cars:
    print()
    print(car) # <__main__.ElectricCar object at 0x00000227C77F6E40>
    for item in car.__dict__:
        print(f"{item}: {car.__dict__[item]}")


# helping myself and finding a better way to print the names    
print(dir(my_car))
""" ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__',
 'condition', 'display_car', 'drive_car', 'return_beans'] """

for item in dir(my_car):
    print()
    #print(item)
    # print(ParseUpNone.item) - this will error as no attribute ".item"
    hidden_thing = getattr(my_car, item)
    print(hidden_thing)


    # expanding a bit
    # created the hidden_thing var
    # changing to my_car
    if callable(hidden_thing) and not item.startswith("__"): # == True:   remember that hack
        # print("callable")
        hidden_thing()

for i in range(4):
    print()

# all of that turned out to be useless and not give the answer I wanted
# what I want is: 
print("Found nice output solution")

for car in new_cars:
    print()
    print(car.__class__.__name__)
    for item in car.__dict__:
        print(f"{item}: {car.__dict__[item]}")