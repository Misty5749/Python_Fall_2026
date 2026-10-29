"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Bober Custard POS
"""

import random

"""
things to do:
1. make the toppings more clean
2. add a file system
3. more toppings
4. add topping sections for easier use
5. make the customer ticket better
"""
TOPPINGS = (
    "0. Plain",
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
)
# made above with AI
SIZES = ("1. Small", "2. Medium", "3. Large")


def get_price(size_choice):
    if size_choice == 1:
        return 5.50
    elif size_choice == 2:
        return 7.50
    elif size_choice == 3:
        return 8.50
    else:
        raise ValueError("Size must be 1, 2, or 3.")


def take_order():
    """collects the amount of scoops, amount of toppings, which types of topping, and how much mixed"""
    # TODO: Get size, toppings and how much mixed
    name = input("Can I get a name for the order: ")

    while True:
        try:
            size_choice = int(input(f"{SIZES}\nPlease select a size (1, 2, or 3): "))
            if size_choice in (1, 2, 3):
                break
            print("Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

    chosen_toppings = []
    while True:
        print(TOPPINGS)
        toppings_length = len(TOPPINGS)
        try:
            topping_choice = int(
                input("Choose a topping number (0 for plain/finish): ")
            )
            if topping_choice == 0:
                break
            if 1 <= topping_choice <= toppings_length:
                chosen_toppings.append(TOPPINGS[topping_choice - 1])
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


def customer_info(name):
    """Create a short system label and a readable customer label."""
    order_number = random.randint(1, 99)
    system_label = f"order-{order_number:02d}, {name}"
    customer_label = f"Customer {name}, number {order_number}"
    return system_label, customer_label


def send_data(system_label, size_choice, chosen_toppings):
    """Print an organized ticket for the person making the custard."""
    print("\n--- Custard Order ---")
    print(f"Order: {system_label}")
    print(f"Base: {SIZES[size_choice - 1]}")
    print("Toppings:")
    if chosen_toppings:
        for topping in chosen_toppings:
            # asked AI how to spilt the toppings into different rows
            print(f"- {topping.split('. ', 1)[1]}")
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
