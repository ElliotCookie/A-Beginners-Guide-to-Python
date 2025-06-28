#A module is a file that is responsible for a thing
#I'm going to boldly make a cooking analogy and for cooking pasta
#You'd have a kneading module, a gas hob module, and a kettle module
#They all do their own weird little bit
#Obviously in our case, it's just a .py file a bunch of times

#buckle up, it's looking complicated

#So modules use the (reserved) keyword 'import', e.g.
""" import 1.01 - Hello world.py """
#EXCEPT that modules CAN'T START WITH A NUMBER!! so all our progress is just...

#It then looks like you basically use it like a function
#Lets see if it lets us make one up

import myfirstpythonfile #important all lowercase and no spaces or numbers
StringToPrint = "Hello World"
myfirstpythonfile.MyFirstPrintingClass(StringToPrint)
#This throws an error but idc, I think that's the righ

#Back to the cooking analogy
#This mail file is like the work surface or counter level, and all the actions are done here
#A module is a drawer or cupboard and contains tools (kettle)
#An object or function is the tool (boiling water, just go with it)

import kettle 
kettle.boilwater() 
#this is okay, but each time I need to go to the cupboard (kettle.) and put it on the counter
#if I do
from kettle import boilwater
boilwater()
#I've now got the kettle on the counter and can boil water without visiting the cupboard

#we can take this further actually
from food_processor import blend, grate #(you can do import * to bring in everything, but that's naughty!!!)
import food_processor #(gets you the other stuff)
food_processor.mix() #but you still need to put it on the surface each time (it's the -> .)



#A cool thing is renaming your module on the import
if pasta_is_raw:
    import kettle as next_step
else:
    import stir_into_sauce as next_step

next_step.cook(weight_of_pasta) #cook is a function that takes WoP

#New direction--------------------
""" #So a singleton is a general, resulable solution (called a design pattern)
#where only one instance of it exists. Once it's created it becomes the reference point
#It's basically what happens when your mum buys chicken nuggets for the freezer
#and then you ask for them when you're out in town
#"No, we have chicken nuggets at home"
#The chicken nuggets are acting/effectively (that's actual technical terminology)
#as a SINGLETON
#This is important to remember when we think about "initialising a module" (running a programme)

#Lets say we have module A (MA) that calls module B (MB). 
#When we do (keyword) import, python runs MB once and adds it to it's sys.modules list
#Later on in our code, MA calls for module C (MC).
#If MC calls for MB, python says: "No, we have chicken nuggets at home!"
#Module B acts as a singleton, and python will use this already-loaded copy """

#PYTHONPATH
""" dsds 
Basically when you import, python has a few key locations it will check
this saves us having to define it, and as long as we are roughly logical
with where we save a module then it looks like it will search the right areas
so same system folder, your python folder, other libraries etc """
#PYTHONPATH lets us give a quirky reference to a module that is 
#lets say on a USB or something a bit different
"""One thing that makes sense to mention here and not later,
your .py modules need to have an (empty) __init__.py file in the folder
Python can't  import your module(s) without this little file"""


#BUILT-IN MODULES
""" One of the reasons that python is LIT is that there is a bunch of modules
that come with it. You can import more for data science or AI or whatever...

Apparently, dir and help are very useful functions.
In this snippet we will look at how to de-shroud the black box """

import urllib
dir(urllib)
help(urllib.urlopen)

#________ E X E R C I S E ___________
#In this exercise, print an alphabetically sorted list of all the
#functions in the re module containing the word find.

import re

# Your code goes here
find_members = []

#search all the functions in the re module
#if a function contains the word "find" then add it to a list
#sort the list into alphabetical order
#print the (newly alphabetically ordered) list

for dir() in dir(re).length():
    if "find" in dir() == True:
        find_members.append(dir())
    
def mergesort(list):
    middle = len(list) // 2 # // is integer floor, rounds down to nearest whole no
    left_half = find_members[0 : middle]
    right_half = find_members[middle : ]
    return merge (left_half, right_half)

