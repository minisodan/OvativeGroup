import utils
from app.image_processor import ImageProcessor


"""
This file is used to start the application. The start method is used in the runner.py file, which will ask the user for 
input once started.
"""

processor: ImageProcessor = ImageProcessor()


def process_input(user_input: str) -> None:
    processor.process_input(user_input)
    return


def start():
    while True:
        utils.clear()
        print('Please provide an image URL(s) or a directory path to an image(s). If submitting '
              'multiple URLs, separate them with a comma and a space (i.e, ", ").\n(You may quit the application at '
              'anytime by entering "q" or "quit")')
        user_input: str = input('\n> ')

        if utils.quitting(user_input):
            utils.end()
            return

        process_input(user_input)

        reprompt()


def reprompt() -> None:
    print('\nWould you like to provide more images? (y/n)')
    user_input = input('\n> ')

    if user_input.lower() in ['n', 'no']:
        utils.end()
