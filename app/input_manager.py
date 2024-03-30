import utils
from app.image_processor import ImageProcessor


"""
This file is used to start the application. The start method is used in the runner.py file, which will ask the user for 
input once started.
"""

processor: ImageProcessor = ImageProcessor()


def process_input(user_input: list) -> None:
    processor.process_input(user_input)
    return


def start():
    utils.clear()  # clear terminal for fresh start
    print('Please provide an image URL(s) or a directory path to an image(s). If submitting '
          'multiple URLs, separate them with a comma and a space (i.e, ",").\n(You may quit the application at '
          'anytime by entering "q" or "quit")')
    user_input: str = input('\n> ')  # collect user input

    inputs: list = [x.strip() for x in user_input.split(',')]  # split the input into a list using a comma as a delimiter

    while len(inputs) != 0:
        if utils.quitting(user_input):
            utils.end()
            return

        process_input(inputs)

        inputs.clear()  # clearing elements to reprompt users to possibly provide more images to keep the while loop
        reprompt(inputs)


def reprompt(inputs: list[str]) -> None:
    if len(inputs) == 0:
        print('\nWould you like to provide more images? (y/n)')
        user_input = input('\n> ')

        if user_input.lower() in ['n', 'no', 'q', 'quit']:
            utils.end()

        utils.clear()
        print('Please provide an image URL(s) or a directory path to an image(s). If submitting '
              'multiple URLs, separate them with a comma and a space (i.e, ",").\n(You may quit the application at '
              'anytime by entering "q" or "quit")')

        user_input: str = input('\n> ')  # collect user input

        if utils.quitting(user_input):
            utils.end()

        inputs += [x.strip() for x in user_input.split(',')]