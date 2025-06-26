#Lists are similar to arrays - seems reasonable.
#Lists can contain as many variables as you like, and are easy to iterate over

mylist = []
for x in mylist:
    print(x)
print("Done printing initialised list in for loop, now manually:")
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1, note that we have started at 0!! I reckon this will get confusing later
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

print("okay, and in a for loop they look like:")
# prints out 1,2,3
for x in mylist:
    print(x)

#If you tried to call mylist[5] you'd obviously get an error, because it only has info at 0, 1 and 2

""" In this exercise, you will need to add numbers and strings to the correct lists
 using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers" list,
   and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, 
using the brackets operator []. Note that the index is zero-based, so if you want to access 
the second item in the list, its index will be 1. """
print("Start of exercise task:")
#Initial code:
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

print("Completed exercise task:")
#_______________________________________________________________________________________
#Copy of the code that we will edit to implement changes

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
for x in range(1, 4):
    numbers.append(x)

strings.append('hello')
strings.append('world')

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
#print("The second name on the names list is %s" % second_name)
print(f"The second name on the names list is {second_name}") #This flagged an error on the website, it didn't like the f string
