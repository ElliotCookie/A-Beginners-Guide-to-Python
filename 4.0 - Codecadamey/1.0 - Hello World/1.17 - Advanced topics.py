# 1/18 - Iterators for dictionaries

my_dict = {"Topic1": "Variable", "Topic2": 1, "Topic3": 1.11}
print(my_dict.items()) # the () brackets are important

# 2/18 - Keys and values
# .items() returns tuple values of the key and value
# you'll never guess what .keys() and .values() do

my_dict = {"Topic1": "Variable", "Topic2": 1, "Topic3": 1.11}
print(my_dict.keys()) # the () brackets are important
print(my_dict.values()) # the () brackets are important

# 3/18 - the 'in' operator
# this is a protected keyword - the same as 'for' loops?

for key in my_dict:
    print(key, my_dict[key])

#another case of me matching the answer word for word and it not liking it...
