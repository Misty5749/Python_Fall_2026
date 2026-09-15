"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

try:
    more_tickets = True
    tickets = 1
    while more_tickets:
        try:
            extra_tickets = input("Would you like more than 1 tickets (Y/N)").upper()
            if extra_tickets == "Y":
                tickets = int(input("how many tickets would you like: "))
                if tickets <= 0:
                    print("Must be more than 1 ticket")
                else:
                    print(f"Placed {tickets} tickets.")
                    more_tickets = False
            elif extra_tickets == "N":
                print(f"Ticket for {tickets}")
                more_tickets = False
            else:
                print("Please enter Y or N")
        except ValueError:
            print("error, ticket amount is not an integer")

    for ticket_number in range(tickets):
        ticket_number = ticket_number + 1
        print(f"ticket number {ticket_number}")
        # True is when the user inputs a letter/word for the age
        # False is when the user inputs a age in integer
        while True:
            try:
                age = int(input("input your age: "))
                if age >= 21:
                    print("you can get a drink ticket")
                    break
                else:
                    print("you can't get a drink ticket")
                    break
            except ValueError:
                print("error, age is not an integer")

        # True is when the user input for name is blank
        # False is when the user has a name with the ticket
        while True:
            try:
                first_name = input("input first name for ticket: ")
                last_name = input("input last name for ticket: ")
                if first_name == "" or last_name == "":
                    print("please input a name")
                else:
                    print(f"hello {first_name} {last_name}")
                    break
            except ValueError:
                print("Invalid input.")

        # True is when the user inputs a blank phone number
        # False is when the user inputs a phone number
        while True:
            try:
                phone = input(f"can i get a phone number {first_name} (altogether)")
                if phone == "":
                    print("Please enter in a phone number")
                elif phone.isdigit():
                    # asked copilot if there was a way to see if the user inputs a number or a letters/word
                    print("phone number good")
                    break
                else:
                    print("Phone number should be a integer")
            except ValueError:
                print("Please type in numbers")
except Exception:
    print("invalid input")
