""" Indexing allows you to access individual values from a sequence. 
In this lesson you’ll learn to extract,
 modify and replace a specific range of elements from 
 sequences with a new technique: slicing. """

movies = ["Avengers", "Avatar", "Titanic"]
print(movies[1])

#two paywalls in a row, showing that slicing is the format [x:y] with a semicolon

animals =['dog', 'cat', 'bird', 'cow']
print(animals[0:3]) #interesting this stops seemingly early 
#e.g. cow isn't printed

colors = ['red', 'green', 'blue', 'yellow']
print(colors[2:3])

color = 'pink'
print(color[1:4])

#ahh okay, so in the example above
#3 - 0 = 3, therefore 3 things printed

""" Lesson Takeaways
Great job! You learned that:

🌟 You can extract a section of a sequence with slicing

🌟 Slicing a list produces another list

🌟 Slicing a string produces another string """