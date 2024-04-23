Threading
---------

We have implemented multithreading into the project for effeciency.
The way we have done this is by creating classes of the two models used
in this project, so they many return an instance of a thread to be used in the
``image_processer.py`` file.

    The Cohere LLM does not have a multihreading implementation, as it needs to wait for the input
    from both the easyOCR and blip-image models.

- ``blip_image_thread.py``
    Class that represents a thread instance salesforce BLIP image captioning model. Includes
    a basic constructor, along with setters and getters for properties needed to retun for the output
    as shown in the ``image_processer.py`` file.

    Contains a ``run`` function: returns the result of the BLIP image captioning model, which is needed
    for the CSV output.
- ``easy_ocr_thread.py``
    Class that represents a thread instance easyOCR model. Includes
    a basic constructor, along with setters and getters for properties needed to retun for the output
    as shown in the ``image_processer.py`` file.

    Also contains a ``run`` function: returns the result of the easyOCR  model, which is needed for the CSV output.

We create the instances as threads in the ``image_processer.py`` file to run parallel:

.. code-block:: console

    t1 = BlipImageThread(img)
    t2 = EasyOcrThread(img_source)

    t1.start()
    t2.start()

    # end both threads
    t1.join()
    t2.join()






