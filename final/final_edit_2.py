"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Bober Custard POS
"""

TOPPINGS = (
    "1. Hot fudge",
    "2. Sprinkles",
    "3. Caramel sauce",
    "4. Crushed Oreos",
    "5. Cookie dough bites",
    "6. Brownie bites",
    "7. Strawberries",
    "8. Bananas",
    "9. Chopped nuts",
    "10. Whipped cream",
    "11. Cherries",
    "12. Mini marshmallows",
    "13. Peanut butter cups",
    "14. Chocolate chips",
    "15. Plain",
)
# made above with AI
SIZES = ("1. Small", "2. Medium,", "3.Large")


def get_price(size):
    if size == "small":
        return 5.50
    elif size == "medium":
        return 7.50
    elif size == "large":
        return 8.50


def take_order():
    """collects the amount of scoops, amount of toppings, which types of topping, and how much mixed"""
    # TODO: Get size, toppings and how much mixed
    name = input("Can i get a name for the order: ")
    size = int(input(f"{SIZES}\nPlease select a size (1, 2, or 3) "))
    chosen_toppings = []
    while True:
        try:
            print(f"{TOPPINGS}")
            toppings = int(
                input("Please select a number for your topping and plain to end: ")
            )
            if toppings == 15:
                break
            chosen_toppings.append(TOPPINGS[toppings - 1])
        except ValueError:
            print("please enter in a number within the list")


test_order = take_order()
print(test_order)


def calculate_total():
    """gets the price of the total amount and including if they want more than 2 toppings"""
    # TODO get price from menu

    pass


# def customer_info():
#     """sends data to order history and creates a label with a number (1-99). Creates a human readable label"""
#     # TODO create 2 labels, one for the system and the other for humans
#     pass


# def send_data():
#     """sends the data to the people making the custard"""
#     # TODO send the data in a organize blocks on what base first then topping then how much mixing
#     pass


# def main():
#     # info of customer
#     name, number = customer_info()
#     print(f"Customer {name} Number {number}")

#     # order of customer
#     current_order = take_order()

#     # price of the order
#     final_price = calculate_total(current_order)

#     # saves the data of the order
#     send_data(name, number, current_order, final_price)


# main()
