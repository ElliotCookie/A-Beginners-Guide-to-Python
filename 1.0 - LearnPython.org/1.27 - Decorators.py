# Seems pretty huge, allow you to modify callable objects like classes, methods or funcitons
# It uses some more keyword-like notation

# Instead of writing
def function(argument):
    return "value"
#function = decorator(function) (<--- errors)
# passing the function to the decorator, reassigning it

# We can write:
@decorator
def anotherFunction(argument):
    return "value"

test upload