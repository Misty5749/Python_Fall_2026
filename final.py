"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Bober Custard POS
"""


def take_order():
    """collects the amount of scoops, amount of toppings, which types of topping, and how much mixed"""
    # TODO: Get size, toppings and how much mixed
    pass


def calculate_total():
    """gets the price of the total amount and including if they want more than 2 toppings"""
    # TODO get price from menu
    pass


def customer_info():
    """sends data to order history and creates a label with a number (1-99). Creates a human readable label"""
    # TODO create 2 labels, one for the system and the other for humans
    pass


def send_data():
    """sends the data to the people making the custard"""
    # TODO send the data in a organize blocks on what base first then topping then how much mixing
    pass


def main():
    # info of customer
    name, number = customer_info()
    print(f"Customer {name} Number {number}")

    # order of customer
    current_order = take_order()

    # price of the order
    final_price = calculate_total(current_order)

    # saves the data of the order
    send_data(name, number, current_order, final_price)


main()
