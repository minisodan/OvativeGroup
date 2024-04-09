import threading

from models import cohere

class CohereThread(threading.Thread):
    """
     A class for the Cohere Thread to implement multithreading: The purpose of this
     class is to return an instance variable of each model's/LLM's respective threads that can
     be used/accessed for output
    """

    # constructor
    def __init__(self):
        # execute the base constructor
        threading.Thread.__init__(self)

    # function to execute Cohere Thread
    def run(self):
        self.ocr_output = cohere.coherence(self.captions[0], self.captions[1], self.ocr_output)
