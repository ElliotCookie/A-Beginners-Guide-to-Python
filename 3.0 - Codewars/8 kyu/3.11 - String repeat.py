#Write a function that accepts a non-negative integer n and a string s as parameters,
# and returns a string of s repeated exactly n times.

""" def repeat_str(repeat, string):
    return '' """

"""     test.assert_equals(repeat_str(4, 'a'), 'aaaa')
        test.assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
        test.assert_equals(repeat_str(2, 'abc'), 'abcabc')
        test.assert_equals(repeat_str(0, ''), '')
        test.assert_equals(repeat_str(0, 'I'), '')
        test.assert_equals(repeat_str(5, ''), '')
        test.assert_equals(repeat_str(6, 'I'), 'IIIIII')
        test.assert_equals(repeat_str(5, 'Hello'), 'HelloHelloHelloHelloHello') """


def repeat_str(repeat, string):
    repeatedString = ""
    while repeat > 0:
        repeatedString = repeatedString + string 
        repeat = repeat - 1
        print(repeatedString)
    return repeatedString 

#see, what you didn't learn was:       return repeat * string
# didn't remember***, lesson 1.04: lotsofhellos = hello * 10
#print(lotsofhellos)



print(repeat_str(4, 'a'))
print(repeat_str(5, 'Hello'))