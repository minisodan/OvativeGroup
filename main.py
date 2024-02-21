import requests
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from image_processor import ImageProcessor


class ImageCaptionGenerator:
    def __init__(self):
        self.using_url: bool = False
        self.using_dir: bool = False
        self.img_url: str = ''
        self.dir_path: str = ''
        self.image_processor: ImageProcessor

    def get_input(self):
        user_input: str = input('Will you use an image URL or a file directory? (url/dir)\n> ')
        self.process_input(user_input)

    def process_input(self, user_input: str) -> None:
        self.using_url = True if user_input.__contains__('u') else False
        self.using_dir = True if user_input.__contains__('d') else False

        if self.using_url or self.using_dir:
            image_processing = ImageProcessor(self.img_url, self.dir_path)
            image_processing.process_image()
            return

        print('Please provide proper input (url, URL, u; dir, d, directory)')
        self.get_input()


if __name__ == '__main__':
    print('Welcome to the Ovative Group Image Caption Generator!', end='\n\n')
    image_caption_generator = ImageCaptionGenerator()
    image_caption_generator.get_input()
