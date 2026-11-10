"""
ASSIGNMENT 12B: SPRINT 2 - FUNCTIONAL STUBS
Project: Bober Custard POS
"""

import random  # from magic_8ball.py
import read_menu

"""
things to do:
1. make the toppings more clean
2. add a file system
3. more toppings
4. add topping sections for easier use
5. make the customer ticket better
"""
DATA_FILE = "order_history.txt"
MENU_ITEMS = read_menu.read_menu() or {}
MENU_VALUES = read_menu.split_into_variables(MENU_ITEMS)
TOPPING_TEXT = MENU_VALUES[0] or ""
SIZE_TEXT = MENU_VALUES[1] or ""
PRICE_TEXT = MENU_VALUES[2] or ""
MIXED_TEXT = MENU_VALUES[3] or ""
FLAVOR_TEXT = MENU_VALUES[4] or ""


def take_order():
    """collects the amount of scoops, amount of toppings, which types of topping, and how much mixed"""
    # TODO: Get size, toppings and how much mixed
    name = input("Can I get a name for the order: ")

    sizes = []
    for size in SIZE_TEXT.split(","):
        size = size.strip()
        if size != "":
            sizes.append(size)

    toppings = []
    for topping in TOPPING_TEXT.split(","):
        topping = topping.strip()
        if topping != "" and topping.lower() != "plain":
            toppings.append(topping)

    read_menu.print_sizes(SIZE_TEXT, PRICE_TEXT)

    while True:
        try:
            size_choice = int(input("\nPlease enter the number for your size: "))
            if 1 <= size_choice <= len(sizes):
                break
            print(f"Please choose a number from 1 to {len(sizes)}.")
        except ValueError:
            print("Please enter a number.")

    chosen_toppings = []
    while True:
        read_menu.print_toppings(",".join(toppings))
        toppings_length = len(toppings)
        try:
            topping_choice = int(
                input("Choose a topping number (0 for plain/finish): ")
            )
            if topping_choice == 0:
                break
            if 1 <= topping_choice <= toppings_length:
                chosen_toppings.append(toppings[topping_choice - 1])
            else:
                print(f"Please choose a number from 0 to {toppings_length}.")
        except ValueError:
            print("Please enter a number.")

    return name, size_choice, chosen_toppings


def calculate_total(size_choice, chosen_toppings):
    """Return the size price plus $1 for each topping after the second."""
    total = get_price(size_choice)
    extra_toppings = len(chosen_toppings) - 2
    # when the user goes over 2 toppings it will add on $1
    if extra_toppings > 0:
        total = total + extra_toppings
    return total


def get_price(size_choice):
    prices = PRICE_TEXT.split(",")
    return float(prices[size_choice - 1].strip())


def customer_info(name):
    """Create a short system label and a readable customer label."""
    order_number = random.randint(1, 99)
    system_label = f"{order_number:02d}, {name}"
    customer_label = f"Customer {name}, number {order_number}"
    return system_label, customer_label


def send_data(system_label, size_choice, chosen_toppings):
    """Print an organized ticket for the person making the custard."""
    sizes = SIZE_TEXT.split(",")
    print("\n--- Custard Order ---")
    print(f"Order: {system_label}")
    print(f"Base: {sizes[size_choice - 1].strip()}")
    print("Toppings:")
    if chosen_toppings:
        for topping in chosen_toppings:
            print(f"- {topping}")
    else:
        print("- Plain")


def main():
    name, size_choice, chosen_toppings = take_order()
    system_label, customer_label = customer_info(name)
    total = calculate_total(size_choice, chosen_toppings)

    print(f"\n{customer_label}")
    send_data(system_label, size_choice, chosen_toppings)
    print(f"Total: ${total:.2f}")


main()
