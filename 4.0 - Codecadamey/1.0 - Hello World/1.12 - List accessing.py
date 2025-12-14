n = [1, 3, 5]

print(n[1])

n[1] = n[1] * 5
print(n[1])

n.append(4)
print(n[3])

#taking stuff off a list
""" 
- n.pop(index) will remove the item at index from the list and return
- n.remove(item) will remove the actual item if it finds it
- del(n[1]) is like .pop in that it will remove the item at the given index, but it won’t return i
"""

del(n[0])

#altering a function
number = 5

def my_function(x):
  return x * 3

print (my_function(number))


def add_function(x, y):
  return x + y


n = "Hello"
def string_function(s):
  return str(s) + "world"

print (string_function(n))


def list_function(x):
  return x

n = [3, 5, 7]
print (list_function(n))


def list_function(x):
  x[1] = x[1] + 3
  return x

n = [3, 5, 7]
print (list_function(n))

def list_extender(lst):
  lst.append(9)# Add your function here
  return lst


def print_list(x):
    for items in x:
      print(items)

print_list(n) # had the right code but it didn't like it bcos spacing

#Mental note for later, this List and Functions bit is really good
#probably the best bit of the course so far, just bashing out examples

def double_list(x):
  new_list = []
  for item in x:
    new_list.append(x*2)

#oh, they give you scaffold:
n = [3, 5, 7]

def double_list(x):
  for i in range(0, len(x)):
      x[i] = x[i] * 2
  # Don't forget to return your new list!
  return x

print(double_list(n))


#Passing a range into a function

def my_function(x):
  for i in range(0, len(x)):
    x[i] = x[i]
  return x

#print(my_function(range(0, 3, 1))) 
print(my_function(n)) #hmm, this is now broken

""" The range function has three different versions:

range(stop)
range(start, stop)
range(start, stop, step) """

#iterating over a list in a function
n = [3, 5, 7]

def total (numbers):
  result = 0
  for items in numbers:
    result += items
  return result

print(total(n))


#using strings in lists in functions (joining strings, concatonating)
def join_strings(words):
  result = ""
  for word in words:
    result = result + word
  return result

names = ["alice", "ben", "charles"]

print(join_strings(names))


#Joining two lists together
def join_lists(x, y):
  return x + y

print (join_lists(n, names))


#using a list of lists in a function
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  results = []
  for numbers in lists:
    for number in numbers:
      results.append((number))
  return results

print(flatten(n))

