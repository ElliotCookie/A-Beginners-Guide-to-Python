"""
Description: Short story thingy
Author:  Elliot
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."
print("Journey has started")
name = input("Enter a name: ")
adj1 = input("Please provide adjective #1")
adj2 = input("Please provide adjective #2")
adj3 = input("Please provide adjective #3")
verb1 = input("And a verb please: ")
noun1 = input("Two nouns now, 1/2: ")
noun2 = input("Two nouns now, 2/2: ")
animal = input("Animal: ")
food = input("Food: ")
fruit = input("Fruit: ")
superhero = input("Superhero: ")
country = input("Country: ")
dessert= input("Dessert: ")
year = input("Year: ")

#don't forget to use CTRL + H to replace all

print(STORY % (name, adj1, adj2, animal, food, verb1, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2))

#can't complete the module, the 12th of 12 steps is to get an AI code overview