def merge (left_half, right_half):
    i = 0, j = 0, merged = []
    #while LH and RH have stuff in, this is a signal to populate MERGED
    while len(left_half) + len(right_half) <> 0: #need syntax for is not equal
        for i in len(left_half):
            for j in len(right_half):
                #WHICH IS BIGGER
                if left_half[i] < right_half[j]:
                    merged.append(left_half[i]) #this is at the back and needs to be at the front!
                    left_half.pop(left_half[i])
                else:
                    #EITHER WAY, MOVE THE SMALLEST ONE OUT
                    merged.append(right_half[i])
                    right_half.pop(right_half[i])
                #this will slowly remove things from LH RH
                #does this lock in the length when it's initialised? I need to index only the 0 location at one point
    return merged #but this will only ever be half the list in total? 
    #when do we stop?

#I need to be breaking down left half (and RH) again
#this could pass left half = 3 and rh = 4
#I then need to function(mergesort) left half into 1 and 2
#but, I need to be careful not to overwrite the stuff that's important

mergesort(find_members)
print(find_members)

""" time to ask chat gpt for some input, I'll paste with updates """




import re

# Your code goes here
find_members = []

for name in dir(re): #input name, removed.length
    if "find" in name: #therefore had to change this to name, removed '== True'
        #find_members.append(dir())   <--- removed
        find_members.append(name)
    
def mergesort(list):
    #triggers when things are already sorted, e.g [8]
    if len(list) <= 1:
        return list # *** where value is returned
    
    middle = len(list) // 2 # // is integer floor, rounds down to nearest whole no
    left_half = list[0 : middle]
    right_half = list[middle : ]

    #adding in sorted lists
    #I think we are saying there is almost a phantom break here, that this will eventially produce a list length of 1 item each, and it's these two we feed into merge?
    sorted_left = mergesort(left_half) #gets the value from return line ***
    sorted_right = mergesort(right_half)
    
    #Needs updating to sorted left and sorted right
    return merge (sorted_left, sorted_right)

def merge (left_half, right_half): #takes two sorted lists and produces a combined list, keeping the order
    i = j = 0
    merged = []
    #while LH and RH have stuff in, this is a signal to do stuff
    while i < len(left_half) and j < len(right_half): #changed, catches empty case
        #Looping through a little more manually now
        if left_half[i] < right_half[j]:
            merged.append(left_half[i]) #this is at the back and needs to be at the front!
            i += 1
        else:
        #EITHER WAY, MOVE THE SMALLEST ONE OUT
            merged.append(right_half[j])
            j += 1
        #this will slowly remove things from LH RH
        #does this lock in the length when it's initialised? I need to index only the 0 location at one point
    #At this point, one half is empty (= 0)
    merged.extend(left_half[i:]) #extend is like append but for many things (one by one)
    merged.extend(right_half[j:])    
    return merged 
    
sortedfunctionsHITfinds = mergesort(find_members)
print(sortedfunctionsHITfinds)                 


# ----------------------------------------

#mergesort(28794621)
#Split into left_half = [2879] and right_half = [4621]
#    mergesort(2879)
#    Split into [28] and [79]

#        mergesort(28)
#        Split into [2] and [8]
#            mergesort(2) returns [2] (base case)
#            mergesort([8]) returns [8] (base case)
#        merge(2, 8) produces SORTED (2 8)

#        mergesort(79) 
#        merge similarly produces SORTED [79]
#    merge SORTED (28, 79) produces SORTED [2 7 8 9]

#    mergesort(4621)
#    Split into [46] and [21]
#        mergesort(46)
#        Split into [4] and [6]
#            mergesort(4) returns [4] (base case)
#            mergesort([6]) returns [6] (base case)
#        merge(4, 6) produces SORTED (4 6)

#        mergesort(21) 
#        merge similarly produces SORTED [21]
#    merge SORTED (46, 21) produces SORTED [1 2 4 6] 
 
#merge SORTED [2 7 8 9] [1 2 4 6] PRODUCES SORTED 1 2 2 4 6 7 8 9


# Note: Each recursive call "pauses" at the split, works on smaller lists,
# and only returns to merge its two sorted halves back into the caller.
# The actual ordering decisions (comparisons) all occur inside the merge() function.

#it's hard to see with just 2 digits. but it's basically 'feed in this'
# and then 'merge will spit out this'    






