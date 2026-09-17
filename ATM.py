"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a loop (using a state flag or while True) to remain awake.
[ ] 3. Main menu uses match-case logic with a wildcard (case _) for selections.
[ ] 4. Inputs are validated using try-except blocks to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

balance = 1000.00
is_running = True
while True:
    # will continue until user exits the program
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")
    choice = -1
    while True:
        try:
            choice = int(input("Please enter a number of your choice: "))
            break
        except ValueError:
            print("\nPlease enter a valid number\n")
        except Exception:
            print("")
    match choice:
        case 1:
            print(f"you have ${balance}")
        case 2:
            try:
                deposit = float(input("how much would you like to deposit: "))
                if deposit <= 0:  # prevent less than $0
                    print("you can't deposit less than $0")
                else:
                    balance += deposit  # add money to balance
                    print(f"deposited {deposit:.2f}, total amount {balance:.2f}")
                continue
            except ValueError:
                print("please enter in a integer")
            except Exception:
                print("please enter an integer")
        case 3:
            try:
                withdraw = float(input("how much would you like to withdraw: "))
                if withdraw <= 0:  # prevent less than $0
                    print("you can't withdraw less than $0")
                elif withdraw >= balance:
                    # prevent transferring more than what they have
                    print("you can't withdraw that much")
                else:
                    balance -= withdraw  # remove money from the account
                    print(f"withdrawn {withdraw:.2f}, total amount {balance:.2f}")
                continue
            except ValueError:
                print("please enter in a integer")
            except Exception:
                print("please enter an integer")
        case 4:
            try:
                transfer = float(input("how much would you like to transfer: "))
                if transfer <= 0:  # prevent less than $0
                    print("you can't transfer less than $0")
                elif (
                    transfer >= balance
                ):  # prevent transferring more than what they have
                    print("you can't transfer that much")
                else:
                    balance -= transfer  # remove money from the account
                    print(
                        f"transferred {transfer:.2f} to a random account, thanks for the money, total amount {balance:.2f}"
                    )
                continue
            except ValueError:
                print("please enter in a integer")
            except Exception:
                print("please enter an integer")
        case 5:
            print("Goodbye")
            break  # exits the program
        case _:
            print("please enter 1-5")
            # makes sure that the user inputs the correct numbers


# except ValueError:
#     print("")
# except Exception:
#     print("")
