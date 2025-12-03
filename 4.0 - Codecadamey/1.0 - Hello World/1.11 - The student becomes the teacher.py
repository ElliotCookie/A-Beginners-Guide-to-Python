lloyd = {}
alice = {}
tyler = {}
dict_list = [lloyd, alice, tyler]

newkeys = ["name", "homework", "quizzes", "tests"]

def adding_keys_to_dicts(keylist):
    for keys in keylist:
        for dicts in dict_list:
            dicts[keys] = []
    
adding_keys_to_dicts(newkeys)

lloyd["name"] = "Lloyd"
alice["name"] = "Alice"
tyler["name"] = "Tyler"

for dict in dict_list:
    print(dict)


#adding in the scores - makes redundant text above
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

for student in dict_list:
    print (student["name"])
    print (student["homework"])
    print (student["quizzes"])
    print (student["tests"])


#doing the average function
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return (total / len(numbers))

trial = [3, 4, 5]
print("Average of numbers is:")
print(average(trial))