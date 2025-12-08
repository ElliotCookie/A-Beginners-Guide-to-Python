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