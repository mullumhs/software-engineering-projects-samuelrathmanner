"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to format numbers for display.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ask the user for a decimal number and store it in a variable 'num1', converting to a float
num1 = float(input("Enter a number: "))

# Round the number to 2 decimal places using the round function
num1 = round(num1,2)
print(f"My number rounded to 2 decimals: {num1}")


# Define a large integer
large_num = 999999999

# Print the large integer with commas as thousands separators using f-strings

print(f"large number withm commas: {large_num:,}")


# Define a small floating-point number

small_num = 0.000000000123456789

# Print the number in scientific notation using f-strings
print(f"small number in scientific notation: {small_num:.2e}")

# Define a small integer
small_int = 7

# Print the number with leading zeros using f-strings
print(f"small integer with padded with 5 Zeros: {small_int:05}")