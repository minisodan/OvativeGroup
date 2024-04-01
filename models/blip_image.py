from PIL import Image
import datetime
import os
import utils


def caption_image(img: Image, img_source: str, processor, model) -> None:
    """
    This method will caption the given Pillow Image using the given model, which is the Salesforce captioning model.
    Two captions will be generated and outputted.
    :param img:
    :param img_source:
    :param processor:
    :param model:
    :return: None
    """

    # Conditional image captioning
    text = "a photo of"
    inputs = processor(img, text, return_tensors="pt")

    out = model.generate(**inputs, max_length=60)
    con_caption: str = 'Conditional image caption: ' + processor.decode(out[0], skip_special_tokens=True)
    print(con_caption)

    # Unconditional image captioning
    inputs = processor(images=img, return_tensors="pt")

    out = model.generate(**inputs, max_length=60)
    unc_caption: str = 'Unconditional image caption: ' + processor.decode(out[0], skip_special_tokens=True)
    print(unc_caption, end='\n\n')

    store_caption(utils.create_dir(), img_source, con_caption, unc_caption)


def store_caption(path: str, img_source: str, con_caption: str, unc_caption: str) -> None:
    """
    Stores the given captions of the given image in a file. Creates a new folder on the local device if that path
    doesn't already exist.
    :param path: The path of the directory
    :param img_source: The URL or directory path that sourced the image
    :param con_caption: Conditional caption
    :param unc_caption: Unconditional caption
    :return: None
    """

    current_time: datetime = datetime.datetime.now()
    file_name: str = current_time.strftime("%Y-%m-%d %H-%M-%S") + '.csv'

    with open(os.path.join(path, file_name), 'a') as file:
        file.write(f'Image source: {img_source}\n'
                   f'{con_caption}\n'
                   f'{unc_caption}\n\n')
        print(f'Stored output in "{path}\\' + file_name + '.txt"')


def valid_extension(img_source) -> bool:
    """
    This method will check if the user's input contains a valid file extension.
    :return: True or False
    """

    # reverse the string, get the file extension, and then re-reverse the string
    extension: str = img_source[::-1].split('.')[0][::-1]

    result: bool = extension in ['jpeg', 'jpg', 'png', 'tiff', 'raw', 'webp']

    # check if the file extension is valid
    return result


def invalid_msg(img_source) -> None:
    """
    Print a message saying that the given image source is not valid and won't be processed.
    :param img_source:
    :return: None
    """
    print(f'\nThe given input, "{img_source}", is an invalid input. This will not be processed.')


def break_line():
    """
    A break line that's used to help separate the outputs.
    :return:
    """
    print('\n-----------------------------------------------------------------------')


def prune(images: list[tuple[Image, str]]) -> list[tuple[Image, str]]:
    """
    This method will remove any None values from the list of image, image source pairings given.
    :param images:
    :return: a list without None values
    """
    return [image for image in images if image is not None]
