Easy OCR Model
==============

download_image Function
-----------------------

.. function:: download_image(image_url: str) -> Image

    Downloads an image from a URL into a format processable for Optical Character Recognition (OCR).

    :param image_url: The URL of the image.
    :type image_url: str
    :return: A Pillow Image object created from the downloaded image.

    Retrieves an image from the specified URL and converts it into a Pillow Image object for further processing.

draw_boxes Function
-------------------

.. function:: draw_boxes(image: Image, bounds, color='yellow', width=2) -> Image

    Draws bounding boxes around text found in the image.

    :param image: The Pillow Image object.
    :type image: Image
    :param bounds: An iterator containing the bounding box coordinates.
    :param color: The color of the bounding boxes (default is 'yellow').
    :type color: str
    :param width: The width of the bounding box lines (default is 2).
    :type width: int
    :return: The updated Pillow Image object with bounding boxes drawn around the text.

    Draws bounding boxes around text regions detected in the image. It is primarily used for visualization purposes.

inference Function
------------------

.. function:: inference(img_source, lang='en') -> list[str]

    Reads text from an image and returns the detected text.

    :param img_source: The source of the image (can be a URL or a file path).
    :type img_source: str
    :param lang: The language used for text detection (default is 'en' for English).
    :type lang: str
    :return: A list of strings containing the detected text.

    Reads text from the input image using the EasyOCR library. It supports both local image files and URLs.
    Text detection is performed based on the specified language, with an optional parameter to adjust confidence filtering.

Example usage:
--------------

.. code-block:: python

    from ocr_module import download_image, inference

    image_url = "https://example.com/image.jpg"
    img = download_image(image_url)
    text = inference(img)
    print("Detected Text:", text)

