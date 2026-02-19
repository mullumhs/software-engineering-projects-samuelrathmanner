"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Ask for first and last name and greet user by their full name.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

first_name = input("whats your first name? ")
last_name  = input("whats your last name? ")

first_name = first_name.strip()
last_name  = last_name.strip()

first_name = first_name.title()
last_name = last_name.title()

print(f"Hello {first_name} {last_name}!")