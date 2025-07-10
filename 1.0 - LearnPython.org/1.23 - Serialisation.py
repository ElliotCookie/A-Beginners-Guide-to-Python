# STERILISATION
# This is a way of turning an in-memory data structure into a portable format
# You can go the other way (desterilisation)
# This lets us all play nice together on our different systems and programmes
# JSON is a very popular sterilisation and python can handle it

# JSON has two formats of data, strings or object datastructures
# The string format is used to pass the data or open datastructures (ds)
# The datastructures format is a series of lists and dictionaries

#The loading method takes a string and turns it into the JSON ds
import json
""" print(json.loads(myFirstJSONThing)) """

#Encoding requires you to use the dumps method, turning an object into a string
json_string = json.dumps([1, 2, 3, "a", "b", "c"]) #brackets are important!
print(json_string)

#Python has moved on and now a fast serialisation method called cPickle is used
import pickle
pickleString = pickle.dumps([1, 2, 3]) # brackets again!
print(pickleString)
restored = pickle.loads(pickleString)
print(restored)

""" The aim of this exercise is to print out the JSON string
 with key-value pair "Me" : 800 added to it. """

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here

    salaries_dict = json.loads(salaries_json)
    salaries_dict[name] = salary

    salaries_json = json.dumps(salaries_dict)
    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])