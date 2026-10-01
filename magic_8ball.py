"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""

import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = (
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "Definitely not",
    "Do it later",
    "Are you sure?",
    "Just DO IT",
)

print("Welcome to the Digital Oracle!")
while True:
    try:
        question = input("type to get an answer or quit: ").lower()
        if question == "quit":
            print("goodbye")
            break
        else:
            print(random.choice(RESPONSES))
    except ValueError:
        print("please enter in words")
# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop
