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

#THAT'S ENOUGH FOR ME TODAY, START AT MODULE INITIALIZATION
