import requests
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# print('What is the url of the image?')
# filename = input()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
raw_image = Image.open('C:/Users/emand/Downloads/ad3.jpg').convert("RGB")

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
