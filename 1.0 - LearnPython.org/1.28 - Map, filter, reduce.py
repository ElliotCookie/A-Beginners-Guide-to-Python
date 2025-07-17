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

""" F I L T E R """
# Map passes everything and that's great, filter first gets some boolean values
# I'm assuming it uses these to decide what gets mapped. Syntax:
# filter(function, iterable)

# Only 1 iterable is required, so it goes without saying...
# The function must only take one argument, which must return a boolean type

pokemonAndMoves = {
    "Dragonite":  {"Fly", "Outrage", "Extreme Speed"},
    "Bulbasaur":  {"Tackle", "Absorb", "Solar Beam"}}

priorityMoves = ["Quick Attack", "Extreme Speed"]

def doesPokemonHavePriority(pokemon):
    moves = pokemonAndMoves[pokemon] #square brackets!
    return any(move in priorityMoves for move in moves)
            
priorityPokemon = filter(doesPokemonHavePriority, pokemonAndMoves)
print(list(priorityPokemon))

# That was with our own function, lets try using a built i (lambda) one
# I quite like the example actually 

backwardsWords = ["hello", "test", "kiosk", "anutforajaroftuna", "hannah",
                  "go hang a salami im a lasagna hog" "racecar", "godog", 
                  "yobananaboy", "neveroddoreven"]

palindromes = filter(lambda word: word == word[::-1], backwardsWords)
print(list(palindromes))

""" R E D U C E """
# Passes the elements to an interable function of two arguments. Syntax:
# reduce(function, iterable[, initial])
#(that is horrible, with the [,) unless it is a typo

# it's main benefit over a loop is it removes the logic
# obviously there is also a nice chain with map and filter

from functools import reduce
cart = [
    {"name": "eggs", "price" : 1.99},
    {"name": "milk", "price" : 0.99},
    {"name": "cheese", "price" : 2.99},
]

total = reduce(lambda acc, item: acc + item["price"], cart, 2.79) #delivery
print(f"{total:.2f}") # otherwise like 12 dp