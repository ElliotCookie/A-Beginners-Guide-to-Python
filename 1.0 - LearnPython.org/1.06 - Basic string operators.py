#Strings are bits of text, which we already know
#If you define one with '' then when you come to use '' in a string it can be an issue
#(that's pretty obvious and not new ground)
print("single quotes are ' '")

#Code given in the lesson is
astring = "Hello world!"
print(len(astring))
#That prints out 12, because "Hello world!" 
# is 12 characters long, including punctuation and spaces.
#the len function is new here, obvious what that does
#Interestingly though it doesn't start at 0

print(astring.index("o"))
#This will say 4, because we start counting at 0 (ofc)
# .index will find the first instance of a specified value

print(astring.count("l"))
#This will print out 3, for the number of l's in the string

print(astring[3]) #this will print the value at index 3
print(astring[:7])
print(astring[3:7])
#this prints 'lo w', starting index of 3 (from 0)

print(astring[3:7:2])
#The syntax for this is [start:stop:step]

print(astring[::-1])
#This prints start:end but goes in -1 steps
#The effect is to reverse the string! (Not doable otherwise)

print(astring.upper())
print(astring.lower())
#Transforms into upper and lower cases, pretty easy

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
#These will print TRUE and FALSE, again, obvious reasoning

afewwords = astring.split(" ") #turns it into a list!
print(afewwords)


""" EXERCISE """
#starting at 01234567890123456789
s = "Str3456 a9a1234 ome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))