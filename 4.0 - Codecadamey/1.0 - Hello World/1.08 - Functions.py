def spam():
  """ prints 'Eggs!' to the console """
  print ("Eggs!")

spam() 


#Another example, parsing values
def power(base, exponent):  # Add your parameters here!
  result = base ** exponent
  print (f"length = {len(str(result))}")
  print ("%d to the power of %d is %d." % (base, exponent, result))

base_input = int(input("base: "))
power_input = int(input("power: "))
power(base_input, power_input) 

#looking at making an etf creator, no progress!