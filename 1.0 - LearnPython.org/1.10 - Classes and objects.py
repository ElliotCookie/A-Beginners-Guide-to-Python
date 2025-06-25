#A class is basically a template to create an object
#A class gives variables and functions to an object so it can be made
#Therefore, an object is a blend of variables and functions into one thing

#We are going to go into it, for now we just have to accept that (self) is a thing
#A basic class might look like:

class MyFirstClass:
    OpeningType = "Front door" #this is a string variable
    QuantityOfOpenings = 4

    def WaysToEnterHouse(self):
        self.QuantityOfOpenings += 1 #dont pass variables normally, use this self. thing
        print ("We are now printing ways to enter a house")

TrialObject1 = MyFirstClass() #TO now contains the string and function

#The string inside the object is still ours to meddle with!
#It needs accessing with correct formatting though. It's the .  <-

PrintableDemoVariable = MyFirstClass.OpeningType
print(PrintableDemoVariable)

#We can have several obects of the same class
TrialObject2 = MyFirstClass()
TrialObject2.OpeningType = "Back door"
print(f"Opening type of TO2 is {TrialObject2.OpeningType}")

#Accessing a function in the class is similar to accessing the variable
TrialObject1.WaysToEnterHouse()

#__init__ is a special function (a dunder one, short for double underscore)
#It gets called when the class is being initiated

#Is is using for assiging values in a class,
#allowing you to pass values at the moment of creation

#This means we can have different objects with different properties,
#without manually reassigning all of them 

class PokemonClass:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def returnName(self):
        return self.name

TestObject = PokemonClass("Bulbasuar", "Grass")
print(TestObject.returnName()) #dont forget the extra ()

""" 
Exercise
We have a class defined for vehicles.
Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer, 
and car2 to be a blue van named Jump worth $10,000.00. """

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())


""" BUT THERE MUST BE A BETTER WAY!!! SHORTER!!"""
class Vehicle2:
    def __init__(self, name, body, colour, value):
        self.name = name
        self.kind = body
        self.colour = colour
        self.value = value

    def description2(self):
        return f"{self.name} is a {self.colour} {self.kind} worth ${self.value:.2f}."
    
car3 = Vehicle2("Fer", "convertible", "purple", 30000.00)
car4 = Vehicle2("Jumper", "tank", "green", 1000000.00) #dont forget to input as floats and not strings
print(car3.description2())
print(car4.description2())

