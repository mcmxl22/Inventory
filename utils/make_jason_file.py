import os

class Json_File:
    """Check and/or create inventory file."""

    def create_inventory_file() -> None:
        """Create file"""
        with open("inventory.json", "w+"):
            if os.path.exists("inventory.json"):
                print(f"inventory.json created!")
            else:
                return

    def check_inventory_file() -> None:
        """Check if file exists"""
        if os.path.exists("inventory.json"):
            pass
        else:
            Json_File.create_inventory_file()
