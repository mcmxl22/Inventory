import json
from utils.clear_screen import Clear_Screen
from utils.get_data import get_data


class Inventory:
    """Add, remove and view inventory."""
    
    def write_to_file(inventory_item) -> None:
        """Write to file."""
        with open("inventory.json", "w") as file:
            json.dump(inventory_item, file, indent=4)

    def add_inventory() -> dict:
        """Add items to inventory."""
        inventory_item = get_data()
        try:
            add_item = input("Enter item: ").strip()
            add_quantity = int(input("Enter quantity: "))
            if add_item in inventory_item:
                inventory_item[add_item] += add_quantity
                print(f"{add_item} added to inventory.\n")
            else:
                inventory_item[add_item] = add_quantity
        except ValueError:
            print("Invalid Entry!")
        Clear_Screen()
        print(f"{add_item} added to inventory.")
        Inventory.write_to_file(inventory_item)

    def delete_item() -> dict:
        """Delete items from inventory."""
        inventory_item = get_data()
        try:
            if inventory_item == {}:
                print("Nothing to delete.\n")
            else:
                delete = input("Enter item to delete: ").strip()
                inventory_item.pop(delete)
                print(f"{delete} deleted!\n")
                Inventory.write_to_file(inventory_item)
        except KeyError as error:
            print(error)
        return inventory_item

    def take_items() -> dict:
        """Take items from inventory."""
        inventory_item = get_data()
        if inventory_item == {}:
            print("No inventory available!\n")
        else:
            try:
                take = input("What did you take? ").strip()
                take_quantity = int(input(f"How many {take}? "))
                if take_quantity > inventory_item[take]:
                    print(f"Not enough {take} available!\n")
                elif take in inventory_item:
                    inventory_item[take] -= take_quantity
                    print(f"{inventory_item[take]} {take} left.\n")
                    Inventory.write_to_file(inventory_item)
                else:
                    print(f"{take} doesn't exist.\n")
            except ValueError:
                print("Invalid entry!\n")
        return inventory_item

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
