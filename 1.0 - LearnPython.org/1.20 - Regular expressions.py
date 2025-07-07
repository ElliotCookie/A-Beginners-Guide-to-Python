#Regular expressions (regexp, regex or re) are a text pattern matching tool
#In python this is the re module, but it carries across to other languages also
#it's pretty complicated and huge. You're actually best off reading the
#standard python docs on it (the sacred texts!!)
#for now, lets go over the basic pattern keyword thingys
""" 
\d = digit
\w = word character 
. = any character
*, +, ? = repetition
() = groups
[] = sets
^, $ = start/end of a string
 """

import re # this is what are are learning about
import requests #how we make an external HTTP request

queryOfNames = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0") #.get is a funtion in the requests library
pokemonList = queryOfNames.json() #requests return in JSON so this allows python to read that
names = [pokemon['name'] for pokemon in pokemonList['results']] #List comprehension!!

charsToMatch = input("Type a bit of a name: ").strip() #removes leading and ending whitespace

scanningFormula = re.compile(f"^{charsToMatch}", re.IGNORECASE) #matches lowercase
matches = [name for name in names if scanningFormula.match(name)] #list comprehension!

if matches:
    print("Matching cases: ")
    for name in matches:
        print(name)
    else:
        print("No matching cases")

