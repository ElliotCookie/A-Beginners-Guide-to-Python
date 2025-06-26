#Python uses C-style formatting, which I'm assuming means 'C' the language

#you can use % with an argument specifier to print it, in the same line, eg
name = "John"
print("Hello, %s" % name)
#but we have been over that f strings are more elite 
print(f"Hello, {name}")
#look how much shorter it is!!

#The "%" operator is used to format a set of variables enclosed in a "tuple" 
#(a fixed size list), together with a format string
#A tuple is a way to group items together in a fixed order


#You can use multiple argument specifiers, unsure 
age = 23
print("%s is %d years old." % (name, age)) #%d is integer, not %i for some reason
#it's still good to appreciate this as it will allow you to review legacy code

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)



""" You will need to write a format string which prints out the data using
 the following syntax: Hello John Doe. Your current balance is $53.44. """

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f."
#the 2f gives a float to 2dp, could use %s only though
print(format_string % data)

#I'm thinking that we need to extract the last item out of the data
#John and Doe can be next to each other as they are called that way


