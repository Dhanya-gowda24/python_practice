''' Write a Python function that prints numbers from 1 to n, replacing:

Multiples of 3 with "Fizz",
Multiples of 5 with "Buzz",
Multiples of both with "FizzBuzz". '''

# Function to print FizzBuzz sequence from 1 to n
def fizzBuzz(n):
    for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
        # If number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # If number is divisible only by 3
        elif i % 3 == 0:
            print("Fizz")
        # If number is divisible only by 5
        elif i % 5 == 0:
            print("Buzz")
        # If number is not divisible by 3 or 5
        else:
            print(i)

# Take user input and call the function
n = int(input("Enter a number: ").strip())
fizzBuzz(n)
