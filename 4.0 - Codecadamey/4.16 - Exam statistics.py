# 1/9 was just pressing run

# 2 / 9 printing grades:
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
    for grade in grades_input:
        print(grade)

print_grades(grades)

#3 / 9 just pressing run

# 4 / 9 - sum of scores

def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total

print_grades([(grades_sum(grades))]) # using [] to make it 'iterable'


# 5 / 9 - grades average

def grades_average(grades_input):
    sum = grades_sum(grades_input)
    average = sum / float(len(grades_input))
    return average

print(grades_average(grades))

# 6 / 9 is just pressing run

# 7 / 9 - variance
print("Variance:")

def grades_varience(scores):
    average = grades_average(scores) # I have a typo here and therefore the solution doesn't accept it
    varience = 0
    for score in scores:
        varience += (average - score) ** 2
    return (varience / len(scores))

print(grades_varience(grades))

def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_varience(grades)
print(grades_std_deviation(variance))        


# 9/9 Printing everything
print("Printing everything...")
print(grades)
print(grades_sum(grades))
print(grades_average(grades))
print(grades_varience(grades))
print(grades_std_deviation(variance))