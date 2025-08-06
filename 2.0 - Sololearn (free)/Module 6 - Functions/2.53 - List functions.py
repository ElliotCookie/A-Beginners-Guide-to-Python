""" Lists are an essential concept in coding.
They let you store multiple values in a single variable,
making the program more efficient and organized.

In this lesson you'll learn to use built-in list functions. """

#len() is one of the most useful built-in functions. len() stands for length and,
#  when used on lists, it returns the number of items in the list.
# len() is a very useful function that accepts a wide range of arguments. 
# It’s not specific to any one particular data type or object, 
# so you don’t use dot notation to call it.

""" The append() function adds a new item to the end of a list. 
append() is called using dot notation because it’s specific to lists. """

#The insert() function allows you to add an
#  element to a list, at a specific position.


""" insert() takes 2 arguments. The first is the index (where to insert)
 and the second is the item (what to insert). """
colors = ["Red", "Blue", "Yellow"]
colors.insert(0, "Green")
print(colors)

colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
print(colors)

colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])

""" The pop() function removes an element from a list.

That position indicated by the index is the only argument
 that the pop() function accepts. """

points = [15, 36, 74, 88]
points.pop(2)
points.append(95)

#bro this is so much mental arithmatic for what?? I get the point

""" Lesson Takeaways
Great job! You learned that:

🌟 len() returns the number of items in a sequence

🌟 append() adds an item to the end of a list

🌟 insert() and pop() add and remove list items at specific positions """