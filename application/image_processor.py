import datetime
import os

import requests
import torch
import validators
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

import utils


def caption_image(img: Image, img_source: str, processor, model) -> None:
    # Conditional image captioning
    text = "a photo of"
    inputs = processor(img, text, return_tensors="pt")

    out = model.generate(**inputs, max_length=60)
    con_caption: str = 'Conditional image caption: ' + processor.decode(out[0], skip_special_tokens=True)
    print(con_caption)

    # Unconditional image captioning
    inputs = processor(images=img, return_tensors="pt")

    out = model.generate(**inputs, max_length=60)
    unc_caption: str = 'Unconditional image caption: ' + processor.decode(out[0], skip_special_tokens=True)
    print(unc_caption, end='\n\n')

    store_image(img_source, con_caption, unc_caption)


def store_image(img_source: str, con_caption: str, unc_caption: str) -> None:
    """
    Stores the given captions of the given image in a file. Creates a new folder if it doesn't exist.
    :param img_source: The URL or directory path that sourced the image
    :param con_caption: Conditional caption
    :param unc_caption: Unconditional caption
    :return: None
    """
    parent_dir: str = os.path.expanduser('~') + '\\Desktop'  # User's directory (e.g., C:/Users/example_user_name/)
    directory: str = 'Ovative Group Caption Generator'
    path: str = os.path.join(parent_dir, directory)

    try:
        os.makedirs(path)  # make directory if it doesn't exist already
        print(f'Created new directory, "{path}", to store generated captions.\n')
    except OSError:
        print(f'Directory "{path}" already exists. Creating file to store generated captions...\n')

    now: datetime = datetime.datetime.now()
    file_name: str = now.strftime("%Y-%m-%d %H-%M-%S")

    with open(path + '\\' + file_name + '.txt', 'a') as file:
        file.write(f'Image source: {img_source}\n'
                   f'{con_caption}\n'
                   f'{unc_caption}\n\n')
        print(f'Stored output in "{path}\\' + file_name + '.txt"\n')


class ImageProcessor:
    def __init__(self, user_input: str):
        self.user_input: str = user_input
        self.urls: list[str] = []

    def convert_input(self) -> list[tuple[Image, str]] | None:
        """
        This method converts the URL to an image if it is a valid image link. Otherwise, it converts the given file
        directory.
        :return: Pillow Image type
        """

        # Do not delete this line; used for creating the image
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        print('\nChecking input...')

        if self.is_url():
            self.clean_url()

            # return a list of tuple of (Image, URL)
            return [(Image.open(requests.get(url, stream=True).raw).convert('RGB'), url) for url in self.urls]

        if self.is_dir():
            # return a list of tuple of (Image, directory)
            return [(Image.open(self.user_input).convert("RGB"), self.user_input)]

    def process_input(self) -> None:
        """
        This method will use the user's input to call the pre-trained model and provide the output.
        :return: None
        """

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        # Receive the given input as a Pillow Image object
        images: list[tuple[Image, str]] | None = self.convert_input()

        if images is None:
            self.invalid_prompt()
            return

        print('\nValid input received. Processing image(s)...')
        utils.clear()

        for img, img_source in images:
            print()  # to space the captions generated in the terminal

            try:
                caption_image(img, img_source, processor, model)
            except Exception as e:
                print(e)
                print('An error occurred while processing an image. Please try again.\n')

    def valid_extension(self) -> bool:
        """
        This method will check if the user's input contains a valid file extension.
        :return: True or False
        """

        # reverse the string, get the file extension, and then re-reverse the string
        extension: str = self.user_input[::-1].split('.')[0][::-1]

        # check if the file extension is valid
        return extension in ['jpeg', 'jpg', 'png', 'tiff', 'raw', 'webp', ]

    def validate_file_extension(self) -> None:
        """
        This method will check if the user's input contains a valid file extension. If not, it will prompt the user
        again to enter a URL or file directory to an image.
        :return: None
        """

        valid: bool = self.valid_extension()

        while not valid:
            utils.clear()
            print(f'Invalid file extension, "{self.user_input}", was given. Please provide input containing a valid '
                  f'file extension (jpeg, jpg, png, tiff, raw, webp).')
            self.user_input = input('Please provide the new image url/directory. Press "Q" to quit.\n> ')

            # end application if quitting
            if utils.quitting(self.user_input):
                utils.end()

            valid: bool = self.valid_extension()

        self.process_input()

    def is_url(self) -> bool:
        """
        This method checks if the user's input contains a valid URL(s). Many URL may be given at a time.
        :return: True or False
        """

        self.urls: list[str] = self.user_input.split(', ')

        valid: bool = True

        for url in self.urls:
            if not validators.url(url):
                valid = False
                break

        return valid

    def is_dir(self) -> bool:
        """
        This method checks if the user's input is an existing, local directory.
        :return: True or False
        """

        return os.path.exists(self.user_input)

    def clean_url(self) -> None:
        """
        If the given URL contains 'www,' add 'https://' to the beginning of the string so the model recognizes it.
        :return: None
        """

        if self.user_input[0:3] == 'www':
            self.user_input = 'https://' + self.user_input

    def invalid_prompt(self) -> None:
        utils.clear()
        print(f'Invalid input, "{self.user_input}", was given. Please provide an image URL or an existing directory.')
        self.user_input = input('> ')

        if not utils.quitting(self.user_input):
            self.process_input()

        utils.end()
