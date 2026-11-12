"""
ASSIGNMENT 12B: SPRINT 2 - FUNCTIONAL STUBS
Project: Bober Custard POS
"""

import random  # from magic_8ball.py
import read_menu

"""
things to do:

2. add a file system
3. more toppings
5. make the customer ticket better

AI recommends:

Create main.py to run the program.
Create employees.py for employee records.
Create orders.py for order records.
Create print_orders.py to print order tickets.
Create employees.txt and orders.txt.
Write functions to load and save employees and orders.
Add options to create, find, update, and delete records.
Use employee dictionaries and lists to organize data.
Add type hints and the required order price calculations.
Handle input and file errors, and log errors in error.txt.
"""
DATA_FILE = "order.txt"


def get_menu_values():
    """Return the menu values as a fresh dictionary each time they are needed."""
    menu_items = read_menu.read_menu() or {}
    topping_text, size_text, price_text, mixed_text, flavor_text = (
        read_menu.split_into_variables(menu_items)
    )
    return {
        "toppings": topping_text or "",
        "sizes": size_text or "",
        "prices": price_text or "",
        "mixed": mixed_text or "",
        "flavors": flavor_text or "",
    }


def take_order():
    """collects the amount of scoops, amount of toppings, which types of topping, and how much mixed"""
    # TODO: Get size, toppings and how much mixed
    name = input("Can I get a name for the order: ")
    menu_values = get_menu_values()
    size_text = menu_values["sizes"]
    topping_text = menu_values["toppings"]
    price_text = menu_values["prices"]

    sizes = []
    for size in size_text.split(","):
        size = size.strip()
        if size != "":
            sizes.append(size)

    toppings = []
    for topping in topping_text.split(","):
        topping = topping.strip()
        if topping != "" and topping.lower() != "plain":
            toppings.append(topping)

    read_menu.print_sizes(size_text, price_text)
    list_length = len(sizes)

    while True:
        try:
            size_choice = int(input("\nPlease enter the number for your size: "))
            if 1 <= size_choice <= list_length:
                break
            print(f"Please choose a number from 1 to {list_length}.")
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
    if extra_toppings > 0:
        total = total + extra_toppings
    return total


def get_price(size_choice):
    menu_values = get_menu_values()
    price_text = menu_values["prices"]
    prices = []
    for price in price_text.split(","):
        price = price.strip()
        if price != "":
            prices.append(price)
    return float(prices[size_choice - 1])


def customer_info(name):
    """Create a short system label and a readable customer label."""
    order_number = random.randint(1, 99)
    system_label = f"{order_number:02d}, {name}"
    customer_label = f"Customer {name}, number {order_number}"
    return system_label, customer_label


def send_data(system_label, size_choice, chosen_toppings):
    """Print an organized ticket for the person making the custard."""
    size_text = get_menu_values()["sizes"]
    sizes = size_text.split(",")
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
