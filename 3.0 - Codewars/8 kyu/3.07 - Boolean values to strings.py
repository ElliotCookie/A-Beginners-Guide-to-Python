#Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

""" def bool_to_word(boolean):
    # TODO """

"""     test.assert_equals(bool_to_word(True), 'Yes')
        test.assert_equals(bool_to_word(False), 'No')
 """

def bool_to_word(boolean):
    if boolean: return "Yes"
    else: return "No"
    
#the cool way is: return "Yes" if bool else "No"    

print(bool_to_word(True))
print(bool_to_word(False))