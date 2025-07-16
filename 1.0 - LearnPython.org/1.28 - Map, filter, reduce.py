# These have all been invented in the interest in enabling shorter code
# Because of this, they seem relatively complicated
# They basically let you apply a function across a bunch of iterables at once

""" M A P """
# This has the following python syntax
# map(function, iterables), e.g:
mapped = map(lambda x: x * 3, [1, 2, 3])
print(list(mapped))
# MAP has cleanly applied a function to every item on our conveyor belt

# MAP can also take multiple arguments to do more complicated stuff
numbers = [1, 2, 3]
letters = ["a", "b","c"]
combination = map(lambda n, l : f"{n}{l}", numbers, letters[::-1])
print(list(combination))
#this is as much of a lesson on lambda functions as it is maps
#but you can do pretty powerful stuff, very cool

#looks like we have just done what we were going to do with the zip function
#lets do it anyway
moreNumbers = [5, 6, 7, 8]
zipped = zip(numbers, moreNumbers)
print(list(zipped))
#but this misses no 8, and I SPECIFICALLY wanted this one
from itertools import zip_longest # here we go!! 
zippingAgain = zip_longest(numbers, moreNumbers, fillvalue="-")
print(list(zippingAgain))



