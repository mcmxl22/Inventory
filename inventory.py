import json
from utils.clear_screen import clear_screen
from utils.get_data import get_data

class Inventory:
    """Add, remove and view inventory."""

    def write_to_file(inventory_item):
        """Write to file."""
        with open("inventory.json", "w") as file:
            json.dump(inventory_item, file, indent=4)

    def check_available_inventory():
        inventory_item = get_data()
        if not inventory_item:
            print("No inventory available!\n")

    def add_inventory() -> dict:
        """Add items to inventory."""
        clear_screen()
        inventory_item = get_data()
        add_item = input("Enter item: ").strip()
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid Entry!")
            return inventory_item

        if add_item in inventory_item:
            inventory_item[add_item] += quantity
        else:
            inventory_item[add_item] = quantity

        #clear_screen()
        print(f"{add_item} added to inventory.\n")
        Inventory.write_to_file(inventory_item)
        return inventory_item

    def delete_item() -> dict:
        """Delete items from inventory."""
        clear_screen()
        inventory_item = get_data()
        if not inventory_item:
            print("Nothing to delete.\n")
            return inventory_item

        delete = input("Enter item to delete: ").strip()
        if delete not in inventory_item:
            print(f"{delete} does not exist in the inventory.\n")
            return inventory_item

        inventory_item.pop(delete)
        print(f"{delete} deleted!\n")
        Inventory.write_to_file(inventory_item)
        return inventory_item

    def take_items() -> dict:
        """Take items from inventory."""
        clear_screen()
        inventory_item = get_data()
        if not inventory_item:
            print("No inventory available!\n")
            return inventory_item

        take = input("What did you take? ").strip()
        if take not in inventory_item:
            print(f"{take} does not exist in the inventory.\n")
            return inventory_item

        try:
            take_quantity = int(input(f"How many {take}? "))
        except ValueError:
            print("Invalid entry!\n")
            return inventory_item

        if take_quantity > inventory_item[take]:
            print(f"Not enough {take} available!\n")
            return inventory_item

        inventory_item[take] -= take_quantity
        print(f"{inventory_item[take]} {take} left.\n")
        Inventory.write_to_file(inventory_item)
        return inventory_item

    def view_items() -> None:
        """View items from inventory."""
        clear_screen()
        view_items = get_data()
        if not view_items:
            print("No inventory available!\n")
            return

        for item, view in view_items.items():
            print(f'{item} = {view}')
        print('\n')
