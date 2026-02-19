"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Ask for full name and greet user by their first name only.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
full_name = input("whats your full name? ")

full_name = full_name.strip()
full_name = full_name.title()

full_name = full_name.split()


print("Hello " + full_name[0] +"!")