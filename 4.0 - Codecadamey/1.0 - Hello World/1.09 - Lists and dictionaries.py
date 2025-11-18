zoo_animals = ["pangolin", "cassowary", "sloth", "badger"];
# One animal is missing!

if len(zoo_animals) > 3:
  print ("The first animal at the zoo is the " + zoo_animals[0])
  print ("The second animal at the zoo is the " + zoo_animals[1])
  print ("The third animal at the zoo is the " + zoo_animals[2])
  print ("The fourth animal at the zoo is the " + zoo_animals[3])

#---

numbers = [5, 6, 7, 8]

print ("Adding the numbers at indices 0 and 2...")
print (numbers[0] + numbers[2])
print ("Adding the numbers at indices 1 and 3...")
print (numbers[1] + numbers[3])


zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
# the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "eel"




#lists don't have to have a fixed length, you can add whenever
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("suncream")
suitcase.append("sunhat")
suitcase.append("thongs")

list_length = len(suitcase) # Set this to the length of suitcase

print ("There are %d items in the suitcase." % (list_length))
print (suitcase)


# New lesson
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4] # remember to plus one at the end

# The last two items (index four and five)
last =  suitcase[4:6]


animals = "catdogfrog"

# The first three characters of animals
cat = animals[:3]

# The fourth through sixth characters
dog = animals[3:6]

# From the seventh character to the end
frog = animals[6:] # notice the overlap





animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")

print (animals) # Observe what prints after the insert operation




# Using for loops to go over an entire list
my_list = [1,9,3,8,5,7]

for number in my_list:
  # Your code here
  print(number * 2) #no need for the [], because indexing is already handled




start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
  square_list.append(number**2)
square_list.sort() #don't forget brackets
print (square_list)  



#Dictionaries
#these use keys to look things up, instead of an index
d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
#also notice the different brackets

# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print (residents['Puffin']) # Prints Puffin's room number

# Your code here!
print(residents['Sloth'])
print(residents['Burmese Python'])



#these are mutable, so we can add to them after they are created
#empty {} is an empty dict
#len counts the amount of pairs, not keys and item stored '
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print (menu['Chicken Alfredo'])

# Your code here: Add some dish-price pairs to menu!
menu['Pasta pizza'] = 16
menu['Kebop'] = 12
menu['Drink'] = 3

print ("There are " + str(len(menu)) + " items on the menu.")
print (menu)