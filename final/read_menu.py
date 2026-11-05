import datetime
import os


def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")


def read_menu():
    menus = {}
    try:
        with open("final\\menu.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
        print(f"Menus: {menus}")
        return menus
    except FileNotFoundError:
        print("Please create the file or check the file name.")
    except IndexError:
        return menus
    except Exception as e:
        right_now = datetime.datetime.now()
        with open("error_log.txt", "a") as f:
            f.write(f"{right_now}, e")
        print(e)


def split_into_variables(menu_items):
    toppings = menu_items.get("TOPPINGS")
    sizes = menu_items.get("SIZES")
    prices = menu_items.get("PRICE")
    mixed = menu_items.get("MIXED")
    flavors = menu_items.get("FLAVORS")
    return (toppings, sizes, prices, mixed, flavors)


def print_toppings(toppings):
    """This section deliberately incomplete"""
    print("Toppings\n")
    count = 1
    toppings_item = toppings.split(",")
    for item in toppings_item:
        print(f"{count}.   \t{item.strip()}")
        count += 1


def print_sizes(sizes, prices):
    print("Sizes\n")
    count = 1
    sizes_item = sizes.split(",")
    prices_item = prices.split(",")
    for item in range(0, len(sizes_item)):
        print(
            f"{count}.  Size: {sizes_item[item]}          price:    ${prices_item[item]}"
        )
        count += 1


def print_mixed(mixed):
    print("Mixed\n")
    count = 1
    mixed_item = mixed.split(", ")
    for item in mixed_item:
        print(f"{count}.   \t{item.strip()}")
        count += 1


def print_flavors(flavors):
    print("Flavors\n")
    count = 1
    flavors_item = flavors.split(", ")
    for item in flavors_item:
        print(f"{count}.   \t{item.strip()}")
        count += 1


def main():
    menu_items = read_menu()
    toppings, sizes, prices, mixed, flavors = split_into_variables(menu_items)
    print_toppings(toppings)
    print_sizes(sizes, prices)
    print_mixed(mixed)
    print_flavors(flavors)


main()
