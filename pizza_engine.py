"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("cheese", "pepperoni", "bacon", "sausage")


def get_price(size):
    if size == "small":
        return 8.00
    elif size == "medium":
        return 10.50
    elif size == "large":
        return 12.00
    return 0.00


# gets the price of the pizza based of the size


def customer():
    name = input("What is your name? ")
    return name.strip()


# removes any spaces in name


def size():
    while True:
        pizza_size = (
            input("What size pizza would you like (small, medium, large): ")
            .lower()
            .strip()
        )
        # makes sure that the size is available
        if pizza_size in ("small", "medium", "large"):
            return pizza_size
        else:
            print("please enter a correct size")


def toppings():
    while True:
        pizza_toppings = (
            input(f"What topping would you like {TOPPINGS}").lower().strip()
        )
        # makes sure that the topping is available
        if pizza_toppings in ("cheese", "pepperoni", "bacon", "sausage"):
            return pizza_toppings
        else:
            print("please enter a correct toppings")


def delivery():
    while True:
        # makes sure that the user selects pickup or for delivery
        order_type = input("Will this be pickup or for delivery? ").strip().lower()
        if order_type == "delivery":
            return True
        elif order_type == "pickup":
            return False
        else:
            print("please enter here or delivery")


def make_pizza(customer_name, pizza_size, pizza_toppings, is_delivery=False):
    total = get_price(pizza_size)
    order_type = "delivery" if is_delivery else "pickup"

    print(f"\n{customer_name}'s pizza order:")
    print(f"Size: {pizza_size}")
    print(f"Toppings: {pizza_toppings}")
    print(f"Order type: {order_type}")
    print(f"Total: ${total:.2f}")


def main():
    print(f"Global Pantry: {TOPPINGS}")
    customer_name = customer()
    pizza_size_choice = size()
    pizza_toppings_choice = toppings()
    is_delivery_order = delivery()
    make_pizza(
        customer_name=customer_name,
        pizza_size=pizza_size_choice,
        pizza_toppings=pizza_toppings_choice,
        is_delivery=is_delivery_order,
    )


main()
