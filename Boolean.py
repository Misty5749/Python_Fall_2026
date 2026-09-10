"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# This program is about when people should sleep to hit their sleep target
sleep_desired = int(input("when do you want to wake up (numbers only): "))
sleep_actual = int(input("how many hours of sleep did you get (numbers only): "))

# this organize the amount of sleep the user inputs to show if they need more sleep or less sleep.
if sleep_desired >= 8 and sleep_actual >= 8:
    print("perfect amount of sleep")
elif sleep_desired >= 8 or sleep_actual >= 8:
    print("you should get both to 8 hours of sleep")
elif sleep_desired != sleep_actual:
    print("your sleep desires and actual sleep are not the same.")
elif sleep_desired > sleep_actual:
    print("you should go to sleep earlier")
elif sleep_desired < sleep_actual:
    print("Good job but you can sleep in later or wake up later")
elif sleep_actual == 0:
    print("you should sleep")
else:
    print("you should sleep more")
