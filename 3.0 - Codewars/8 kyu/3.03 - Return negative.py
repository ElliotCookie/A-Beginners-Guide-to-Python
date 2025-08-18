#In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
""" def make_negative( number ):
    pass """

def make_negative( number ):
    """ if number < 0:
        pass
    else:
        number = number * -1
    return number """
    
    #here is a great idea: return -abs(number)

    if number > 0: return number * -1
    else: return number



        



if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(make_negative(n))

