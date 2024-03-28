import os

import requests
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

import utils
from models import blip_image as bi


class ImageProcessor(object):
    """
    This class enforces a singleton structure. This is because only *one* instance of ImageProcessor is needed when the
    application is in use.
    """

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ImageProcessor, cls).__new__(ImageProcessor)
            cls.__instance.urls = []
            cls.__instance.path = utils.create_dir()
        return cls.__instance

    def __convert_input(self, user_input: str) -> list[tuple[Image, str]]:
        """
        This method converts the URL to an image if it is a valid image link. Otherwise, it converts the given file
        directory.
        :return: Pillow Image type
        """

        # Do not delete this line; used for creating the image
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        utils.clear()

        print('Checking input...')

        if utils.is_url(user_input):
            return [(Image.open(requests.get(img_source, stream=True).raw).convert('RGB'), img_source) if
                    bi.valid_extension(img_source) else bi.invalid_msg(img_source) for img_source in self.urls]

        if utils.is_dir(user_input):
            # return a list of tuple of (Image, directory)
            return [(Image.open(os.path.join(user_input, img_source)).convert("RGB"),
                     os.path.join(user_input, os.path.basename(img_source))) if bi.valid_extension(img_source) else
                    bi.invalid_msg(img_source) for img_source in os.listdir(user_input)]

    def process_input(self, user_input: str) -> bool:
        """
        This method will use the user's input to call the pre-trained model and provide the output. True or False is
        returned to resemble a successful output.
        :return: True or False
        """

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        # Receive the given input as a Pillow Image object and the given source
        images: list[tuple[Image, str]] | None = self.__convert_input(user_input)

        try:
            # clean the input of any bad files
            images = bi.prune(images)
        except TypeError:
            return False

        print('\nProcessing...')

        for img, img_source in images:
            print()  # to space the captions generated in the terminal

            bi.caption_image(img, img_source, processor, model)
            bi.break_line()

        return True
