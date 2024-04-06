import easyocr
import pandas as pd
from PIL import Image, ImageDraw
import requests
from io import BytesIO
import numpy as np

def download_image(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img


def draw_boxes(image, bounds, color='yellow', width=2):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


def inference(img_source, lang='en'):
    if img_source.startswith('http://') or img_source.startswith('https://'):
        im = download_image(img_source)
    else:
        im = Image.open(img_source)

    reader = easyocr.Reader([lang], gpu=False)
    bounds = reader.readtext(np.array(im))
    draw_boxes(im, bounds)
    df = pd.DataFrame(bounds, columns=['Position', 'Text', 'Confidence'])
    filtered_df = df[df['Confidence'] > 0.3]
    return filtered_df['Text'].tolist()
