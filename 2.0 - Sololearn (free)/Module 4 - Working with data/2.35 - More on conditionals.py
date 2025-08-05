""" Conditional statements allow you to program machines that make decisions.
In this lesson, you’ll learn to program more complex scenarios. """

temperature = 36
if temperature > 39:
  print("High temperature")
else:
  print("No fever")
  #what will it print??

  #if, elif and else statements need to be in the correct order.

age = 29
is_student = True
if age < 18:
  if is_student:
    print(f"20% discount")
else:
  print("Regular price")
print("Proceed to payment")

""" Lesson Takeaways
Great job! You learned that you can:
🌟 skip the else statement when it is not needed

🌟 check for more conditions with the elif statement

🌟 nest if-else statements within each other """