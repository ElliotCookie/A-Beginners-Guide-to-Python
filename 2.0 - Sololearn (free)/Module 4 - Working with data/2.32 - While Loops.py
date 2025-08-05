""" 
While loops are powerful because they can be used 
ven when you don’t know how many iterations will be needed. """

for i in range(5):
  print("For Loop")

  
while seats > 0:
    print("Sell ticket")
    seats = seats - 1

counter = 0
while counter < 4:
  print(counter)
  counter = counter + 1
#there is a nice table here afterwards

#nice to know an infinite loop doesn't actually ping an error

i = 0
while i < 5:
  print(i)
  i = i + 1

  """ Lesson Takeaways
Fantastic work! You learned that:

🌟 you can apply iteration to your programs with the while loop

🌟 counters keep track of the number of iterations and avoid infinite loops

🌟 indentation and the colon : symbol are required for the code to run """