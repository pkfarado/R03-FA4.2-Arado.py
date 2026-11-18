# Student Information Formatting Tool - Version 2
# Added string formatting (.title(), .upper(), len())

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

full_name = f"{first_name} {last_name}"

print("\nFormatted Output:")
print(f"Name: {full_name.title()}")
print(f"Name Code: {full_name.upper()}")
print(f"Section: {section.upper()}")
print(f"Favorite Subject: {favorite_subject.title()}")
print(f"Character Count: {len(full_name)}")
