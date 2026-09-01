"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float)(Rent, Utilities, etc.)
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# user's monthly expenses
name = input("Enter name: ")
income = input("Enter monthly income: ")
rent = input("Cost of rent monthly: ")
utilities = input("Cost of utilities monthly: ")
food = input("Cost of food monthly: ")
hobbies = input("Cost of hobbies monthly: ")
gas = input("Cost of gas monthly: ")
col_rent = "rent"


# user's total expenses
print(f"{col_rent:^40}")
