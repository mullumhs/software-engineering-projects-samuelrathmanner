"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Perform basic operations and calculations using numbers.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ask the user for two numbers and store them in variables 'a' and 'b', converting to floats
a = float(input("Enter a number: "))
b = float(input("Enter a number: "))

# Add 'a' and 'b' and store the result in a variable 'add_result'
add_result = a+b

# Subtract 'b' from 'a' and store the result in a variable 'sub_result'
sub_result = a-b


# Multiply 'a' and 'b' and store the result in 'mul_result'

mul_result = a*b

# Divide 'a' by 'b' and store the result in 'div_result'

div_result = a/b

# Raise 'a' to the power of 'b' and store in 'exp_result'

exp_result = a**b

# Calculate the modulus of 'a' and 'b' and store in 'mod_result'

mod_result = a%b

# Print the results of each calculation, with a description of the operation, e.g. "5 plus 3 is 8"

print(f"a + b = {add_result}")
print(f"a - b = {sub_result}")
print(f"a x b = {mul_result}")
print(f"a / b = {div_result}")
print(f"a to the power of b = {exp_result}")
print(f"a mod b = {mod_result}")