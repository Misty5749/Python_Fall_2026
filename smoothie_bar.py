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
def get_prices(size):
    if size == "small":
        return 3.00
    elif size == "medium":
        return 4.00
    elif size == "large":
        return 5.00


# selection for sizes

while True:
    size = input(f"what size would you like {SIZES}: ").lower()
    size_confirmation = input("Is that size okay (yes/no): ").lower()
    if size_confirmation == "yes":
        break
        # breaks the loop when user selects the correct size
    elif size_confirmation == "no":
        print("select another size")
        # repeats back to the start to select a new size

# selects which bases and how many

while True:
    base = input(f"what bases would you like {BASES}: ")

# selects which fruits and how many


# selects how many scoops

# TODO: Define blend(size, base, fruit, scoops)

# TODO: Define main() to collect input and call your logic
