import threading

from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

from models import blip_image as bi


class BlipImageThread(threading.Thread):
    """
     A class for the BLIP Image Thread to implement multithreading: The purpose of this
     class is to return an instance variable of each model's/LLM's  respective threads that can
     be used/accessed for output
    """

    # constructor
    def __init__(self, img: Image):
        # execute the base constructor
        threading.Thread.__init__(self)

        self.captions: tuple[str, str] = ('', '')
        self.image: Image = img
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    @property
    def captions(self) -> tuple[str, str]:
        # return the captions
        return self.__captions

    @captions.setter
    def captions(self, captions: tuple[str, str]) -> None:
        # check if the passed in variable is a tuple
        if captions is None or not isinstance(captions, tuple):
            raise ValueError(f'{self.__class__.__name__}.captions must be a tuple. The passed in value is of type '
                             f'{type(captions)}')

        # check if every item in the tuple is a string
        if not any(isinstance(caption, str) for caption in captions):
            raise ValueError(f'{self.__class__.__name__}.captions must be a tuple of strings. The passed in value '
                             f'was {captions}')

        self.__captions = captions

    @property
    def image(self) -> Image:
        # return the image that is processed from the model
        return self.__image

    @image.setter
    def image(self, img: Image) -> None:
        if not isinstance(img, Image.Image):
            raise ValueError(f'{self.__class__.__name__}.captions must be an Image object from the Pillow library')
        self.__image = img

    # function to execute Blip Image Thread
    def run(self):
        self.captions = bi.caption_image(self.image, self.processor, self.model)
