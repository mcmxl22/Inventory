#!/usr/bin/env python3
"""
Author: M. McConnaughey
Inventory Version 3
Date: 08/03/2022
Python 3.7
"""


from inventory import Inventory
from utils.clear_screen import Clear_Screen
from utils.get_data import get_data
from utils.menu import Menu
from utils.make_jason_file import Json_file


def main():
    """main function"""
    while True:
        Json_file.check_inventory_file()
        choice = Menu.list_choices()

        option_dict = {
            "1": Inventory.add_inventory,
            "2": Inventory.take_items,
            "3": Inventory.view_items,
            "4": Inventory.delete_item,
            "5": exit,
        }

        try:
            Clear_Screen()
            get_data()
            option_dict[choice]()

        except KeyError:
            print("Invalid entry!\n")


if __name__ == "__main__":
    Clear_Screen()
    main()
