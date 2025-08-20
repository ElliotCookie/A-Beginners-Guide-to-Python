#Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. Leave punctuation marks untouched.

""" pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway ! """

""" def pig_it(text):
    #your code here """

    #we are going to get an input string
    #need to go through this char by char (don't forget to ignore punctuation)
    #when we get to a space we know that is a new word
    #could log that location and come back afterwards?
    #well, it's a given that the previous char AFTER we find a space needs to be put at the front
    #and likewise the front needs to come back there, don't forget we can swap variables using a, b = b, a
    #there is the option to create an array of new words we create and assemble at the end?

def pig_it(text):   
    if text.count(" ") > 0: # This means we have multiple clauses
        array_of_incoming_words = text.split()
        array_of_new_words = []
        for words in array_of_incoming_words:
            if words.isalpha() == True: #checks if alphabet or not
                array_of_new_words.append(swap_it_add_ay(words))
            else: array_of_new_words.append(words)
        final_string = ""
        for quant in range(0, len(array_of_new_words)):
            final_string += array_of_new_words[quant] + " "           
        return final_string[0:len(final_string)-1]

    else: # We have a single word, so can just swap and add 'ay' 
        return swap_it_add_ay(text) 
    
def swap_it_add_ay(word):
    new_string_to_be_made = word[1:(len(word))] + word[0] + "ay"
    return new_string_to_be_made

print(pig_it('Singleword'))
print(pig_it('Two words'))
print(pig_it('Pig latin is cool'))
print(pig_it('Word !^* and punctuation %^'))