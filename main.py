#!/usr/bin/env python3
"""
Author: M. McConnaughey
Inventory Version 3.1
Date: 03/15/2023
Python 3.11
"""

from inventory import Inventory
from utils.menu import Menu
from utils.clear_screen import clear_screen
from utils.make_json_file import JsonFile
from utils.get_data import get_data


def main():
    """Main function."""
    JsonFile.check_inventory_file()
    get_data()

    while True:
        option_dict = {
            "1": Inventory.add_inventory,
            "2": Inventory.take_items,
            "3": Inventory.view_items,
            "4": Inventory.delete_item,
            "5": exit
        }

        try:
            option_dict[Menu.list_choices()]()
        except KeyError:
            print("Invalid entry!\n")

if __name__ == "__main__":
    clear_screen()
    main()
