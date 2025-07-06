#Functions obviously take in arguments, which are a fixed amount and order
#if we know what the function is and there is little dynamism
#*args and **kwargs let you write funcitons that can take a 
#variable amount of arguments. Very useful when you don't know ahead
#of time exactly how many inputs the function will need

#*args
def pokemonMovePrinter(name, *moves):
    i = 1
    for move in moves:
        print(f"{name}s  {i} move is {move}")
        i += 1
pokemonMovePrinter("Mudkip", "Tackle", "Watergun", "Leer")

#**kwargs
def pokemonStatsPrinter(name, **stats):
    print(f"{name}s stats:")
    for stat, value in stats.items():
        print(f" {stat}: {value}")
pokemonStatsPrinter("Mudkip", HP = 50, Attack = 70, test = 60)
pokemonStatsPrinter("Pikachu", Def = 80, SpAtt = 90, Speed = 100)
""" 
Exercise
Fill in the foo and bar functions so they can receive a variable amount
of arguments (3 or more) The foo function must return the amount of extra
arguments received. The bar must return True if the argument with the 
keyword magicnumber is worth 7, and False otherwise. """

# edit the functions prototype and implementation
def foo(a, b, c, *d):
    i = 3
    for things in d:
        i += 1
    return len(d) #you just need this line and nothing else!
    return i  
      

def bar(a, b, c, **d):
    return d["magicnumber"] == 7 #you just need this line and nothing else!
    if d == 7:
        return True
    else:
        return False
    return d["magicnumber"] == 7


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")
if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")