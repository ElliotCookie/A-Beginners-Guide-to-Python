# 1 / 14 - Bitwise operators
print (5 >> 4)  # Right Shift       0
print (5 << 1  )# Left Shift        10
print (8 & 5 )  # Bitwise AND       0
print (9 | 4)   # Bitwise OR        13
print (12 ^ 42 )# Bitwise XOR       38
print (~88  )   # Bitwise NOT       -89


# 2 / 14 - The 2 base number system
# This is essentially binary, 0b is the protected keyword that lets you interact this way
print (0b1,)   #1
print (0b10,)  #2
print (0b11,)   #3
print (0b100,)  #4
print (0b101,)  #5
print (0b110,)  #6
print (0b111 )  #7
print ("******")
print (0b1 + 0b11)
print (0b11 * 0b11)


# 3 / 14 - counting in binary
one = 0b1
two = 0b10
three = 0b11
four = 0b100 # - so 1 x 4, 0 x 2, 0 x 2
five = 0b101 # rejected my answer for having that comment explaining
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010 
eleven = 0b1011 # = 8x1 + 4x0 + 2x1 + 1x1 
twelve = 0b1100


# 4 / 14 - The bin function, to make it easy
print(bin(1)) # 0b1

for nos in range(2,6):
    print(bin(nos))




# 5 / 14 - There is a second parameter on the int function!
#When given a string containing a number and the base that number is in, the function will return
# the value of that number converted to base ten.
print("Second parameter of int...")
print (int("1",2))
print (int("10",2))
print (int("111",2))
print (int("0b100",2))
print (int(bin(5),2))
print(int("11001001", 2))






# 6 / 14 - Shifting bits left and right
print("shifting bits...")
""" Shift operations are similar to rounding down after dividing
and multiplying by 2 (respectively) for every time you shift, 
but it’s often easier just to think of it as shifting all the 1s and 0s
left or right by the specified number of slots. """

# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 #(1 << 2 = 4)
0b000101 << 3 == 0b101000 #(5 << 3 = 40)       

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 #(20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 #(2 >> 2 = 0) 


shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right >> 2 == 0b11 #this would be a boolean, not the operation
shift_left << 2 == 0b100


shift_right = 0b1100
shift_left = 0b1
shift_right = shift_right >> 2
shift_left = shift_left << 2

print("Shifting left and right")
print (bin(shift_right)) #0b11
print (bin(shift_left)) #0b100


# 7 / 14 - the & operator, AND
# at most, it can be the smaller of the two values
# finds all the turned on 1's in common

""" 0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
0b111 (7) & 0b1010 (10) = 0b10 
print out the result of calling bin() on 0b1110 & 0b101."""
print("Printing bin on the AND operator...")
print(bin(0b1110 & 0b101)) # 0b100
# this is because the first 1 is both a 1, and all the others are OR's, so 0









# 8 / 14 - The bitwise OR (|) operator 
""" 
The same as above, but only true when different:
0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1
 """
print("Doing the or thing with |...")
print((0b1110 | 0b101))
print(bin(0b1110 | 0b101)) # the bin allows us to stay in 0b notation







# 9 / 14 - The XOR (^) or exclusive or operator
# works like an OR, but returns false if both true 
""" 
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
"""
print("Doing the XOR function with ^...")
print(bin(0b1110 ^ 0b101)) # rejected this solution for the extra brackets needed in Py3




# 10 / 14 - The NOT operator, ~
# ~ 1 == 0 
# it just flips the binary value





# 11 / 14 - The man behind the bit mask
""" num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on" """
# we have used mask as a dummy variable to check against

def check_bit4(integer):
    mask = 0b1000
    if integer & mask > 0: # this means the fourth digit from the left is a 1
        return "on"
    else:
        return "off"

print("Checking bit four...")    
print(check_bit4(0b11001))    
print(check_bit4(0b011))    



