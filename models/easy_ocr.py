import easyocr
import pandas as pd
from PIL import Image, ImageDraw
import requests
from io import BytesIO
import numpy as np


def download_image(image_url: str) -> Image:
    """
    Downloads an into a processable format for the OCR. This code was given from the EasyOCR code
    :param image_url: a string representing the URL to the image
    :return: an Image object created from the URL
    """
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    return img


def draw_boxes(image: Image, bounds, color='yellow', width=2) -> Image:
    """
    Provided code that draws bounding boxes around the text found in the image. This was originally provided by the
    EasyOCR code. It shouldn't be necessary for this project, but is present to ensure the OCR still functions.
    :param image: a Pillow Image object
    :param bounds: a given iterator
    :param color: the color of the boxes to be drawn
    :param width: the width used for drawing the boxes
    :return: the updated Image object with the bounding boxes around the text
    """
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image


def inference(img_source, lang='en') -> list[str]:
    """
    Reads the text in the image and returns all the text found.
    :param img_source: the source of the image
    :param lang: the language used to detect the text
    :return: the list of text
    """
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
