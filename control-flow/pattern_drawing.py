# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop for rows
while row < size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")  # Print * without newline
    print()  # Move to next line after one row
    row += 1


