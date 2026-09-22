"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# prints out the list of seats
seats = list(range(1, 21))


while True:
    try:
        print(seats)
        # prints out the list of available seats
        print("0 to quit\n")
        seat = int(input("which seat would you like: "))
        if seat == 0:  # ends the program when user selects
            print("\ngoodbye")
            break
        if seat >= 21:
            print("Value not in rage")
            # prevents any value
        elif seat in seats:  #
            print("seat selected")
            # removes the seat selected in the list
            seats.remove(seat)
        else:
            print("seat has already been taken\n")
            # informs the user that the seat is taken and to prevent errors
    except ValueError:
        print("value not in range")
