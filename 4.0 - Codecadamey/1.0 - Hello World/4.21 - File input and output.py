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