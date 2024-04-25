import csv
import datetime
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

import requests
import torch
from PIL import Image
from tqdm import tqdm

import utils
from models import cohere
from threads.blip_image_thread import BlipImageThread
from threads.easy_ocr_thread import EasyOcrThread


class ImageProcessor(object):
    """
    This class enforces a singleton structure. This is because only *one* instance of ImageProcessor is needed when the
    application is in use.
    """

    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(ImageProcessor, cls).__new__(ImageProcessor)
        return cls.__instance

    def __source_to_image_object(self, image_sources: list[str]) -> list[tuple[Image, str]]:
        """
        This method converts the URL to an image if it is a valid image link. Otherwise, it converts the given file
        directory.
        :return: Pillow Image type
        """

        # Do not delete this line; used for creating the image
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        results: list[tuple[Image, str]] = []

        for img_source in image_sources:
            if utils.is_url(img_source):
                results.append((Image.open(requests.get(img_source, stream=True).raw).convert('RGB'), img_source))

            if utils.is_dir(img_source):
                results.append(((Image.open(img_source)).convert("RGB"), img_source))

        return results

    def process_input(self, image_sources: list[str]) -> bool:
        """
        This method handles the logic for processing images. It will return a boolean indicating a successful
        processing of the images.
        :param image_sources: A list of image URLs or directory paths to be processed
        :return: True or False
        """
        success = False

        utils.clear()
        print('Checking input...\nThis may take a while if many images were provided.')
        filtered_input: list[str] = utils.filter_and_validate(image_sources)

        # processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        # model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

        # Receive the given input as a Pillow Image object and the given source
        images: list[tuple[Image, str]] | None = self.__source_to_image_object(filtered_input)

        if len(images) == 0:
            print('No provided input was valid. Nothing found to process.')
            return False

        utils.clear()
        print('Processing images...\n')

        utils.create_dir()

        # a list representing the names of each column in the generated .csv file
        fieldnames: list[str] = ['Image Source', 'Conditional Caption', 'Unconditional Caption', 'Text Found in Image',
                                 'Compiled Output', 'Date Processed', 'Time Processed']

        # used to store generated outputs from the models
        rows: list[dict] = []
        values: list[str]

        print()  # to space the captions generated in the terminal

        for img, img_source in tqdm(images, desc='Progress', ascii=False):
            # multithreading for speed and efficiency
            t1 = BlipImageThread(img)
            t2 = EasyOcrThread(img_source)

            # start the multithreading to have both time-intensive models work in parallel
            t1.start()
            t2.start()

            # end both threads
            t1.join()
            t2.join()

            # collect all data/captions from the models *before* adding the information to the rows dict
            captions: tuple[str, str] = t1.captions

            # get the list of all words found in the image
            ocr_output: list[str] | str = t2.ocr_output

            # Use Large Language Model (Cohere) to compile output and give deeper context
            compiled_output: str = cohere.coherence(captions[0], captions[1], ocr_output)

            # get the current date and time the photos were processed
            date: str = datetime.datetime.now().strftime('%Y-%m-%d')
            current_time: str = datetime.datetime.now().strftime('%H:%M:%S')

            # the values used to store in the rows dict
            values = [img_source, captions[0], captions[1], ocr_output, compiled_output, date, current_time]

            rows.append({k: v for (k, v) in zip(fieldnames, values)})

        success = self.store_outputs(rows)

        return success

    def store_outputs(self, rows: list[dict]) -> bool:
        """
        Store all the given data in their respective columns the .csv file.
        :param rows: a list of dictionaries, where each dict is a row in the .csv file
        :return: True or False for successfully storing the data
        """
        # a boolean representing if the output file exists; using `open` creates the file immediately
        file_exists: bool = os.path.isfile(utils.output_file_path())

        try:
            with open(utils.output_file_path(), 'a') as file:

                # create a writer object to write the given rows in the csv file
                writer = csv.DictWriter(file, fieldnames=rows[0].keys())

                # only write the column headers if the file was created for the first time
                if not file_exists:
                    writer.writeheader()

                for row in rows:
                    writer.writerow(row)

                print(f'\nData stored successfully in "{utils.output_file_path()}"')

            return True
        except PermissionError:
            utils.clear()
            print(f'WARNING: the file located at "{utils.output_file_path()}" is open and is preventing any data from '
                  f'being saved.', 'Please close it and try again.', sep='\n')

            return False
