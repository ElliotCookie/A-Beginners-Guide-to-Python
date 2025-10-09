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