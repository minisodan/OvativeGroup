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

        utils.clear()

        results: list[tuple[Image, str]] = []

        for img_source in image_sources:
            # append to the results list a tuple of (Image, image_source)

            if utils.is_url(img_source):
                results.append((Image.open(requests.get(img_source, stream=True).raw).convert('RGB'), img_source))
                # return [(Image.open(requests.get(img_source, stream=True).raw).convert('RGB'), img_source) if
                #         bi.valid_extension(img_source) else bi.invalid_msg(img_source) for img_source in self.urls]

            try:
                if utils.is_dir(img_source):
                    results.append(((Image.open(img_source)).convert("RGB"), img_source))
            except PermissionError:
                print(f'The given directory, "{img_source}," is opened and cannot be read. Please close it for it to '
                      f'be usable.\nThe application will terminate. Please run again.')
                sys.exit()
        #
        #     return [(Image.open(os.path.join(user_input, img_source)).convert("RGB"),
        #              os.path.join(user_input, os.path.basename(img_source))) if bi.valid_extension(img_source) else
        #             bi.invalid_msg(img_source) for img_source in os.listdir(user_input)]

        return results

    def process_input(self, image_sources: list[str]) -> None:
        utils.clear()
        print('Checking input...')
        filtered_input: list[str] = utils.filter_and_validate(image_sources)

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        # Receive the given input as a Pillow Image object and the given source
        images: list[tuple[Image, str]] | None = self.__source_to_image_object(filtered_input)

        # remove any potential None values from the list
        # images = bi.prune(images)

        print('Processing images...')

        for img, img_source in images:
            print()  # to space the captions generated in the terminal

            bi.caption_image(img, img_source, processor, model)
            bi.break_line()