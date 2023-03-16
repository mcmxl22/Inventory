import json

class Write:    

    def write_to_file(inventory_item) -> None:
        """Write to file."""
        with open("inventory.json", "w") as f:
            json.dump(inventory_item, f, indent=4)
