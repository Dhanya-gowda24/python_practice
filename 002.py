# Write a Python program to print a pyramid pattern of * using nested loops.

rows = 6  # Number of rows in the pyramid

for i in range(rows):
    # Print spaces for left padding
    for j in range(rows - i - 1):
        print("   ", end="")  # 3 spaces

    # Print stars with spacing
    for k in range(i + 1):
        print("*", end="     ")  # Star followed by 5 spaces

    print()  # Move to the next line
