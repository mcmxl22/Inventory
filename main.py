#!/usr/bin/env python3
"""
Author: M. McConnaughey
Inventory Version 3
Date: 08/02/2022
Python 3.7
"""


import inventory
import clear_screen
import get_data
import menu
import make_jason_file


def main():
    """main function"""
    while True:
        make_jason_file.Json_file.check_inventory_file()
        choice = menu.Menu.list_choices()

        option_dict = {
            "1": inventory.Inventory.add_inventory,
            "2": inventory.Inventory.take_items,
            "3": inventory.Inventory.view_items,
            "4": inventory.Inventory.delete_item,
            "5": exit,
        }

        try:
            clear_screen.Clear_Screen()
            get_data.get_data()
            option_dict[choice]()

        except KeyError:
            print("Invalid entry!\n")


if __name__ == "__main__":
    clear_screen.Clear_Screen()
    main()
