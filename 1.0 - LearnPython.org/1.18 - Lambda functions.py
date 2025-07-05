#A lambda function is good when you need to pass a basic function as an
#argument. That being said, it needs to be super basic and fit on one line
#and only ever be called once. The benefits are you can go from:

x = int(input())

def squaring(x):
    square = x * x
    return square 
print(squaring(x))

#To this:

lambdasquaring = lambda x : x * x
print(lambdasquaring(x))

#and then even shorter!
print(lambda x : x * x)

#it seems like it's best for sorting things as you parse them, e.g
nums = [132456, 64343, 245456, 75644, 23456, 54332, 4645, 3]
sorted_nums = sorted(nums, key = lambda x : -x)
print(sorted_nums) #prints in decending order
#other great functions to use are map, filter and reduce

""" Exercise
Write a program using lambda functions to check if a number
in the given list is odd. Print "True" if the number is odd or
"False" if not for each element.
 """

l = [2,4,7,3,14,19]
for i in l:
    # your code here
    lambdadivtwo = lambda i : i % 2
    if lambdadivtwo(i) == 0:
        print("False")
    else:
        print("True")


#A better version is
    if (lambda x: x % 2)(i) == 0:
        print("False")
    else:
        print("True")


#Or even shorter:
    print("False" if (lambda x: x % 2)(i) == 0 else "True")
