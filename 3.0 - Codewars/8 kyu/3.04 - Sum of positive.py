#You get an array of numbers, return the sum of all of the positives ones.

""" def positive_sum(arr):
    # Your code here
    return 0
 """

""" @test.describe("positive_sum")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(positive_sum([1,2,3,4,5]),15)
        test.assert_equals(positive_sum([1,-2,3,4,5]),13)
        test.assert_equals(positive_sum([-1,2,3,4,-5]),9)
        
    @test.it("returns 0 when array is empty")
    def empty_case():
        test.assert_equals(positive_sum([]),0)      
        
    @test.it("returns 0 when all elements are negative")
    def negative_case():
        test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0) """

""" abs(x)
Return the absolute value of a number.
The argument may be an integer, a floating-point number, or an object implementing __abs__(). 
If the argument is a complex number, its magnitude is returned. """

def positive_sum(arr):
    sum = 0
    for num in arr:
        if -abs(num) != num: sum += num
    return sum

    """ 
    Other very good solutions
    sum = 0
    for e in arr:
        if e > 0:
            sum = sum + e
    return sum

    return sum(x for x in arr if x > 0) """

#little test function:
print(positive_sum([1,-2,-3,-4, 5]))

