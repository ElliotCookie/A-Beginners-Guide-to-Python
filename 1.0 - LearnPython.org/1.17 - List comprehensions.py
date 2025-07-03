#List comprehensions allow you to create a new list based on an existing one
#all in a single, readable line!? very cool
#There isn't a keyword to learn for this one, it is a syntax pattern containing
#square brackets [], a for loop, and an optional if condition

numbers = [1, 5, 6, 74, 4, 456, 2335, 3546, 45657, 2, 2456, 573, 3567, 8645, 2456]
#these are random tehe 
myFirstListComprehension = [number for number in numbers if number > 2300]
#“Make a list of number for each number in numbers if number > 2300.”
print(myFirstListComprehension)