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



# 12 / 18 - Anonymous functions
# Python allows for 'functional programming' which means that functions can be parsed as variables
# This is quite powerful - not every language does this!
# Example:
lambda x: x % 3 == 0 # this is the ANYONYMOUS part, it doesn't have a name!
# is the same as 
def by_three(x):
  return x % 3 == 0

my_list = range(16)
# filter is another keyword introduced here, which isn't useful
print (filter(lambda x: x % 3 == 0, my_list))


# the basic format of filter is filter(function, iterable)
print("working out what filter does")
numbers = range(16)
result = (filter(by_three, numbers))
print(list(numbers))
print(list(result))
# so by this logic we could compound it for the printing only
print(list(filter(by_three, numbers)))

def not_multiple_four(x):
   return x % 4 != 0
print(list(filter(not_multiple_four, numbers)))
# Notice it is not function(x), this is because filter is it's own function

# List comprehensions are favourable over mabdas, if you can




# 13 / 18 - Lambda functions, lambda syntax

# best for when you need a quick one, not one you will use many times (then use def:)
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print (list(filter(lambda x: x == "Python", languages))) # ['Python']
print (next(filter(lambda x: x == "Python", languages)), None) # Python
# next is used to give the first thing it finds, so best used with a error catch

# next is useful to just quickly grab the first thing, so first line of a text file
# or to store the first row of an interable (headers) so you can read the data below





# 14 / 18 - testing lambda stuff, and list comprehensions

print("Squares list comp test...")
squares = [x**2 for x in range(1, 11)]
print(squares)
print("filtering this a bit...")
print(list(filter(lambda x: 30<x<70, squares)))



# 15 / 18 - iterating over dictionaries
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}
# let's not forget items(), values() and keys()
print(movies.items())




# 16/ 18 - List comprehensions practise
print("list of multiples of 3 and 5 in between 1 and 15")
threes_and_fives = [x for x in range (1, 16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives) 
# the IF is very important, and changes a) to b)
# a) [False, False, True, False, True]
# b) [3, 5, 6, 9, 10, 12, 15]





# 17 / 18 - List slicing
print("deciphering a message using slicing...")
# The message is backwards and we only want every other letter
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# From memory, we have [start:finish:step]
# It is a string, so an effective list of chars
reformatted = garbled[len(garbled):0:-2]
print(reformatted)
# I had :0: in the middle, but this missed the "!"
reformatted = garbled[::-2]
print(reformatted)




# 18 / 18 - Lamda expressions
print("Deciphering using lamda functions...")
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
# create a filter to remove X
message = (lambda x: x != "X", garbled)
print(message)
# WRONG - [<function <lambda> at 0x0000019AB124C0E0>, 'IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX']
message = filter(lambda x: x != "X", garbled)
print(message)
# WRONG - <filter object at 0x000002148DF035B0>
message = list(filter(lambda x: x != "X", garbled))
print(message)
# ['I', ' ', 'a', 'm', ' ', 'a', 'n', 'o', 't', 'h', 'e', 'r', ' ', 's', 'e', 'c', 'r', 'e', 't', ' ', 'm', 'e', 's', 's', 'a', 'g', 'e', '!']
message = "".join(list(filter(lambda x: x != "X", garbled)))
print(message)
# I am another secret message!
# This took some undocumented tries... # printing lists, joining lists
