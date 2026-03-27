# 1 / 11 - Class basics (did we not just sort of do this??)
class Car(): # don't forget (object) in py 2
    condition = "new"
    def __init__(self, model, colour, mpg):
        self.model = model
        self.colour = colour # obviously the solution was rejected for this
        self.mpg = mpg

    def return_beans():
        return "beans" 

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