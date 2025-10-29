print("Pig Latin")
pyg = "ay"
original = input("Enter a word: ")

if len(original) > 0:
    print(f"Valid string: {original}")
else:
    print("empty")


if len(original) > 0 and original.isalpha() == True: #don't forget ()
    word = original.lower()
    print("Valid string: %s" % (word))
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
else:
    print("empty or non-alpha")


