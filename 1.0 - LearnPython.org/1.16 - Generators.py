#These are simple functions that are use to create iterators
#They ave a special way of returning a set of items, one at a time
#From what I gather, it's a way of running a for loop to get one output
#Rather than running it adinfinitum to get a whole batch of cookies, you can run it once
#just get the 1 cookie you need, and then come back to it later when you need another


def cookie_baker():
    for i in range(2):
        print(f"we are making cookie number {i}")
        yield f"cookie {i}"
    
    yield f"We've done making cookies and are now making bread"
#the yield statements are the thing that tells it how many times it can run
for item in cookie_baker():
    print(item)

""" 
Exercise
Write a generator function which returns the Fibonacci series.
They are calculated using the following formula:
The first two numbers of the series is always equal to 1,
and each consecutive number returned is the sum of the last two numbers.
Hint: Can you use only two variables in the generator function?
Remember that assignments can be done simultaneously. The code
a = 1
b = 2
a, b = b, a
print(a, b)
will simultaneously switch the values of a and b. """

# fill in this function
def fib():
    a = 1
    yield a
    b = 2
    yield b
    while True: #counter function below stops us, need something to loop lots so
        #that we can return a lot of 'yields'
        a, b = b, a + b 
        yield b


# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break