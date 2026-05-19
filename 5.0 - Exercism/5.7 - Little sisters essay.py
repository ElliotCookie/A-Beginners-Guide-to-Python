"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """

    counter = 0
    for counter in range(0, len(title)):
        char_in_question = title[counter]
        if (counter == 0) or (title[counter - 1] == " " and char_in_question != " "):
            char_in_question = char_in_question.upper()
            title = title[:counter] + char_in_question + title[counter+1:] # could use a list and not rebuild strings
 
    return title


print(capitalize_title("green giant"))
print(capitalize_title("new Test"))
print(capitalize_title("three words now"))
print(capitalize_title("ending in a space "))
print(capitalize_title(" starting with a space"))
print(capitalize_title("number test 1five"))

"""             for chars in range(0, len(title)-1):
                scan = title[chars]
                if scan != " ":
                    first_letter = title[chars]   
                    first_letter = first_letter.upper()
                    title = title[:chars] + first_letter + title[chars:] """



"""     for char in range(1, len(title) - 1):
        new_char = title[char]
        if new_char == " ":
            char_in_question = title[char + 1] 
            char_in_question = char_in_question.upper()
            title = title[:char] + char_in_question + title[char:]
            new_title = title
    return title """


"""     counter = 0
    while counter < len(title):
        first_letter = title[counter]    
        if first_letter != " ":  
            first_letter = first_letter.upper()
            title = first_letter + title[1:]
            counter += len(title)
        elif first_letter == " ":
            blank_spaces = 0  
            while title[blank_spaces] == " ":
                blank_spaces += 1 
            first_letter = title[blank_spaces]
            first_letter = first_letter.upper()
            title = title[:blank_spaces] + first_letter + title[blank_spaces+1:]
            counter += len(title)

        counter += 1 """
    


# progress, in a form
# late to work though!


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    if sentence[len(sentence)-1] == ".": return True
    else: return False

    
print(check_sentence_ending("I am a frog"))
print(check_sentence_ending("Frogs are friends."))

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    while len(sentence) > 0 and sentence[0] == " ":
        print("FRONT space removed")
        sentence = sentence[1:]

    while len(sentence) > 0 and sentence[-1] == " ":
        print("REAR space deleted")
        sentence = sentence[:-1]

    return sentence


print(clean_up_spacing("no spaces here"))
print(clean_up_spacing(" one space here "))
print(clean_up_spacing("   three and four here space here    "))


"""
AS WE ARE MUTATING THE LENGTH OF THE ITERABLE, A WHILE LOOP IS MORE FAVOURABLE 
    for char in range(0, len(sentence)):
        char_in_question = sentence[char]
        if char_in_question == " ": # armed, found blank space at START
            sentence = sentence[char+1:] # move the start of the sentance one digit over
            print("FRONT SPACE REMOVED")
        if char_in_question != " ": # found our first char, so exit
            break
    
    # lets go backwards
    for char in range(len(sentence) -1 , -1, -1):   
        char_in_question = sentence[char]
        if char_in_question == " ": # armed, found blank space at END
            sentence = sentence[:char] # move end of sentance inwards
            print("END SPACE REMOVED")
        if char_in_question != " ": # found our last char, so exit
            break """



def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    pass
