meal = 44.50
tax = 6.75 / 100
tip = 15.0 / 100

meal *= (1 + tax)
print(meal)

total = meal + meal * tip
print(total)

#short 6 q test

#Strings & Console output
brian = "Hello life!"

caesar = "Graham"
praline = "John"
viking = "Teresa"   
print (caesar)
print (praline)
print (viking)

#fix this: 'This isn't flying, this is falling with style!'
#you can use the backslash to allow ''s 

string = ("This isn't flying, this is falling with style!")
print(string)
#this works in Py 3, but not 2!

montyName = "MONTY"
fifth_letter = montyName[4] #make sure to use [] and not ()
print (fifth_letter)

parrot = "Norwegian Blue"
print (len(parrot))
print (parrot.lower())
print (parrot.upper())

pi = 3.14
print (str(pi))

ministry = "The Ministry of Silly Walks"

print (len(ministry))
print (ministry.upper())

"""Tell Python to print "Monty Python"
to the console on line 4!"""
print("Monty Python")

"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print(the_machine_goes)


print ("Spam " + "and " + "eggs")

print ("The value of pi is around " + str(3.14))

string_1 = "Camelot"
string_2 = "place"

print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
print (f"Lets not go to {string_1}, tis a silly {string_2}")

name = "Alex"
quest = "Teaching Python"
color = "Blue"

print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))

my_string = "lets get this over with   "
print(len(my_string))
print(my_string.upper())
