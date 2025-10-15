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