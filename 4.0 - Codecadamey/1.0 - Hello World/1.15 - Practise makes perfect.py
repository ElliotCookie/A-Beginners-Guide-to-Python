def is_even(x):
    if x % 2 == 0: #took far too long to remember this lol
        return True
    else:
        return False
print(is_even(30))

#is int (no value in the decimals)
def is_int(x):
    floored_no = x // 1
    if x - floored_no == 0:
        return True
    else:
        return False

print(is_int(7.0))   # True    
print(is_int(7.5))   # False    
print(is_int(-1))    # True     

#digit sum
def digit_sum(n):
    # str_of_n = str(n)
    # length_of_n = len(str_of_n)
    # sum = 0
    # for digits in length_of_n:
    #     current_digit = str_of_n[digits]
    #     if type(current_digit) == int:
    #         sum += int(current_digit)   
    # return sum
    total = 0
    for chars in str(n):
        if chars.isdigit(): #this was the key we were missing
            total += int(chars)
    return total

print(digit_sum(10))   
print(digit_sum(1234))
print(digit_sum(-194))

