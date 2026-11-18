# Student Information Formatting Tool - Version 1
# Initial version: Basic input and output without string methods
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

print("\nFormatted Output:")
print("Name:", first_name, last_name)
print("Name Code:", first_name, last_name)
print("Section:", section)
print("Favorite Subject:", favorite_subject)
print("Character Count:", len(first_name + " " + last_name))
