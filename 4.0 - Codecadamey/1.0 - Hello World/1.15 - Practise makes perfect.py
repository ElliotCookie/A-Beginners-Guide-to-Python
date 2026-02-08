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
""" def remove_duplicates(unrefined_list):
    items_seen_sofar = []
    print(unrefined_list[0])
    items_seen_sofar.append(unrefined_list[0])

    for uritem in range(1, len(unrefined_list)):
        if uritem != in(items_seen_sofar):


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [n for n in numbers if n > 0]
print(newlist) 


    for uritem in range(1, len(unrefined_list)):
        for ritem in refined_list:
            if unrefined_list[uritem] != ritem:
                
    return refined_list

print(remove_duplicates([1, 1, 2, 2])) """

#Starting over
#I'm convinced the best thing you can do is pseudo code it


def remove_duplicates(unrefined_list):
    # Incoming list = unrefined list
    # items seen before = list
    # Something for the output?

    # look at item one of the unrefined list
    # have we seen it before? 
    # take that variable and then loop through our list of stuff seen before
    # did we see it there?
    # if we didn't, then we should add it, so now it has been seen before

    #move to 2nd item of list, and then 3rd etc
    # each time, check the single element against the list of 
    return True

print(remove_duplicates([1, 3, 1, 2, 6, 4, 2, 1, 4, 3, 5])) 

# now flesh it out with code to replace the pseudo

def remove_duplicates(unrefined_list):
    seen_items = []
    
    seen_items.append(unrefined_list[0])
    for uritem in unrefined_list:
        uritem_in_question = uritem
        print("New loop, new ur iq:")
        print(uritem_in_question)
        flag = False
        for si in seen_items:
            sitem_iq = si
            print("Another one, new si iq:")
            print(sitem_iq)

            if uritem_in_question == sitem_iq:
                flag = True

        if flag == False:
            seen_items.append(uritem_in_question)        
            

    # look at item one of the unrefined list
    # have we seen it before? 
    # take that variable and then loop through our list of stuff seen before
    # did we see it there?
    # if we didn't, then we should add it, so now it has been seen before

    #move to 2nd item of list, and then 3rd etc
    # each time, check the single element against the list of 
    return seen_items

#print(remove_duplicates([1, 3, 1, 2, 6, 4, 2, 1, 4, 3, 5])) 

#nailed it, now lets refine


def remove_duplicates(unrefined_list):
    seen_items = []
    seen_items.append(unrefined_list[0])
    for uritem in unrefined_list:
        flag = False
        for si in seen_items:
            if uritem == si:
                flag = True
        if flag == False:
            seen_items.append(uritem)        
    return seen_items

print(remove_duplicates([1, 3, 1, 2, 6, 4, 2, 1, 4, 3, 5])) 

# really good now, cheating a bit

def advanced_rem_dup(xs):
    out = []
    for x in xs:
        if x not in out:
            out.append(x)
    return out

print(advanced_rem_dup(["cat", "dog", "mouse", "cat", "bird", "dog", "hawk"]))

#15/15 - median
# write a function that takes an input and returns the median value (this is the middle number btw)
# The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
# If the list contains an even number of elements, your function should return the average of the middle two.

def mergesort(list):
    #triggers when things are already sorted, e.g [8]
    if len(list) <= 1:
        return list # *** where value is returned
    
    middle = len(list) // 2 # // is integer floor, rounds down to nearest whole no
    left_half = list[0 : middle]
    right_half = list[middle : ]

    #adding in sorted lists
    #I think we are saying there is almost a phantom break here, that this will eventially produce a list length of 1 item each, and it's these two we feed into merge?
    sorted_left = mergesort(left_half) #gets the value from return line ***
    sorted_right = mergesort(right_half)
    
    #Needs updating to sorted left and sorted right
    return merge (sorted_left, sorted_right)
def merge (left_half, right_half): #takes two sorted lists and produces a combined list, keeping the order
    i = j = 0
    merged = []
    #while LH and RH have stuff in, this is a signal to do stuff
    while i < len(left_half) and j < len(right_half): #changed, catches empty case
        #Looping through a little more manually now
        if left_half[i] < right_half[j]:
            merged.append(left_half[i]) #this is at the back and needs to be at the front!
            i += 1
        else:
        #EITHER WAY, MOVE THE SMALLEST ONE OUT
            merged.append(right_half[j])
            j += 1
        #this will slowly remove things from LH RH
        #does this lock in the length when it's initialised? I need to index only the 0 location at one point
    #At this point, one half is empty (= 0)
    merged.extend(left_half[i:]) #extend is like append but for many things (one by one)
    merged.extend(right_half[j:])    
    return merged 

