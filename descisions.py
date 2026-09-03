"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
"""

# TODO 1: Ask the user for the day of the week.
day = input("enter the day of the week, don't abbreviate: ").lower()


# TODO 3: Use match/case to set child_price_per_year.
match day:
    case "tuesday":
        child_price_per_year = 0.5
    case "sunday":
        child_price_per_year = 1
        print("Free Drinks")
    case _:
        child_price_per_year = 1
# Tuesday: $0.50 per year.
# Sunday: $1.00 per year and print the free-drinks notice.
# Every other day: $1.00 per year using the default case (case _).

# TODO 4: Ask the user for their age and convert it to an integer.
age = int(input("enter in your age in numbers: "))
child_price = child_price_per_year * age
# TODO 5: Use if/elif/else to calculate the price.
if age < 1:
    print("Tickets are free ($0.00)")
elif age <= 12:
    print(f"Tickets will cost ${child_price:.2f}")
elif age <= 64:
    ticket_price = 16.95
    print(f"Tickets will cost ${ticket_price:,.2f}")
else:
    ticket_price = 12.95
    print(f"Tickets will cost ${ticket_price:,.2f}")

# Under 1: FREE ($0.00)
# Ages 1 to 12: age multiplied by child_price_per_year
# Ages 13 to 64: $16.95
# Age 65 and older: $12.95


# TODO 6: Print the final price formatted as currency.
