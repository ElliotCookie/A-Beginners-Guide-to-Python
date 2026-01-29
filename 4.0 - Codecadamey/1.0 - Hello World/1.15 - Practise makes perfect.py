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
    lower_word = word.lower() # a == is a truth test btw!
    sc_score = 0
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    for char in lower_word:
        for letter in score:
            if char == letter:
                sc_score += score[char]
    return sc_score

print(scrabble_score("DuNe"))
print(scrabble_score("dune"))
print(scrabble_score("random"))
print()

#refining
print("refined scrabble version:")
def scrabble_score(word):
    sc_score = 0
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
    for char in word.lower():
        sc_score += score[char]
    return sc_score

print(scrabble_score("testerWord"))

#10/15 - censor
print("Censor task")
def censor(text, word):
    #return text with chosen word in ****s
    new_text = ""
    for i in range(0, len(text)):
        test_word = text[i:len(word)+1]
        print(test_word)
        if test_word == word:
            new_text += text[0:i] + "*"*len(word)
    return new_text

print(censor("banter", "ant"))

#some tests
test = "wordsmith"
print("Some test words:")
print(test[0:2]) #wo
print(test[0::2]) #wrsih
print(test[::3]) #wdi
print(test[:2:2]) #w

def censor2(text, word):
    #return text with chosen word in ****s

    print("Entering censor function")
    #text = incoming word that we want to censor
    #word = censored word
    new_text = ""
    word_checker = ""
    for char in text:
        print("char is")
        print(char)
        word_checker += char
        print("word checker is")
        print(word_checker)
        if len(word_checker) == len(word):
            if word_checker == word:
                new_text += "*"*len(word)
                print("new text is")
                print(new_text)
                word_checker = ""
            else:
                new_text += word_checker[0:1]
                print("new text is now")
                print(new_text)
                word_checker = word_checker[1:]
                print("word checker is now")
                print(word_checker)
    new_text += word_checker

                        
    """
    go through text char by char
    append each char to a temp string
    when the temp string has the len(word)
    check if temp_string == word
    if it does then add that amount of asterixes to the new_text
    start counting again with an empty temp string
    if it doesn't (e.g ban =/= ant)
    add the first letter to the new_text
    """
    return new_text
print("New attempt at censor")
print(censor2("banterclauseWithants", "ant"))

#lets tidy that up and remove fluff

def censor3(text, word):
    new_text, word_checker = "", ""
    for char in text:
        word_checker += char
        if len(word_checker) == len(word):
            if word_checker == word:
                new_text += "*"*len(word)
                word_checker = ""
            else:
                new_text += word_checker[0:1] #apparently n^2
                word_checker = word_checker[1:]
    return new_text + word_checker
print(censor3("morewordsthataretiedtogethere", "re"))

#the example solution btw
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
  
print(censor("this hack is wack hack", "hack"))


#11/15 - count
print("Count exercise")
def count (sequence, items):
    #check how many times ITEM appears in list[sequence]
    #can't use the list method, have to do it the long way
    #reutrn an int, accept int, str, flt or even a list!
    #don't forget that list is reserved word in python

    rolling_count = 0
    for bits_of_list in sequence:
        if items == bits_of_list:
            rolling_count += 1
    return rolling_count

print(count([1, 2, 3, 4, 1, 4, 'a','A'], 1)) # 2
print(count([1, 2, 3, 4, 1, 4, 'a','A'], 'a')) # 1
print(count([1, 2, 3, 4, 1, 4, 'a','A'], ['a', 'A'])) # 0
print(count([1, 2, 3, 4, 1, 4, ['a', 'A'],'A'], ['a', 'A'])) # 1


# 12 / 15 - purify 
# a function that taks a list of numbers
# removes the odd ones
# returns the purified result
# no modification, return a new list
print("Purify function")

def purify(unpurified):
    purified = []
    for item in unpurified:
        if item % 2 == 0: # not: !=
            purified.append(item)
    return purified

print(purify([1, 2, 3, 4, 1, 4]))
# shorter than the example ;) nice


def product (int_list):
    total = 1 # an easy way to get rid of 0?
    for int in int_list:
        total = total * int
    return total

print(product([4, 5, 6]))


#14 / 15 - removing duplicates
# taking a list and removing any of the elements that are the same 
def remove_duplicates(unrefined_list):
    refined_list = []
    for uritem in unrefined_list:
        for ritem in refined_list:
            if uritem == ritem:
                continue
        refined_list.append(uritem)
    return refined_list

print(remove_duplicates([1, 1, 2, 2]))