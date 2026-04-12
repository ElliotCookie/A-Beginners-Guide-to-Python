# 1 / 9 - Writing and exporting
# I get the impression that a lot of this will be different as it is py 2
# no reason to base that off of, just a hunch

my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

# so that has been stored in this folder, which is useful (so I don't lose it)





# 2 / 9 - The open function
# basically the process of identifying a file and setting it up to be interacted with

my_file = open("output.txt", "r+") # the second argument allows you to do different things ofc





# 3 / 9 - Writing
# the write() function takes a string argument
# you also need to remember to close the file, or "python won't write to it properly"

# Instructions aren't that clear on this one, considering it is a new lesson

for item in my_list:
  my_file.write(str(item)+ "\n") # kinda cheating as they already gave us this
my_file.close()  






# 4 / 9 - Reading
# I have a feeling this might be similar to writing, although we won't need to offer up a str() ofc

my_new_file = open("output.txt", "r")
print(my_new_file.read()) # the .read() goes outside the object, not read(object)
# DON'T FORGET TO CLOSE
my_new_file.close()



# 5 / 9 - Reading between the lines
# Feel like we are in for a surprise here!
# Oh wait, it's just a readline thing

my_file3 = open("output.txt", "r") #this asked for "text.txt" but we haven't done that in the lesson yet
print(my_file3.readline()) #it actually adds a space after each line
print(my_file3.readline())
print(my_file3.readline())
my_file3.close()

# trying something extra
print("extra stuff")
my_file4 = open("output.txt", "r")
test_list = my_file4.read()
#for item in test_list[0,3]:
#  print(item)
my_file4.close()

# I've got an error but I think I need to close it properly

# okay, we've stored the var so lets close it immediately
# also, lets store it in a list rather than a str

my_file5 = open("output.txt", "r")
test_list = [my_file5.read()]
my_file5.close()

""" for item in test_list[0,3]:
  print(item) """

# more errors, lets print the whole list and see what happens

print(test_list) #['1\n4\n9\n16\n25\n36\n49\n64\n81\n100\n']

# we need a function that basically looks at a list but filters out certain selected chars
# the other issue is that this is a list of len 0, basically a str

my_file5 = open("output.txt", "r")
test_list = [my_file5.read()]
my_file5.close()

for item in test_list[0:3]: #this was the syntax error, : not ,
  print(item) # this prints everything, because it's a list of len 0


# updates

my_file6 = open("output.txt", "r")
test_str = my_file6.read() # removed [] because irrelevant
my_file6.close()

test_list = test_str.split("\n") # this was the missing function
print(test_list) # ['1', '4', '9', '16', '25', '36', '49', '64', '81', '100', '']
for item in test_list[0:3]:
  print(item) 

print("Think we are finally there....")
my_file7 = open("output.txt", "r")
test_str = my_file7.read() # removed [] because irrelevant
my_file7.close()

test_list = test_str.strip().split("\n") # added in .strip() to remove ''
print(test_list) # ['1', '4', '9', '16', '25', '36', '49', '64', '81', '100']
for item in test_list[0:3]:
  # change the seperator example
  print(item, end=" ")
print()
print("Change seperator finished")

# print all at once
print(*test_list[0:3])
print("Print all at once finished")

# join into a string, controlled
print(" ".join(test_list[0:3])) # bracket placement here very important
print("Join into a string finished")


# I think we need to unpack how all of these work tbh, readline is cool though!





# 6 / 9 - Buffering data
# If you write to a file without closing it, the data never gets there!



# Use a file handler to open a file for writing
write_file = open("text.txt", "w")

# Open the file for reading
read_file = open("text.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

write_file.close()

# Try to read from the file
print (read_file.read())
read_file.close()




# 7 / 9 - with and as keywords
# there is an exit method that automatically closes our files
# to get there, we use the keywords
print("new keywords...")
with open("text.txt", "w") as textfile:
  textfile.write("Success!")


# 8 / 9 - trying it ourselves

string_to_write = str(input("put in the string please: "))
print(string_to_write)
with open("text.txt", "w") as file_to_write:
  file_to_write.write(string_to_write)

# obviously it didn't like this answer
