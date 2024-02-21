import requests
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import utils
import re


class ImageProcessor:
    def __init__(self, user_input: str):
        self.user_input: str = user_input

    def convert_input(self) -> Image:
        """
        This method converts the URL to an image if it is a valid image link. Otherwise, it converts the given file
        directory.
        :return: Pillow Image type
        """

        # Do not delete this line; used for creating the image
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        if self.is_url():
            self.clean_url()
            return Image.open(requests.get(self.user_input, stream=True).raw).convert('RGB')

        return Image.open(self.user_input).convert("RGB")

    def process_image(self) -> None:
        """
        This method will use the user's input to call the pre-trained model and provide the output.
        :return: None
        """

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        img = self.convert_input()

        # Conditional image captioning
        text = "a photo of"
        inputs = processor(img, text, return_tensors="pt")

        out = model.generate(**inputs)
        print(processor.decode(out[0], skip_special_tokens=True))

        # Unconditional image captioning
        inputs = processor(images=img, return_tensors="pt")

        out = model.generate(**inputs)
        print(processor.decode(out[0], skip_special_tokens=True))

    def valid_extension(self) -> bool:
        """
        This method will check if the user's input contains a valid file extension.
        :return: True or False
        """

        # reverse the string, get the file extension, and then re-reverse the string
        extension: str = self.user_input[::-1].split('.')[0][::-1]

        # check if the file extension is valid
        return extension in ['jpeg', 'jpg', 'png', 'tiff', 'raw', 'webp']

    def validate_file_extension(self) -> None:
        """
        This method will check if the user's input is valid. If not, it will prompt the user again to enter a URL or
        file directory to an image.
        :return: None
        """

        valid: bool = self.valid_extension()

        while not valid:
            utils.clear_terminal()
            print('Invalid file extension. Please provide a valid file extension.')
            self.user_input: str = input('Provide the new image url/directory? Press "Q" to quit.\n> ')
            if self.user_input.lower() in ['q', 'quit']:
                break

        if not valid:
            utils.clear_terminal()
            return

        self.process_image()

    def is_url(self) -> bool:
        """
        This method checks if the user's input is a valid URL.
        :return: True or False
        """
        regex = (r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s("
                 r")<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))")
        urls: list[str] = re.findall(regex, self.user_input)

        if len(urls) == 0:
            return False

        # add code to handle when multiple links are provided at once

        return True

    def clean_url(self) -> None:
        """
        If the given URL contains 'www,' add 'https://' to the beginning of the string so the model recognizes it.
        :return: None
        """
        if self.user_input[0:3] == 'www':
            self.user_input = 'https://' + self.user_input
