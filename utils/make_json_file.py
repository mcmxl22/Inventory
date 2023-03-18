from os.path import exists

class JsonFile:
    """Check and/or create inventory file."""

    @staticmethod
    def create_inventory_file() -> None:
        """Create file"""
        with open("inventory.json", "w+") as f:
            print("inventory.json created!")

    @staticmethod
    def check_inventory_file() -> None:
        """Check if file exists"""
        if exists("inventory.json"):
            return
        JsonFile.create_inventory_file()
