from utils.write_to_file import Write
from utils.clear_screen import clear_screen
from utils.get_data import get_data


class Inventory:
    """Add, remove and view inventory."""
    def check_available_inventory():
        item = get_data()
        if not item:
            print("No inventory available!\n")

    def add_inventory() -> dict:
        """Add items to inventory."""
        clear_screen()
        item = get_data()
        add_item = input("Enter item: ").strip()
        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid Entry!")
            return item

        if add_item in item:
            item[add_item] += quantity
        else:
            item[add_item] = quantity

        print(f"{add_item} added to inventory.\n")
        Write.write_to_file(item)
        return item

    def delete_item() -> dict:
        """Delete items from inventory."""
        clear_screen()
        item = get_data()
        if not item:
            print("Nothing to delete.\n")
            return item

        delete = input("Enter item to delete: ").strip()
        if delete not in item:
            print(f"{delete} does not exist in the inventory.\n")
            return item

        item.pop(delete)
        print(f"{delete} deleted!\n")
        Write.write_to_file(item)
        return item

    def take_items() -> dict:
        """Take items from inventory."""
        clear_screen()
        item = get_data()
        if not item:
            print("No inventory available!\n")
            return item

        take = input("What did you take? ").strip()
        if take not in item:
            print(f"{take} does not exist in the inventory.\n")
            return item

        try:
            take_quantity = int(input(f"How many {take}? "))
        except ValueError:
            print("Invalid entry!\n")
            return item

        if take_quantity > item[take]:
            print(f"Not enough {take} available!\n")
            return item

        item[take] -= take_quantity
        print(f"{item[take]} {take} left.\n")
        Write.write_to_file(item)
        return item

    def view_items() -> None:
        """View items from inventory."""
        clear_screen()
        view_items = get_data()
        if not view_items:
            print("No inventory available!\n")
            return

        for items, view in view_items.items():
            print(f'{items} = {view}\n')
