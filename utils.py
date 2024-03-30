import os
import sys
import validators

"""
Utility functions used for the application. Helps to abstract some functions from the other files.
"""

__VALID_EXTENSIONS = ['jpeg', 'jpg', 'png', 'tiff', 'raw', 'webp']


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def quitting(user_input: str) -> bool:
    return user_input.lower() in ['q', 'quit']


def end() -> None:
    clear()
    print('Ending program.')
    sys.exit()


def is_dir(directory: str) -> bool:
    """
    Checks if the given value is an existing, local directory.

    :param directory: possible directory path
    :return: True if value is an existing directory, False otherwise
    """
    return os.path.exists(directory)


def is_url(image_url: str) -> bool:
    """
    Checks if the given value is a valid URL.

    :param image_url: url of the given image.
    :return:
    """
    return validators.url(image_url)


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


def validate_and_add_url(img_source: str, image_sources: list[str]) -> None:
    """
    Check if the user's input contains a valid file extension via :func:`is_valid_extension`
    and extend the images into the list being passed in.

    :param image_sources: a list of sources that will be added to if the img_source is valid
    :param img_source: String representing the url of the image.
    :return: none
    """

    extension: str = img_source[::-1].split('.')[0][::-1]

    # check if the file extension is valid
    if is_valid_extension(extension):
        image_sources.append(img_source)
    else:
        print(f'Invalid image URL with extension "{extension}" was found in  "{img_source}". This will not be '
              f'processed. Valid extensions are: {__VALID_EXTENSIONS}')


def validate_and_add_files(directory: str, image_sources: list[str]) -> None:
    """
    Each file in the given directory is validated to see if the model can use it. If so, its absolute path is written
    to the
    :param directory: Path of the directory with image files to be validated
    :param image_sources: A list that contains all sources for images (urls or filenames)
    :return:
    """

    # used to send a warning message to the user
    success: bool = False

    for file_name in os.listdir(directory):
        # get the file extension by splitting the file name and accessing the extension past the "."
        extension: str = os.path.splitext(file_name)[1].split('.')[1]

        if extension not in __VALID_EXTENSIONS:
            return

        file_path = os.path.join(directory, file_name)
        image_sources.append(file_path)

        print(image_sources)

        success = True

    if not success:
        print(f'Invalid image source in directory: "{directory}" was given. This will not be processed.')


def is_valid_extension(img_source: str) -> bool:
    """
     Checks if the user's input contains a valid file extension in the given string
     :param img_source: source of the given image with file extension.
     :return: none
     """

    # reverse the string, get the backwards file extension, and then re-reverse the extension back to normal and
    # check if the extension is in list of valid extensions.
    extension: str = img_source[::-1].split('.')[0][::-1]

    valid: bool = extension in __VALID_EXTENSIONS

    return valid


def filter_and_validate(image_sources: list[str]) -> list[str]:
    results: list[str] = []

    for image_source in image_sources:
        if is_url(image_source):
            validate_and_add_url(image_source, results)
        elif os.path.isdir(image_source):
            validate_and_add_files(image_source, results)
        else:
            print(f'{image_source} is not a valid input. This will not be processed.')
    return results
