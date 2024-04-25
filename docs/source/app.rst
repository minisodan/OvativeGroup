App Module
==========

The `App` Module contains two files in it, `image_processor.py` and `input_manager.py`. When the application starts,
it's these two files that initiate the process of processing the given images and accepting user input respectively.

----

Input Manager
-------------

``start()``
This method will start the application and is called in the `runner.py` file. It will first prompt the user for a
directory of images or a URL(s). A mix of both can be passed in, as long as each input is separated by a comma
(e.g., URL, directory path, URL, URL).

These inputs are added to a list that will be filtered in the utils.py file. That filtered list is then taken to the
Image Processor class.


``reprompt()``
This method is called at the end of every input cycle (i.e., after the application has processed the given inputs).
This takes a boolean parameter called `success`. This is to determine if the images in the `image_processor.py` file
were successfully processed.

.. code-block::

    msg: str = 'Would you like to provide more images? (y/n)' if success else 'Would you like to try again? (y/n)'

The `success` boolean will also determine which message to output to the user to be transparent as to what occurred.
If the processing was a success, it will simply ask if the user wants to provide more images; otherwise, it will ask
if they would like to try again. Before asking the user to try again, another message is displayed from the
`image_processor.py` file to explain what happened in more depth.

Image Processor
---------------

The ``ImageProcessor`` class is treated as a singleton. This is because only one instance is needed for the
application's lifecycle when it starts.

``__source_to_image_object()``
The filtered list of inputs from the `utils.py` file will be passed to this method. This will convert every URL or image
located in a directory into an Image object from the Pillow library.

When the images are converted to Image objects, they will be added to a list

