import os
import sys


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def quitting(user_input: str) -> bool:
    return user_input.lower() in ['q', 'quit']


def end() -> None:
    clear()
    print('Ending program.')
    sys.exit()
