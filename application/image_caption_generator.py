from application.image_processor import ImageProcessor


def process_input(user_input: str) -> None:
    image_processing = ImageProcessor(user_input)
    image_processing.validate_file_extension()
    return


def start():
    user_input: str = input('Please provide an image URL(s) or directory path to an individual image. If submitting '
                            'multiple URLs, separate them with a comma and a space (i.e, ", ").\n> ')
    process_input(user_input)
