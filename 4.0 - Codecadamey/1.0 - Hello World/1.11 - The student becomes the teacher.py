lloyd = {}
alice = {}
tyler = {}

newkeys = ["name", "homework", "quizzes", "tests"]

def adding_keys_to_dicts(keylist):
    for keys in keylist:
        lloyd[keys] = []
        alice[keys] = []
        tyler[keys] = []
    
adding_keys_to_dicts(newkeys)

lloyd["name"] = "Lloyd"
alice["name"] = "Alice"
tyler["name"] = "Tyler"

print(lloyd)
print(alice)
print(tyler)
