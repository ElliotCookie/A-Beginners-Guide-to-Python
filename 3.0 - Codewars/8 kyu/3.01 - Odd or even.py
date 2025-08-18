
#Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

# Optional: allow local testing when running the file directly,
# but this block is NOT executed when Codewars imports the module.
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(even_or_odd(n))


