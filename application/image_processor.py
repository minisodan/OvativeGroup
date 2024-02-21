import requests
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


class ImageProcessor:
    def __init__(self, using_url: bool):
        self.using_url = using_url

    @property
    def using_url(self):
        return self.__using_url

    @using_url.setter
    def using_url(self, using_url: bool):
        if not isinstance(using_url, bool):
            raise ValueError(f'{self.__class__.__name__}.using_url must be a bol. Passed in type {type(using_url)}')
        self.__using_url = using_url

    def process_image(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        img_url = (Image.open(requests.get(
            'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg', stream=True).raw).
                   convert('RGB'))

        img = img_url if self.using_url else Image.open('C:/Users/ianth/Downloads/coca-cola-ad.jpg').convert("RGB")

        # raw_image = Image.open('C:/Users/ianth/Downloads/coca-cola-ad.jpg').convert("RGB")

        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        # Conditional image captioning
        text = "a photography of"
        inputs = processor(img, text, return_tensors="pt")

        out = model.generate(**inputs)
        print(processor.decode(out[0], skip_special_tokens=True))

        # Unconditional image captioning
        inputs = processor(images=img, return_tensors="pt")

        out = model.generate(**inputs)
        print(processor.decode(out[0], skip_special_tokens=True))
