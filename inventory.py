import json
from utils.clear_screen import Clear_Screen
from utils.get_data import get_data


class Inventory:
    """Add, remove and view inventory."""

    def add_inventory() -> dict:
        """Add items to inventory."""
        item = get_data()

        try:
            add_item = input("Enter item: ")
            quantity = int(input("Enter quantity: "))

            if add_item in item:
                item[add_item] += quantity
            else:
                item[add_item] = quantity

        except ValueError:
            print("Invalid Entry!")

        Clear_Screen()
        with open("inventory.json", "r+") as file:
            json.dump(item, file, indent=4)

    def delete_item() -> dict:
        """Delete items from inventory."""
        item = get_data()

        try:
            if item == {}:
                print("Nothing to delete.\n")
                pass

            else:
                delete = input("Enter item to delete: ")
                item.pop(delete)
                print(f"{delete} deleted!\n")
                with open("inventory.json", "w") as file:
                    json.dump(item, file, indent=4)

        except KeyError as error:
            print(error)

        return item

    def take_items() -> dict:
        """Take items from inventory."""
        item = get_data()
        if item == {}:
            print("No inventory available!\n")

        else:
            try:
                take = input("What did you take? ")
                deduct = int(input(f"How many {take}? "))

                if deduct > item[take]:
                    print(f"Not enough {take} available!\n")
                elif take in item:
                    item[take] -= deduct
                    print(f"{item[take]} {take} left.\n")
                    with open("inventory.json", "w") as file:
                        json.dump(item, file, indent=4)
                else:
                    print(f"{take} doesn't exist.\n")

            except ValueError:
                print("Invalid entry!\n")

        return item

    def view_items() -> None:
        """View items from inventory."""
        view_items = get_data()
        if view_items == {}:
            print("No inventory available!\n")

        else:
            for item, view in view_items.items():
                if int(view) < 1:
                    print("No inventory available!\n")
                else:
                    print(f'{item} = {view}')
            print('\n')
