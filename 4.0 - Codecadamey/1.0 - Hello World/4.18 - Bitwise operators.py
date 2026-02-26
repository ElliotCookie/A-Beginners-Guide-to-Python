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
shift_left << 2 == 0b100
shift_right >> 2 == 0b11 

print (bin(shift_right))
print (bin(shift_left))


# rushing today, but still here!