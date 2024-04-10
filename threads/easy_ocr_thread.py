import threading
from models import easy_ocr as ocr, easy_ocr


class EasyOcrThread(threading.Thread):
    """
     A class for the easyOCR Thread to implement multithreading: The purpose of this
     class is to return an instance variable of each model's/LLM's  respective threads that can
     be used/accessed for output
    """

    # constructor
    def __init__(self, img_source: str):
        # execute the base constructor
        threading.Thread.__init__(self)

        self.img_source: str = img_source
        self.ocr_output: list[str] = easy_ocr.inference(self.img_source)

    @property
    def ocr_output(self) -> list[str]:
        return self.__ocr_output

    @ocr_output.setter
    def ocr_output(self, ocr_output: list[str]) -> None:
        # check if the passed in variable is a list
        if ocr_output is None or not isinstance(ocr_output, list):
            raise ValueError(f'{self.__class__.__name__}.ocr_output must be a list. The passed in value is of type '
                             f'{type(ocr_output)}')

        # check if every item in the list is a string
        if not any(isinstance(outputs, str) for outputs in ocr_output):
            raise ValueError(f'{self.__class__.__name__}.ocr_output must be a list of strings. The passed in value '
                             f'was {ocr_output}')
        self.__ocr_output = ocr_output

    # function to execute easyOCR Thread
    def run(self):
        self.ocr_output = ocr.inference(self.img_source)
