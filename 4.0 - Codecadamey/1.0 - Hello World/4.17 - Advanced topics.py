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


# 4 / 18 - Building lists
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50,)


# 5 / 18 - List comprehension syntax
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0] # => [6]
# This was covered in 1.17, good to do a refresh

print("Even squares:")
even_squares = [x ** 2 for x in range(1, 11) if (x % 2) == 0]
print(even_squares,)


# 6 / 18 - Our own comprehension
print("Cubes by four:")
cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print(cubes_by_four,)
# again, another faff to get it to accept my working solution... 


# 7 / 18 - List slicing syntax
l = [i ** 2 for i in range(1, 11)] # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (l[2:9:2]) # [9, 25, 49, 81]

# 8 / 18 - How to chop - chopping lists - how to slice

to_five = ['A', 'B', 'C', 'D', 'E']
print (to_five[3:]) # prints ['D', 'E'] 
print (to_five[:2]) # prints ['A', 'B']
print (to_five[::2] )# print ['A', 'C', 'E']
# Default starting index is 0
# Default end is end of list
# Default stride is 1

my_list = range(1, 11) # List of numbers 1 - 10
# slice it to print odd numbers only
print("Printing odd numbers...")
print(my_list[::2]) # but appears as: range(1, 11, 2)
# Looked this up, this is because range(1,11) is start = 1, stop = 11, step = 1
# it doesn't store say [1, 2, 3, etc]
# the way to get around this is to call it as a list
print(list(my_list[::2])) #[1, 3, 5, 7, 9] (LIST is key)

#I'm also thinking that if we set it up differently (maybe using a comprehension!) it will work
nums_onetoten = [x for x in range (1, 11)]
print("Trying new assembly of the above...")
print(nums_onetoten[::2]) # [1, 3, 5, 7, 9]





# 9 / 18 - Reversing a list using negative stride, reverse list
backwards = my_list[::-1]
print("Printing backwards...")
print(list(backwards[::2]))




# 10 / 18 - Stride length, list traversal
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print("Backwards by tens challenge...")
print(list(backwards_by_tens))




# 11 / 18 - Final challenge 
print("Final challenge")

to_21 = [x for x in range(1,22)] # go one above each time
odds = to_21[::2]
lower_third, upper_third = int(len(to_21) * 1//3), int(len(to_21) * 2//3) # use // integer division and not / float division
middle_third = to_21[lower_third:upper_third:]

print(list(to_21))
print(list(odds))
print(list(middle_third))