#Complete the square sum function so that it squares each number passed into it and then sums the results together.

""" def square_sum(numbers):
    #your code here """

"""     test.assert_equals(square_sum([1,2]), 5)
        test.assert_equals(square_sum([0, 3, 4, 5]), 50)
        test.assert_equals(square_sum([]), 0)
        test.assert_equals(square_sum([-1,-2]), 5)
        test.assert_equals(square_sum([-1,0,1]), 2) """



def square_sum(numbers):
    return sum(x * x for x in numbers)


print(square_sum([0, 3, 4, 5]))
print(square_sum([-1,-2]))