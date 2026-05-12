"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """


    for char in range(0, len(title) - 1):
        new_char = title[char]
        if new_char == " ":
            char_in_question = title[char + 1] 
            char_in_question = char_in_question.upper()
            title = title[:char] + char_in_question + title[char:]
            new_title = title
    return title

print(capitalize_title("green giant"))
print(capitalize_title("new Test"))
print(capitalize_title("three words now"))
print(capitalize_title("ending in a space "))
print(capitalize_title(" starting with a space"))
print(capitalize_title("number test 1five"))

# progress, in a form
# late to work though!


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """

    pass


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """

    pass


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """

    pass
