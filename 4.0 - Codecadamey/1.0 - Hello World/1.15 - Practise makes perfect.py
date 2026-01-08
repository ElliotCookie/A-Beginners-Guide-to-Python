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

#5/15 - Factorials
def factorial(x):
    total = 1
    for digits in range(1,x+1):
        total = total * digits
    return total

print(factorial(4))
print(factorial(1))
print(factorial(9))

#6/15 - is it prime?
def is_prime(x):
    if x < 2:
        return False # anything under 2 isn't prime
    else: 
        for factors in range(2, x-1):
            if x % factors == 0:
                # if the remainder is 0, it divided perfectly
                return False 
        return True
        

print(is_prime(9))
print(is_prime(17))
print(is_prime(57))

#7/15 - 