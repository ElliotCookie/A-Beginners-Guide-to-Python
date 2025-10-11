#fix these:

""" print("How do you make a hot dog stand?')
print(You take away its chair!) """
      
#Now asking for todays date, can python do dates?
#looks like there is a datetime module

from datetime import * 

date_string = "2025-06-15 14:30:00"
format_code = "%Y-%m-%d %H:%M:%S"

parsed_date = datetime.strptime(date_string, format_code)
print(parsed_date)
# Outputs: 2025-06-15 14:30:00
print(parsed_date.year)
# Outputs: 2025


mirthful_addition = 12381 + 91817
amazing_subtraction = 981 - 312
trippy_multiplication = 38 * 902
happy_division = 540 / 45
sassy_combinations = 129 * 1345 + 120 / 6 - 12

#mention of the modulo operator, %
#this returns what is left after a division


product = 5 * 6
remainder = 1398%11
print(remainder)

fish_in_clarks_pond = 50

print ("Catching fish")

number_of_fish_caught = 10
fish_in_clarks_pond = fish_in_clarks_pond - number_of_fish_caught
#obviously going to be a lesson on data types


august_rainfall = 4.91
annual_rainfall = august_rainfall

september_rainfall = 5.16
october_rainfall = 7.20
november_rainfall = 5.06
december_rainfall = 4.06

annual_rainfall += (september_rainfall + october_rainfall + november_rainfall + december_rainfall)

cucumbers = 7
price_per_cucumber = 3.25

total_cost = cucumbers * price_per_cucumber
print(total_cost)


#Two Types of Division
cucumbers = 100
num_people = 6

#Just doing it like this gives the whole number
whole_cucumbers_per_person = 100/6
print(whole_cucumbers_per_person)

#Two ways to make the decimal place
method_one = float(cucumbers)/num_people
#method_two = cucumbers./num_people.
# looks like method two is for Py 2 only
# wait
test = 100. 
method_two = test / num_people
print(method_two)


print(method_one)

#If we want a string to span multiple lines, we can also use triple quotes:
#I did not know this was a thing?!
address_string = """136 Whowho Rd
Apt 7
Whosville, WZ 44494"""
print(address_string)

age_is_12 = False # remembering this is a capital letter


#Use can use str(), int() and float() to basially do arithmatic and print 
# data types interchangably

float_1 = 0.25
float_2 = 40.0

product = float_1 * float_2
big_string = (f"The product was {product}")
#big_string = "The product was " + str(product)
print(big_string)


#big test at the end!!
skill_completed = "Python Syntax"
exercises_completed = 13
#The amount of points for each exercise may change, because points don't exist yet
points_per_exercise = 5
point_total = 100
point_total += exercises_completed * points_per_exercise

print(f"I got {point_total} points!")
#print("I got ") + str(point_total) + " points!"