import utils
from application.image_processor import ImageProcessor


def process_input(user_input: str) -> None:
    ImageProcessor(user_input).process_input()
    return


def start():
    print('Please provide an image URL(s) or a directory path to an image(s). If submitting '
          'multiple URLs, separate them with a comma and a space (i.e, ", ").\n(You may quit the application at '
          'anytime by entering "q" or "quit")')
    user_input: str = input('\n> ')

    if utils.quitting(user_input):
        utils.end()
        return

    process_input(user_input)

    prompt_again()


def prompt_again() -> None:
    print('\nWould you like to provide more images? (y/n)')
    user_input = input('\n> ')

    if user_input.lower() in ['y', 'yes']:
        utils.clear()
        start()

    utils.end()
