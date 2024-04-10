import sys
import utils
from app.image_processor import ImageProcessor

"""
This file is used to start the application. The start method is used in the runner.py file, which will ask the user for 
input once started.
"""


def start():
    processor: ImageProcessor = ImageProcessor()
    utils.clear()  # clear terminal for fresh start
    print('Please provide an image URL(s) or a directory path to an image(s). If submitting '
          'multiple URLs, separate them with a comma and a space (i.e, ",").\n(You may quit the application at '
          'anytime by entering "q" or "quit")')
    user_input: str = input('\n> ')  # collect user input

    inputs: list

    if len(user_input) != 0:
        inputs = [x.strip() for x in user_input.split(',')]  # split the input into a list using a comma as a delimiter
    else:
        # an empty input was given
        utils.clear()
        print('Please provide an image URL(s) or a directory to images. The application will terminate. Please try '
              'again.')
        sys.exit()

    # start looping over the given image sources (if applicable)
    while len(inputs) != 0:
        if utils.quitting(user_input):
            utils.end()
            return

        success: bool = processor.process_input(inputs)

        inputs.clear()  # clearing elements to reprompt users to possibly provide more images to keep the while loop
        reprompt(inputs, success)


def reprompt(inputs: list[str], success: bool) -> None:
    """
    Asks the user if they would like to continue using the application. If not, the application terminates.
    :param success: represents a successful completion of the image processing
    :param inputs: list of inputs from the previous cycle of images processed
    :return: None
    """

    msg: str = 'Would you like to provide more images? (y/n)' if success else 'Would you like to try again?'

    if len(inputs) == 0:
        print(f'\n{msg}')
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