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


print (bin(shift_right))
print (bin(shift_left))


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