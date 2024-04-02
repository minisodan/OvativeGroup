from PIL import Image
import datetime
import os


def caption_image(img: Image, processor, model) -> tuple[str, str]:
    """
    This method will caption the given Pillow Image using the given model, which is the Salesforce captioning model.
    Two captions will be generated and outputted.
    :param img: the image object used to be captioned
    :param processor: the processor used to caption the images
    :param model: the model used to caption the images
    :return: None
    """

    # Conditional image captioning
    text = "a photo of"
    inputs = processor(img, text, return_tensors="pt")

    out = model.generate(**inputs, max_length=60)
    con_caption: str = 'Conditional image caption: ' + processor.decode(out[0], skip_special_tokens=True)

    # Unconditional image captioning
    inputs = processor(images=img, return_tensors="pt")

    out = model.generate(**inputs, max_length=60)
    unc_caption: str = 'Unconditional image caption: ' + processor.decode(out[0], skip_special_tokens=True)

    return con_caption, unc_caption  # return both generated captions
