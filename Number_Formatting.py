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
income_net = float(input("Enter monthly net income: "))
rent = float(input("Cost of rent monthly: "))
utilities = float(input("Cost of utilities monthly: "))
food = float(input("Cost of food monthly: "))
hobbies = float(input("Cost of hobbies monthly: "))
gas = float(input("Cost of gas monthly: "))


# user's total income
total_expenses = rent + utilities + food + hobbies + gas

# table of expenses
print(f"{name} expenses")
print(f"\n\n\nNet Income: ${income_net:,.2f}")
print(
    f"Total Expenses ${total_expenses:,.2f} \t total amount left over: ${(income_net - total_expenses):,.2f}"
)
print(f"Percent of money used: {(total_expenses / income_net):,.2f}%\n")
print(f"Rent: ${rent:,.2f}")
print(f"Utilities: ${utilities:,.2f}")
print(f"Food: ${food:,.2f}")
print(f"Hobbies: ${hobbies:,.2f}")
print(f"Gas: ${gas:,.2f}")
