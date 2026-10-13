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

# selection for sizes

while True:
    size = input(f"what size would you like {SIZES}: ").lower()
    try:

        if size == "small":
            print(f"The total for {size} is $3")
            size_price = 3
        elif size == "medium":
            print(f"The total for {size} is $4")
            size_price = 4
        elif size == "large":
            print(f"The total for {size} is $5")
            size_price = 5
        else:
            print("please select a valid size")
            continue
        # makes sure user select correct value and to ask the question again before moving on
        size_confirmation = input("Is that size okay (yes/no): ").lower()
        if size_confirmation == "yes":
            break
        # breaks the loop when user selects the correct size
        elif size_confirmation == "no":
            print("select another size")
        # repeats back to the start to select a new size
    except ValueError:
        print("Invalid input.")

# selects which bases and how many

while True:
    base = input(f"what bases would you like {BASES}: ")

# selects which fruits and how many


# selects how many scoops

# TODO: Define blend(size, base, fruit, scoops)

# TODO: Define main() to collect input and call your logic
