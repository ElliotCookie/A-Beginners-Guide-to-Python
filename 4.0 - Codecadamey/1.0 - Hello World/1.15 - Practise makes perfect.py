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

#7/15 - reversing strings

def reverse(text):
    length = len(text)
    new_string = ""
    position = 0
    test_char = text[length -1 ]
    new_string += test_char
    for chars in range(2, length + 1):
        position = length - chars
        test_char = text[position]
        new_string += test_char
    return new_string
#I know this is bad but I'm including it to show it's okay to learn

print(reverse("help"))


#8 / 15 - anti vowels
def anti_vowel(text):
    vowelless = ""
    for chars in text:
        if chars == "a" or chars == "e" or chars == "i" or chars == "o" or chars == "u":
            #don't forget to define each 'or'
            continue
        else:
            vowelless += chars
    return vowelless

print(anti_vowel("a long string with lots of vowels"))

 
#trying refining 
def anti_vowel(text):
    vowelless = ""
    vowels = "aeiouAEIOU" #you want a string here, not a list
    for chars in text:
        if chars in vowels:
            continue
        vowelless += chars
    return vowelless

print(anti_vowel("a different string we are using for refining"))

#9 / 15 - Scrabble score
def scrabble_score(word):
    word == word.lower()
    sc_score = 0
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    for char in word:
        for letter in score:
            if char == letter:
                sc_score += score[char]
    return sc_score

print(scrabble_score("DuNe"))