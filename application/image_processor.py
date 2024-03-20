import os

import requests
import torch
import validators
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

import utils
from models import blip_image as bi


class ImageProcessor:
    def __init__(self, user_input: str):
        self.user_input: str = user_input
        self.urls: list[str] = []
        self.path: str = bi.create_dir()

    def convert_input(self) -> list[tuple[Image, str]]:
        """
        This method converts the URL to an image if it is a valid image link. Otherwise, it converts the given file
        directory.
        :return: Pillow Image type
        """

        # Do not delete this line; used for creating the image
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        utils.clear()

        print('Checking input...')

        if self.is_url():
            return [(Image.open(requests.get(img_source, stream=True).raw).convert('RGB'), img_source) if
                    bi.valid_extension(img_source) else bi.invalid_msg(img_source) for img_source in self.urls]

        if self.is_dir():
            # return a list of tuple of (Image, directory)
            return [(Image.open(os.path.join(self.user_input, img_source)).convert("RGB"),
                     os.path.join(self.user_input, os.path.basename(img_source))) if bi.valid_extension(img_source) else
                    bi.invalid_msg(img_source) for img_source in os.listdir(self.user_input)]

    def process_input(self) -> None:
        """
        This method will use the user's input to call the pre-trained model and provide the output.
        :return: None
        """

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        # Receive the given input as a Pillow Image object and the given source
        images: list[tuple[Image, str]] | None = self.convert_input()

        try:
            # clean the input of any bad files
            images = bi.prune(images)
        except TypeError:
            self.invalid_prompt()

        print('\nProcessing...')

        for img, img_source in images:
            print()  # to space the captions generated in the terminal

            bi.caption_image(img, img_source, processor, model)
            bi.break_line()

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
        """
        If the user input is completely invalid, prompt the user again to provide proper input.
        :return:
        """
        utils.clear()
        print(f'Invalid input, "{self.user_input}", was given. Please provide an image URL(s) or an existing directory '
              f'to multiple images.')
        self.user_input = input('\n> ')

        if not utils.quitting(self.user_input):
            self.process_input()
