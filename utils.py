import os
import sys
import validators

"""
Utility functions used for the application. Helps to abstract some functions from the other files.
"""


def clear():
    """
    This will clear the terminal of any previously printed output.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def quitting(given_input: str) -> bool:
    return given_input.lower() in ['q', 'quit']


def end() -> None:
    clear()
    print('Ending program.')
    sys.exit()


def is_dir(given_input: str) -> bool:
    """
    This method checks if the user's input is an existing, local directory.
    :return: True or False
    """

    return os.path.exists(given_input)


def is_url(given_input: str) -> bool:
    """
    This method checks if the user's input contains a valid URL(s). Many URL may be given at a time.
    :return: True or False
    """

    urls: list[str] = given_input.split(', ')

    valid: bool = True

    for url in urls:
        if not validators.url(url):
            valid = False
            break

    return valid


def invalid_msg(given_input: str) -> None:
    """
    If the user input is completely invalid, prompt the user again to provide proper input.
    :return:
    """
    clear()
    print(f'Invalid input, "{given_input}", was given.')


def clean_url(given_input: str) -> str:
    """
    If the given URL contains 'www,' add 'https://' to the beginning of the string so the model recognizes it.
    :return: None
    """

    if given_input[0:3] == 'www':
        return 'https://' + given_input


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


def user_input(given_input: str) -> str:
    return given_input
