import os
import sys


def Clear_Screen() -> None:
    """Clear the screen."""
    if sys.platform in "win32":
        os.system("cls")

    else:
        os.system("clear")
