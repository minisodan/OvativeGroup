import os
import sys

"""
Utility functions used for the application. Helps to abstract some functions from the other files.
"""


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def quitting(user_input: str) -> bool:
    return user_input.lower() in ['q', 'quit']


def end() -> None:
    clear()
    print('Ending program.')
    sys.exit()
