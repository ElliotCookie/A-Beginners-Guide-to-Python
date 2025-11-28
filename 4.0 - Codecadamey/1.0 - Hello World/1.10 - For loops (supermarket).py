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

for key in prices:
    print(f"{key}: {prices[key]}")
    print("%s: %s" % (key, prices[key])) #don't need brackets on the s, string needs to be a tuple
    #this is an unfinished exercise, we want
    """
     apple
    price: 2
    stock: 0
    """
    print("ACTUAL ANSWER:")
    print()

for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])
    print
#after all that, codecademy told me I was wrong, because I was on a different line
#but the solution moved the lines! It didn't even use their original code


#working out the value
total = 0
for price in prices:
    price_to_print = prices[price] * stock[price]
    print(price_to_print)
    total += price_to_print
print(total)

#shopping at the market
groceries = ["banana","orange", "apple"]

def compute_bill(food):
    total = 0
    for items in food:
        total += prices[items]
    print(total)
    return total

compute_bill(groceries)

#changing that function to only count in-stock
print("stock > 0")
print
def compute_bill(food):
    total = 0
    for items in food:
        if stock[items] > 0:
            total += prices[items]
            stock[items] -= 1
    print(total)
    return total

compute_bill(groceries)

#module complete!

