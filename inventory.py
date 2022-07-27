#!/usr/bin/env python3
"""
Author: M. McConnaughey
Inventory Version 2.8
Date: 07/26/2022
Python 3.7
"""


import json
from os import path, system
from sys import platform


def clear_screen() -> None:
    """Clear the screen."""
    if platform in "win32":
        system("cls")

    else:
        system("clear")


def get_data() -> dict:
    """Get Json data from file."""
    with open("inventory.json", "r+") as file:
        try:
            existing_items = json.load(file)

        except ValueError:
            existing_items = {}
            json.dump(existing_items, file, indent=4)

    return existing_items


class Inventory_file:
    """Check and/or create inventory file."""

    def create_inventory_file() -> None:
        """Create file"""
        with open("inventory.json", "w+"):
            if path.exists("inventory.json"):
                print(f"inventory.json created!")
            else:
                return

    def check_inventory_file() -> None:
        """Check if file exists"""
        if path.exists("inventory.json"):
            pass
        else:
            Inventory_file.create_inventory_file()


class Menu:
    """Prepare a menu."""

    def add_numbers(num) -> None:
        """Add numbers to menu list."""
        for c, value in enumerate(num, 1):
            print(c, value)

    def list_choices() -> list:
        """Give user a choice of actions."""
        inventory_actions = ["Add", "Take", "View", "Delete", "Exit"]
        Menu.add_numbers(inventory_actions)
        action_choice = input("What do you want to do? ")
        return action_choice


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

        clear_screen()
        with open("inventory.json", "r+") as file:
            json.dump(item, file, indent=4)

    def delete_item() -> dict:
        """Delete items from inventory."""
        item = get_data()

        try:
            if item == {}:
                print("Nothing to delete.")
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
                if view < 1:
                    print("No inventory available!\n")
                else:
                    print(f'{item} = {view}')
            print('\n')


def main():
    """main function"""
    while True:
        Inventory_file.check_inventory_file()
        choice = Menu.list_choices()

        option_dict = {
            "1": Inventory.add_inventory,
            "2": Inventory.take_items,
            "3": Inventory.view_items,
            "4": Inventory.delete_item,
            "5": exit,
        }

        try:
            clear_screen()
            option_dict[choice]()

        except KeyError:
            print("Invalid entry!\n")


if __name__ == "__main__":
    clear_screen()
    main()
