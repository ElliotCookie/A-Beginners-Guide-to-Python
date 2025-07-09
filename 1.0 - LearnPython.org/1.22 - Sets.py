#These are just lists with no duplicate entries, easily accessed:
print(set("This is a sentance to test sets and see what comes out".split()))
a = set(["Mudkip", "Marshtomp", "Swampert"])
print(a)
b = set(["Sceptile", "Swampert", "Blaziken"])
print(a.intersection(b))
print(b.symmetric_difference(a))
print(a.difference(b))
print(a.union(b))

""" In the exercise below, use the given lists to print out a set 
containing all the participants from event A which did not attend event B. """
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
differenceSet = set(a) - set(b)
print(differenceSet)
