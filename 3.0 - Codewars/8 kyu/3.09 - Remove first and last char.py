#Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.
# Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.

""" def remove_char(s):
    #your code here """

"""     test.assert_equals(remove_char('eloquent'), 'loquen')
        test.assert_equals(remove_char('country'), 'ountr')
        test.assert_equals(remove_char('person'), 'erso')
        test.assert_equals(remove_char('place'), 'lac')
        test.assert_equals(remove_char('ok'), '')
        test.assert_equals(remove_char('ooopsss'), 'oopss') """


def remove_char(s):
    return(s[1:len(s) - 1:])
    #return s[1 : -1]     REALLY NICE!

print(remove_char("place"))
print(remove_char("country"))