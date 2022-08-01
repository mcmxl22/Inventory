import json


def get_data() -> dict:
    """Get Json data from file."""
    with open("inventory.json", "r+") as file:
        try:
            existing_items = json.load(file)

        except ValueError:
            existing_items = {}
            json.dump(existing_items, file, indent=4)

    return existing_items
