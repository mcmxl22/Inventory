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
