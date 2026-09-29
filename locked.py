"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""

# allow only administer to change usernames aka are you a admin/user/employee
DEPARTMENT = "Information Technology"

USER_NAMES = ["BOBER", "MICHEALC", "POLISH", "AWWVWW", "HAMBURG"]
# switched the tuple into a mutable list to allow admins to change the usernames

passwords = [
    "BlueTiger42!",
    "MoonCoffee7#",
    "RiverStone91@",
    "SunnyCloud18$",
    "TeamRocket63%",
]

while True:
    try:
        print("1. look up username")
        print("2. Change password")
        print("3. Change username")
        print("4. Quit")

        choice = int(input("Please select which one you want to go to: "))
        match choice:
            case 1:
                lookup = input("input a username: ").upper()
                try:
                    for username in USER_NAMES:
                        if username == lookup:
                            print("Username found:", username)
                            break
                        else:
                            print("Username was not found.")
                            break
                except ValueError:
                    print("Username was not found.")
                except IndexError:
                    print("That user index does not exist.")
            case 2:
                lookup = input("input a username: ").upper()
                count = 0
                found = False
                try:
                    for username in USER_NAMES:
                        if username == lookup:
                            found = True
                            old_password = input("Enter in your old password: ")
                            # makes sure a random person can't change the password
                            if passwords[count] == old_password:
                                passwords[count] = input("Enter a new password: ")
                                print("Password updated")
                                break
                            else:
                                print("Incorrect password, contact IT desk for help")
                                break
                        count += 1
                    if found == False:
                        print("Username wasn't found")

                except ValueError:
                    print("Username was not found.")
                except IndexError:
                    print("That user index does not exist.")
            case 3:
                admin = input("Are you a admin (Yes/No): ").lower()
                if admin == "yes":
                    try:
                        index = int(input("enter in index user to change: "))
                        print(USER_NAMES[index])
                        # shows the admin which username is selected
                        USER_NAMES[index] = input("Enter in a new username: ").upper()
                        # changes the username to the new one
                    except TypeError:
                        print("please contact the help desk to change User Name")
                else:
                    print("Only an admin can change usernames.")

            case 4:
                break
            case _:
                print("Please enter in a correct choice")
    except TypeError:
        print("please contact the help desk to change User Name")
    except ValueError:
        print("Please enter in username")
