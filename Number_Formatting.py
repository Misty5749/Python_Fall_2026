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
gross_income = float(input("Enter monthly gross income: "))
rent = float(input("Cost of rent monthly: "))
utilities = float(input("Cost of utilities monthly: "))
food = float(input("Cost of food monthly: "))
hobbies = float(input("Cost of hobbies monthly: "))
gas = float(input("Cost of gas monthly: "))


# user's total income
fed_tax = gross_income * 0.20
net_income = gross_income - fed_tax

#table of expenses
print(f"Gross Income: ${gross_income,.2%}")
print(f"Net Income: ${net_income,.2%}")
print(f"Income after rent: ${net_income - rent,.2%}")