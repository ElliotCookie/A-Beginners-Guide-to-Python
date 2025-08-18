#We need a function that can transform a number (integer) into a string.

#What ways of achieving this do you know?

""" def number_to_string(num):
    pass # Return a string of the number here! """
    
"""     test.assert_equals(number_to_string(67), '67')
        test.assert_equals(number_to_string(79585), '79585')
        test.assert_equals(number_to_string(-79585), '-79585')
        test.assert_equals(number_to_string(1+2), '3')
        test.assert_equals(number_to_string(1-2), '-1')
        test.assert_equals(number_to_string(0), '0') """


def number_to_string(num):
    string = ""
    string = str(num)
    return string
#   return str(num)

print(number_to_string(5))
print(number_to_string(3+1))





