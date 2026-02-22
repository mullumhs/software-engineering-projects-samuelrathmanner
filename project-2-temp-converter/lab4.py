"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Use conditional statements to control the flow of execution.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Ask the user for an integer and store it in a variable 'num'
num = int(input("Enter an intger: "))

# Use an if statement to check if the number is positive, negative or zero
if num < 0:
    print("your number is negative")
elif num > 0:
    print("your number is postive")
else:
    print("your number is 0")

# Ask the user for their age and store it in a variable 'age'
age = int(input("what is your age? "))


# Use an if statement to check if the user is an adult (18+) or a minor

if age> 18:
    print("your an adult")
else:
    print("your a minor")

# Ask the user for two integers, 'a' and 'b'
a = int(input("enter an integer: "))
b = int(input("enter a second integer: "))


# Use an if statement to check if both numbers are positive or both are negative
# Otherwise print "One number is positive and the other is negative."

if a > 0  and b > 0 :
    print("both your numbers are positive")
elif a < 0  and b < 0 :
    print("both your numbers are negative")
else:
    print("your numbers are posutive and negative (or zero)")