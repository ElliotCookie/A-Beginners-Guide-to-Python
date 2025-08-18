#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

""" def move_zeros(lst):
    return lst """

"""     test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) """


def move_zeros(lst):
    #read list
    #maybe make a note of the length
    #check if it's 0 or not
    #if it is then lets pop it another list, and remove it
    #if it isn't then just go to next
    #after we have looked at everything, lets throw our array of 0s on the end of the existing

    arrayOfZeros = []
    arrayofElse = []
    for x in lst:
        if x == 0:
            arrayOfZeros.append(x)
        else:
            arrayofElse.append(x)
    lst = arrayofElse + arrayOfZeros        
    return lst

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
