"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# task 1 (Are we there yet)
# creates a variable to keep track if the car is driving
driving = True
# user inputs if the car is still driving
while driving:
    answer = input("are we there yet (yes/no)").lower()
    if answer == "yes":
        driving = False

# task 2 (99 bottles of beer)
# counts down from 99 to 1 and sends one line for every time it goes down
for count in range(99, 0, -1):
    if (
        count == 1
    ):  # makes sure that once it hits 1 it will say 1 bottle instead of 1 bottles
        print(
            f"{count} bottle of beer on the wall. Take one and pass it around, no more beer on the wall.\n"
        )
    else:
        print(f"{count} bottles of beer on the wall. Take one and pass it around\n")
