Threading
---------

We have implemented multithreading into the project for effeciency.
The way we have done this is by creating classes of the two models used
in this project, so they many return an instance of a thread to be used in the
``image_processer.py`` file.

    The Cohere LLM does not have a multihreading implementation, as it needs to wait for the input
    from both the easyOCR and blip-image models.

- ``blip_image_thread.py``
    Class that represents a thread instance for the salesforce BLIP image captioning model. Includes
    a basic constructor:

    .. code-block:: console

        def __init__(self, img: Image):
        # execute the base constructor
        threading.Thread.__init__(self)

        # instantiating captions container for conditonal and unconditional outputs
        self.captions: tuple[str, str] = ('', '')

        self.image: Image = img

        # processer and model instantiation from blip_image.py class
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

    Along with getters for properties needed to return for the output
    as shown in the ``image_processer.py`` file.

    The setters for the caption and image properties have built-in with input validation, to ensure proper input:

    .. code-block:: console

        @captions.setter
        def captions(self, captions: tuple[str, str]) -> None:
            # check if the passed in variable is a tuple
            if captions is None or not isinstance(captions, tuple):
                raise ValueError(f'{self.__class__.__name__}.captions must be a tuple. The passed in value is of type '
                                 f'{type(captions)}')

            # check if every item in the tuple is a string
            if not any(isinstance(caption, str) for caption in captions):
                raise ValueError(f'{self.__class__.__name__}.captions must be a tuple of strings. The passed in value '
                                 f'was {captions}')

            self.__captions = captions

    We do not have any getters/setters for the model and processer properties, as we will never need
    to return instances of them not change them in any way.

    Contains a ``run`` function that returns the result of the BLIP image captioning model, which is needed
    for the CSV output:

    .. code-block:: console

        def run(self):
            self.captions = bi.caption_image(self.image, self.processor, self.model)

- ``easy_ocr_thread.py``
    Class that represents a thread instance easyOCR model. Includes
    a basic constructor:

    .. code-block:: console

        def __init__(self, img_source: str):
            # execute the base constructor
            threading.Thread.__init__(self)

            self.img_source: str = img_source
            self.ocr_output: list = []

    Along with setters and getters for the OCR output needed to return for the output
    as shown in the ``image_processer.py`` file.

    .. code-block:: console

        @property
        def ocr_output(self) -> list:
            # returns OCR output
            return self.__ocr_output

        @ocr_output.setter
        def ocr_output(self, ocr_output: list | str) -> None:
            # check if the passed in variable is a list of string or an individual string
            if ocr_output is None or not isinstance(ocr_output, list):
                raise ValueError(f'{self.__class__.__name__}.ocr_output must be a list. The passed in value is of type '
                                f'{type(ocr_output)}')

            self.__ocr_output = ocr_output

    Also contains a ``run`` function that returns the result of the easyOCR  model, which is needed for the CSV output:

    .. code-block:: console

        def run(self):
            self.ocr_output = ocr.inference(self.img_source)

|
We create the instances as threads in the ``image_processer.py`` file to run parallel:

.. code-block:: console

    t1 = BlipImageThread(img)
    t2 = EasyOcrThread(img_source)

    t1.start()
    t2.start()

    # end both threads
    t1.join()
    t2.join()






