"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Assignment Name, Date, File Name).
[x] 2. Program asks for at least 5 different inputs (variables).
[x] 3. Output uses F-Strings to combine text and variables.
[x] 4. Output uses at least one escape sequence (\n or \t).
[x] 5. Code contains comments explaining the steps.
[x] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# Madlibs program 8/25

# input and stores variables
print("\t\t\t\t Austin had an accident\n\n")
name = input("Please enter name: ")
name2 = input("Please enter another name: ")
object = input("enter a household object: ")
color = input("enter a random color: ")
shout = input("what would you shout if you stubbed your toe : ")

# output

print(f"\n\n{name} had an accident")
print(f"{name} had stubbed his toe on {object}")
print(f"\t\t\t\t{name} shouted {shout}!")
print(f"{name2} came and asked why is your toe {color}")
print(f"{name} said I stubbed my toe on this {object}")
