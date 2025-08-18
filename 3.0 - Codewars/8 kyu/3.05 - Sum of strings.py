#Complete the solution so that it reverses the string passed into it.

""" def solution(string):
    pass """

""" test.assert_equals(solution('world'), 'dlrow')
        test.assert_equals(solution('hello'), 'olleh')
        test.assert_equals(solution(''), '')
        test.assert_equals(solution('h'), 'h')
 """

def solution(string):
    string = string[::-1]
    return string


print(solution("hello"))
print(solution("world"))

#Good solution!!!
# return str[::-1]