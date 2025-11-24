names = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in names:
    print(name)


#For loops to print dict keys
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for key in webster:
    print(webster[key])


#printing even numbers from a list
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0: #therefore even
        print(number)


#function for fizz
def fizz_count(x):
    count = 0
    for item in x: #a reminder that we can also iterate through strings
        if item == "fizz": #but these happen line by line
            count += 1
    return count



#making our supermarket dictionary
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3 }

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15 }