def median(input_list):
    #lets use our nice code from a previous merge sort, kinda lazy though so will do it proper in a sec
    sorted_list = mergesort(input_list)
    """ 
    walk through the steps mentally
    we now have a sorted list of length(x)
    we need to find the most middle
    so if we half the length (lets say 8 or 9)
    if it's 4 (so no reminder when divided by 2) then there is no middle!
        we need to average position 3 and 5, so index 2 and 4
    if the remainder when divided by 2 is 1 then it's odd and easy
        index of len(list)/2 + 1 is the middle
        return that


    big brain idea, but can a sort be done as we find the median
    something like a comparison, and if it is bigger than or smaller than,
    something gets bumped and a new number becomes the focus and the middle    
       """
    
    if len(sorted_list) % 2 == 1:
        #odd
        position = int((len(sorted_list)/2) + 1)
        return sorted_list[position]
    else:
        #even
        upper_position = int(len(sorted_list)/2)
        lower_position = upper_position - 2
        upper_num, lower_num = sorted_list[upper_position], sorted_list[lower_position]
        av_num = (upper_num + lower_num) / 2
        return av_num

    

print("Median list sort, odd:")
print(median([1, 3, 1, 2, 6, 4, 2, 1, 4, 3, 5])) 
print("Median list sort, even:")
print(median([1, 3, 1, 2, 6, 4, 2, 1, 4, 5])) 
print("Median on a len 4 list:")
print(median([7, 8, 9 ,10])) #8.0, so clearly something wrong
    
""" 
Apparently we were right with the big brain idea that we don't need a whole sort
also // can be used to return a int, rather than / for a float

we go again...

    # not trying to sort the whole list remember
    # we need to find a number in the list that has an equal amount greater and smaller
    # a dictionary feels like a good idea? 
    # the hard bit is at the end, we have another list of sorts of 'amount bigger' and 'amount smaller'
    # forgetting what if they are all equal, eg [1 3 3 3]
    # first lets use some design cases of [1 2 3 4 5] (3) and [6 7 8 9] (7.5)
    # so 3 would have AB and AS as equal, therefore the answer
    # 7 would have 2 AB and 1 AS, 8 1 AB and 2 AS, not seemingly useful
    # 6 would have 3AB, 7 2AB, 8 1AB, 9 0AB, and we need to be at 1.5AB
    # don't forget these are all usefully ordered
    # could work through, find the highest and lowest each time and drop it
    # eventually we'd have either 1 item left or 2 (but dropping would go to 0, so that's our answer)


 """


def median(input_list):
    amount_bigger = []
    count = 0
    for item in input_list:
        checking_item = item
        for item2 in input_list:
            if checking_item < item2:
                count += 1
        amount_bigger.append(count)

    bigger_count = 0
    lower_count = len(amount_bigger)
    index_bigger = 0
    index_lower = 0
    

    if len(amount_bigger) >= 3:
        for item in amount_bigger:
            loop_count = 0
            if item > bigger_count:
                bigger_count = item
                index_bigger = loop_count
            if lower_count < item:
                lower_count = item
                index_lower = loop_count
        amount_bigger.pop(index_bigger)
        amount_bigger.pop(index_lower)
        
    #check if it is 3, 2 or 1 and act accordingly
    result = 0 # temp variable
    #this already feels too long to be correct

    return result


def median(input_list):
    list_length = len(input_list)
    for checking_item in input_list:
        # if n//2 values are bigger then it is the median (odd)
        # if n//2 and n//2 straddle (even)
        counter = 0
       
        for other_item in input_list:
            if checking_item > other_item:
                counter += 1

        if list_length // 2 == counter and checking_item == input_list[list_length-1]:
            #it's the odd case, therefore:
            return checking_item
        else:
            if list_length // 2 - 1 == counter:
                lower_med = checking_item
            if list_length // 2 == counter:
                upper_med = checking_item

    #even case happened...
    return (lower_med + upper_med)/2


print("3rd median attempt:")        
print(median([3, 4, 7, 6, 5]))     
print(median([31, 42, 78, 69, 57]))     
print(median([57, 31, 42, 78, 69]))  
print(median([4, 7, 6, 5])) 
print(median([40, 72, 63, 51])) 
print(median([51, 40, 72, 63])) 


def median(input_list):
    lower_half= []
    upper_half = []

    for item in input_list:
        if lower_half[0] == "":
            lower_half.append(item)
        else:
            if item > max(lower_half):
                upper_half.append(item)
            


""" 


        # STEP 2: rebalance the heaps
        #
        # Invariant we must maintain:
        #
        #   size(LOWER) == size(UPPER)
        #       OR
        #   size(LOWER) == size(UPPER) + 1
        #
        # LOWER is allowed to have ONE extra element
        # but UPPER is never allowed to be bigger.

        if size(LOWER) > size(UPPER) + 1:
            # LOWER is too big
            # move its largest element across the boundary
            move max(LOWER) into UPPER

        else if size(UPPER) > size(LOWER):
            # UPPER is too big
            # move its smallest element across the boundary
            move min(UPPER) into LOWER


        # At this point:
        #   - all values in LOWER <= all values in UPPER
        #   - heaps are balanced


    # STEP 3: compute the median from the heaps
    #
    # If both heaps are the same size:
    #   median is the average of the two boundary values
    #
    # If LOWER has one extra value:
    #   median is simply its maximum

    if size(LOWER) == size(UPPER):
        return ( max(LOWER) + min(UPPER) ) / 2

    else:
        return max(LOWER)

 """
