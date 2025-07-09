#Python deals with errors by calling them exceptions, e.g
""" print(a) """
#Name error: 'a' isn't defined

#obviously a full on crash isn't ideal, so you can add a catch to allow
#the programme to keep running, even if there is an error


try:
    print(a)
except:
    b = 5
    print(f"Fell into exception cause, printing other variable: {b}")


#but wait, there is more! The format goes like this:
""" Try:
    except (name an error):
    else:
    finally: """
#so the above code is naughty as the except catches everything, we should be 
#specific here

try:
    num = 10/0
    print(c + num)
except SyntaxError:
    print("Reached except Syntax clause")
    print(d)
except ZeroDivisionError:
    print("Dividing by 0 doesn't work silly, ZeroDiVEr clause")
except NameError:
    print("Reached NameError clause")
else:  #if no error then this one is also run
    print("Reached else clause") #skipped if we reach an except clause
    print(e)
finally: #always runs after try
    print("Reached the finally clause, this one always happens")

try:
    print("working sentance")
finally:
    print("another working sentance")
""" 


Exercise
Handle all the exception! 
Think back to the previous lessons to return the last name of the actor. """

# Setup
import re
actor = {"name": "John Cleese", "rank": "awesome"} #a dictionary

# Function to modify!!!
def get_last_name():
    # open up our dictionary
    # find the name in it
    # find the space in the name to indicate the last name
    # take all the chars after the whitespace
    # input these into a new index called "last_name" 
    fullNameInQuestion = actor["name"]
    matchObject = re.search(r"\s+(\S+)$", fullNameInQuestion)
    last_name = matchObject.group(1) if matchObject else ""
    actor["last_name"] = last_name
    return actor["last_name"]

# Test code
try:
    get_last_name()
    
finally:
    print("All exceptions caught! Good job!")
    print("The actor's last name is %s" % get_last_name())
