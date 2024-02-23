import utils
from application.image_processor import ImageProcessor


def process_input(user_input: str) -> None:
    image_processing = ImageProcessor(user_input)
    image_processing.validate_file_extension()
    return


def start():
    print('Please provide an image URL(s) or directory path to an individual image. If submitting '
          'multiple URLs, separate them with a comma and a space (i.e, ", ").')
    user_input: str = input('> ')

    if utils.quitting(user_input):
        utils.end()
        return

    process_input(user_input)

    prompt_again()


def prompt_again() -> None:
    print('Would you like to provide more images? (y/n)')
    user_input = input('> ')
    if user_input.lower() in ['y', 'yes']:
        utils.clear()
        start()

    utils.end()
