#Noticed last night that all my files are now in the wrong order, so pressed
#F2 to rename them all and add a 0 at the front

#Todays lesson is DICTIONARIES!
#This is like an array (and therefore, like a list, but)
#It uses keys to access values. Think of it like a phonebook 
#You'd look up "Name" and the answer might be "Ash" (mixed data allowed)
#A list is like a todo list. You look up #1 (0 index tho) and it tells you
#"Ash" or 3.14 etc
#Arrays are like lists but same data types only. Good for maths!

#oh would you look at that, the first example they give is actually a phonebook!
waterTypeDamageMultiplyers = {}
waterTypeDamageMultiplyers["Normal"] = 1.0
waterTypeDamageMultiplyers["Fire"] = 2.0
waterTypeDamageMultiplyers['Grass'] = 0.5
print(waterTypeDamageMultiplyers)
#note that it prints 'fire' with a single ', no matter what

#We can change how a dictionary is initialised with a bit of notation
fireTypeDamageMultipliers = {
    "Fire" : 0.5,
    "Water" : 0.5,
    "Grass" : 2.0
} #the new things this way is the , and the : rather than =

#I'm reading that we can iterate over dictiionaries, but there is a
#knack to it, as it doesn't keep the order of values in it
for Type, Multiplier in fireTypeDamageMultipliers.items():
    print(f"Fire type attacks do {Multiplier} damage to {Type} Pokemon")

#Indexs can be removed using del or .pop
del fireTypeDamageMultipliers["Fire"] #or
fireTypeDamageMultipliers.pop("Water")

""" Exercise
Add "Jake" to the phonebook with the phone number 938273443, 
and remove Jill from the phonebook. """

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

#my code:
phonebook["Jake"] = 938273443
del phonebook["Jill"] #good riddance 

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")