import json

class Write:    

    def write_to_file(item) -> None:
        """Write to file."""
        with open("inventory.json", "w") as f:
            json.dump(item, f, indent=4)
