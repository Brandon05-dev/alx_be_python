# File: pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # For each row, print * size times side by side
    for col in range(size):
        print("*", end="")
    print()  # Newline after each row
    row += 1