# 12 / 14 - "Turning it on" - using the OR operator
# We have to turn the third digit on
print("Turning it on...")
a = 0b10111011
third_on = 0b100
switched =  a | third_on
print(bin(switched)) 







# 13 / 14 - Flipping out with the XOR
# The challenge is to flip all the bits, I think it might be similar to the above
print("Flipping bits...")
a = 0b11101110
mask = 0b1 # we can see the first digit is a 0
flipped =  mask ^ a # swapped them around this time?
print(flipped) # 239
print(bin(flipped)) # 0b11101111

# sort of correct idea, remember 
""" 
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
"""
# what this means is that anyhing with a 1 in it will always be flipped (even 2 no 1's)
new_mask = 0b111111111111111
#undo the order swap
new_flipped = a ^ new_mask
print(bin(new_flipped))

# but this is too long now, we've added value to the number
# use a list comprehension to create the mask

# print(len(a)) - this cannot be done, as a is an int
# lets just make it a string then

print(len(str(a))) # 3 - so all the 1's and 0's are registered as 1 char
# could then break down the bin(a) into say 64, then 32, then 16 etc
# this would then err for numbers >= 128, must be a better way
print(len(bin(a)) - 2)

a = 0b11101110 # 8 chars
def flipper(flip_me):
    print("Entered flip me function")
    no_of_ones_required = len(bin(flip_me)[2:])
    mask_setup = "1" * no_of_ones_required
    mask = int(mask_setup,2)
    pre_bin = flip_me ^ mask
    flipped = bin(pre_bin)
    # aha! diagnosed it is knocking off the extra 0's as these have no value
    # that is why the output isn't 8 chars, we have lost the 3 leading 0's
    return flipped

print(flipper(a)) #outputs, 0b10001, 5 chars



a = 0b11101110 

def flipper_function(to_be_flipped):
    print("___ Entered flipper funciton ___") # Here for debugging
    length_incoming = len(bin(to_be_flipped)[2:]) # takes '0b11101110', looks from 2: onwards, coutns this len
    mask = "1" * int(length_incoming) # uses the binary len to create a mask of the correct length (of 1's)
    return bin(to_be_flipped ^ int(mask, 2)) # returns input, against (^) mask, all in binary

print(flipper_function(a))

# now looking at refinements
# there is a built in tool to measure length, .bit_length
# to_be_flipped.bit_length() will give us a value of 10, one imagines

# knowing how many bits our number has, we can look to use bit shifts
# if we shift 1 left by (no of bits, chars), you get (e.g.) 100000
# taking off 1 from this, would then give us (e.g) 011111...... which is a nice mask!

a = 0b11101110 
def flipper_function2(to_be_flipped):
    print("____ Refined flipping function _____")
    bits = to_be_flipped.bit_length()
    mask = (1 << bits) - 1
    pre_bin = to_be_flipped ^ mask # I was using bits and not TBF, hence getting an error
    return bin(pre_bin)

print(flipper_function2(a))   




# Final try, nice and refined now
a = 0b11101110 
def flipper_function2(to_be_flipped):
    print("____ Refined refined flipping function _____")
    bits = to_be_flipped.bit_length() # returns 8, thanks to that handy function
    mask = (1 << bits) - 1 # 1 shifted becomes 9 bits, less 1 is 8 bits, all 1's    (really good logic hack)
    return bin(to_be_flipped ^ mask) # 

print(flipper_function2(a))   


# I just think it would be funny on one line

a = 0b11101110 

def flipper_function2(to_be_flipped):
    print("______ Refined refined refined flipping function _______")
    return bin(to_be_flipped ^ ((1 << to_be_flipped.bit_length()) - 1))

print(flipper_function2(a))   


# 14 / 14 - You've got to be kidding me, I quote
#"Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place."

bit = 0b110
position = 1

def flip_bit(number, n):
    mask = 0b1 << n-1 
    result = number ^ mask
    return (bin(result))

print(flip_bit(bit, position))
print(flip_bit(9, 1))
print(flip_bit(15, 2))
