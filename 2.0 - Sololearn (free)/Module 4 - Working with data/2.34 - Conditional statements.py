""" Selection is like a fork in the road.
It allows your programs to decide which path to take. 

In this lesson, you’ll learn to build code 
that uses selection to make decisions. """

#immediate paywall

age = 16
if age >= 18:
  print("Regular price")
else:
  print("Discount")

#The else conditional statement starts with the keyword
#else followed by a colon : symbol

#remeber or is optimistic, this saves you so much

age = 32
is_student = True
if age < 18 or is_student:
  print("Discount")
else: 
  print("Regular price")

""" Lesson Takeaways
Well done! You learned that:

🌟 if-else statements are used to implement selection into your programs

🌟 the colon : symbol and the use of indentation are needed to prevent errors """