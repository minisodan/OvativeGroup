import requests
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


class ImageProcessor:
    def __init__(self, url, dir):
        self.url = url
        self.dir = dir

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        if not isinstance(url, str):
            raise ValueError(f'{self.__class__.__name__}.url must be a string. Passed in type {type(url)}')
        self.__url = url

    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        if not isinstance(dir, str):
            raise ValueError(f'{self.__class__.__name__}.dir must be string. Passed in type {type(dir)}')
        self.__dir = dir

    def process_image(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        raw_image = Image.open('C:/Users/ianth/Downloads/coca-cola-ad.jpg').convert("RGB")

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'
        # raw_image = Image.open(requests.get(filename, stream=True).raw).convert('RGB')
        # Conditional image captioning
        text = "a photography of"
        inputs = processor(raw_image, text, return_tensors="pt")

        out = model.generate(**inputs)
        print(processor.decode(out[0], skip_special_tokens=True))

        # Unconditional image captioning
        inputs = processor(images=raw_image, return_tensors="pt")

        out = model.generate(**inputs)
        print(processor.decode(out[0], skip_special_tokens=True))
