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
income_rent = net_income - rent
income_utilities = income_rent - utilities
income_food = income_utilities - food
income_hobbies = income_food - hobbies
income_gas = income_hobbies - gas

# table of expenses
print(f"Gross Income: ${gross_income:,.2f}")
print(f"Net Income: ${net_income:,.2f}")
print(
    f"Income after bills: ${income_rent:,.2f}\n{income_utilities:,.2f}\n{income_food:,.2f}\n{income_hobbies:,.2f}\n{income_gas:,.2f}"
)
