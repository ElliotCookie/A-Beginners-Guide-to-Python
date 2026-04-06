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