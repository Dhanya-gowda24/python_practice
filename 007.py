#Read a line of space‑separated integers and print their average, rounded to two decimal places.

def avg(*args):
    # Calculate average and round to 2 decimal places
    return round(sum(args) / len(args), 2)

# Read space-separated integers from input
numbers = list(map(int, input().split()))

# Call the avg function with unpacked list
result = avg(*numbers)

# Print the result formatted to 2 decimal places
print("{:.2f}".format(result))
