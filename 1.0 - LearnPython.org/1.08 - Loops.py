#In Python, there are two types of loops
#The crowd favourite, for. And the other one, while.

#For loops
#These iterate over a sequency of numbers using one of two functions
#RANGE - which returns a new list with numbers of the specified range
#XRANGE - which returns an iterator, was more efficent in Py 2 but doesn't matter now in Python 3
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)
# Prints out 3,4,5
for x in range(3, 6):
    print(x)
# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)


#WHILE LOOPS
#Will repeat indefinately until a boolean condition is met
# Prints out 0,1,2,3,4
print("Basic while loop")
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

#However, there are a couple of things that can be done to a while loop
#these allow for action or early termination (continue or break)
print("")
for x in range (10):
    if x % 2 == 0:
        print ("Okay, now x % 2 == 0")
        continue
    print (x)

count = 0
while True: #This means literally run this block forever, you NEED break
    print(count)
    count += 1
    if count >= 5:
        print ("break line triggered")
        break


print("ELSE CLAUSE IN LOOPS - both for, then while")
for i in range (10,13): #change that second number to 12 or above to change triggers
    if i%12 == 0:
        break #when i = 12 this should trigger, which will jump past the else clause
    print(i)
else:
    print("printing in the else clause")

while count < 30:
    print (f"count is {count}, adding 5 more!")
    count += 5
else:
    print(f"count limit of {count}, set out in while function, reached")


""" Exercise
Loop through and print out all even numbers from the numbers list in the
same order they are received. Don't print any numbers  that come after 237
in the sequence. """

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
for number in numbers: #first loop number = 951, 2nd 402, etc
    if number % 2 == 0: #this means it's even
        print(number)
    if number == 237: #use a ==, not 1 = as that's trying to assign
        break #breaks the loop at the highest level (so the for loop)


    