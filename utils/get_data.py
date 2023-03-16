import json


def get_data() -> dict:
    """Get Json data from file."""
    with open("inventory.json", "r+") as f:
        try:
            existing_items = json.load(f)

        except ValueError:
            existing_items = {}
            json.dump(existing_items, f, indent=4)

    return existing_items
