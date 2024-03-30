import sys

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
        return cls.__instance

    def __source_to_image_object(self, image_sources: list[str]) -> list[tuple[Image, str]]:
        """
        This method converts the URL to an image if it is a valid image link. Otherwise, it converts the given file
        directory.
        :return: Pillow Image type
        """

        # Do not delete this line; used for creating the image
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        results: list[tuple[Image, str]] = []

        for img_source in image_sources:
            if utils.is_url(img_source):
                results.append((Image.open(requests.get(img_source, stream=True).raw).convert('RGB'), img_source))

            if utils.is_dir(img_source):
                results.append(((Image.open(img_source)).convert("RGB"), img_source))

        return results

    def process_input(self, image_sources: list[str]) -> None:
        utils.clear()
        print('Checking input...\n')
        filtered_input: list[str] = utils.filter_and_validate(image_sources)

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        # Receive the given input as a Pillow Image object and the given source
        images: list[tuple[Image, str]] | None = self.__source_to_image_object(filtered_input)

        if len(images) == 0:
            print('No provided input was valid. Nothing found to process.')
            return

        print('Processing images...')

        for img, img_source in images:
            print()  # to space the captions generated in the terminal

            bi.caption_image(img, img_source, processor, model)
            bi.break_line()