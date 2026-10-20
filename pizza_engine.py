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
TOPPING = ("cheese", "pepperoni", "bacon", "sausage")

def get_price(size):
    if size == "small":
        return 8.00
    elif size == "medium":
        return 10.50
    elif size == "large":
        return 12.00
def customer():
    name = input("What is your name? ")
    return name
def size():
    pizza_size = input("What size pizza would you like (small, medium, large): ").lower()
    return pizza_size
def toppings():
    pizza_toppings = input(f"What toppings would you like {TOPPING}")
    return pizza_toppings
def delivery():
    delivery = input("Will this be here or for delivery")
    if delivery == "delivery":
        return delivery
    elif delivery == "here":
        return delivery
    else:
        print("please enter here or delivery")

def make_pizza():

def main():