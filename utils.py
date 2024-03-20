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


def is_dir(user_input: str) -> bool:
    """
    This method checks if the user's input is an existing, local directory.
    :return: True or False
    """

    return os.path.exists(user_input)


def clean_url(user_input: str) -> str:
    """
    If the given URL contains 'www,' add 'https://' to the beginning of the string so the model recognizes it.
    :return: None
    """

    if user_input[0:3] == 'www':
        return 'https://' + user_input


def create_dir() -> str:
    """
    Creates the directory the inputs will be stored in and return that directory string.
    :return: string representing the created folder directory
    """

    # User's directory (e.g., C:/Users/example_user_name/)
    parent_dir: str = os.path.join(os.path.expanduser('~'), 'Desktop')
    directory: str = 'Ovative Group Caption Generator'
    path: str = os.path.join(parent_dir, directory)

    if not os.path.exists(path):
        clear()
        os.makedirs(path)  # make directory if it doesn't exist already
        print(f'Created new directory, "{path}", to store generated captions.\n')

    return path
