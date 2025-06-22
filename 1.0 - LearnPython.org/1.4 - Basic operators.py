#So a basic operator is another name for + or * or / I think
#% also counts, we know this gives the remainder
#using ** is power

number = 2**3
print(f"2**3 is {number}")

#you can also add strings together which is a bit funky
hello ="hello"
world = "world"
helloworld = hello + world
print(helloworld)

#you can multiply strings!! Wth?! 
lotsofhellos = hello * 10
print(lotsofhellos)

#lists, that we learnt in the previous lesson can be added
StartOfList = [1, 2, 3]
EndOfList = ['Dogs', 'Cats'] #always comes out with ' even if you use "
LongList = StartOfList + EndOfList
print(LongList)

#multiples of lists can also be printed
print(f"This is what Start of list * 4 looks like: {StartOfList * 4}")


""" The target of this exercise is to create two lists called x_list and y_list,
which contain 10 instances of the variables x and y, respectively.
You are also required to create a list called big_list, which contains the variables x and y,
10 times each, by concatenating the two lists you have created. """

x = object()
y = object()

# TODO: change this code
x_list = []
y_list = []

for i in range (10):
    x_list.append(x) #Here we had to use curvy brackets because (I think) it's an object
    y_list.append(y)

big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

#Not foretting comments, commit, stage (?), open old branch, merge, upload (to rem repo)