#Write a program that finds the summation of every number from 1 to num (both inclusive).
# The number will always be a positive integer greater than 0. 
# Your function only needs to return the result, what is shown between parentheses in
#  the example below is how you reach that result and it's not part of it, see the sample tests.

""" def summation(num):
    pass # Code here
    
 """

"""     test.assert_equals(summation(1), 1)
        test.assert_equals(summation(8), 36)
        test.assert_equals(summation(22), 253)
        test.assert_equals(summation(100), 5050)
        test.assert_equals(summation(213), 22791) """


def summation(num):
    newNum = 0
    for x in range(num+1):
        newNum += x
    return newNum
    

print(summation(100))
print(summation(213))
print(summation(1))
print(summation(0))

#the nice solutions:


""" 
return sum(range(1,num+1))
return (1+num) * num / 2

"""