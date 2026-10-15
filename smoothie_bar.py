"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
SIZES = ("Small", "Medium", "Large")
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# TODO: Define get_price(size)
def get_price(size):
    if size == "small":
        return 3.00
    elif size == "medium":
        return 4.00
    elif size == "large":
        return 5.00


# selection for sizes
def main():
    try:
        size = input(f"what size would you like {SIZES}: ").lower()

        amount_base = int(input(f"{BASES}\nHow many bases would you like: "))
        base = input(f"what bases would you like: ")

        amount_fruit = int(input(f"{FRUITS}\nHow many bases would you like: "))
        fruits = input("what bases would you like: ")

        scoops = int(input("how many scoops would you like: "))
    except ValueError:
        print("please enter in a number")


main()
def blend(size, base, fruit, scoops):
# selects which bases and how many


# selects which fruits and how many


# selects how many scoops

# TODO: Define blend(size, base, fruit, scoops)

# TODO: Define main() to collect input and call your logic
