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
