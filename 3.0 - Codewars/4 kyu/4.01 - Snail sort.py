""" Given an n x n array, return the array elements
arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9] """

""" def snail(snail_map):
    pass """





def snail(snail_map):
    
    # input is an array of arrays, or a nested array
    # output needs to be a single array
    # so we also know it's n x n so always square
    # the first line we therefore don't have to do anything with
    # equally, the last line is also always just reversed
    # needs to be infinitely scalable to n




array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print (snail(array))
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print (snail(array))