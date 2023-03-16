import os
import sys


def clear_screen() -> None:
    """Clear the screen."""
    if sys.platform in "win32":
        os.system("cls")
    else:
        os.system("clear")
