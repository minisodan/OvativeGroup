App Module
==========

The ``app`` module contains two files in it, ``image_processor.py`` and ``input_manager.py``. When the application
starts, these are the files that initiate the process of processing the given images and accepting user input
respectively.


Input Manager
-------------

``start()``
...........

**Parameters**:
    - ``None``
**Returns**:
    - ``None``

To start the application, this method is called in the ``runner.py`` file. It will first prompt the user for a
directory of images or a URL(s). A mix of both can be passed in, as long as each input is separated by a comma
(e.g., URL, directory path, URL, URL).

These inputs are added to a list that will be filtered in the (utils.py) file. That filtered list is then taken to the
Image Processor class.

----

``reprompt()``
..............

**Parameters**:
    - ``inputs: list[str], success: bool``
**Returns**:
    - ``None``

At the end of every input cycle (i.e., after the application has processed the given inputs), this will be called to
ask the user to provide further input if they wish to process more images. This takes a boolean parameter called
``success``. This is to determine if the images in the ``image_processor.py`` file were successfully processed.

.. code-block:: python

    msg: str = 'Would you like to provide more images? (y/n)' if success else 'Would you like to try again? (y/n)'

The ``success`` boolean will also determine which message to output to the user to be transparent as to what occurred.
If the processing was a success, it will simply ask if the user wants to provide more images; otherwise, it will ask
if they would like to try again. Before asking the user to try again, another message is displayed from the
``image_processor.py`` file to explain what happened in more depth.


Image Processor
---------------

The ``ImageProcessor`` class is treated as a singleton. This is because only one instance is needed for the
application's lifecycle when it starts.


``__source_to_image_object()``
..............................

**Parameters**:
    - ``image_sources: list[str]``
**Returns**:
    - ``list[tuple[Image, str]]``

The filtered list of inputs from the ```utils.py`` file will be passed to this method. This will convert every URL or
image located in a directory into an Image object from the Pillow library.

When the images are converted to Image objects, they will be added to a list of tuples. The tuples pair the Image object
with its given source.

.. code-block:: python

    results: list[tuple[Image, str]] = []

    for img_source in image_sources:
        if utils.is_url(img_source):
            results.append((Image.open(requests.get(img_source, stream=True).raw).convert('RGB'), img_source))

        if utils.is_dir(img_source):
            results.append(((Image.open(img_source)).convert("RGB"), img_source))

    return results

----

``process_input()``
...................

**Parameters**:
    - ``image_sources: list[str]``
**Returns**:
    - ``bool``

To proceed with the application, the list of tuples from the ``__source_to_image_object()`` method will be used. If the
list is empty (i.e., nothing could be converted to Image objects), the ``success`` boolean is set to False and is
returned. A messaged is also printed to inform the user of what happened.

.. code-block:: python

    if len(images) == 0:
        print('No provided input was valid. Nothing found to process.')
        return False

Otherwise, the program will continue and iterate through the list of tuples from
``__source_to_image_object()``.

.. code-block:: python

    for img, img_source in tqdm(images, desc='Progress', ascii=False):


The loop will access the image and the image source from every tuple in the list. This is to help with storing the
information in the CSV at the end of the input cycle. The for loop uses :doc:`threads` to have the
(Blip Image captioning) (model) and (OCR) run in tandem. The outputs from these models are then used in the (LLM) to
make a cohesive output. All outputs, including the date and time of the process, are added to a list. This list is then
converted into a dictionary.


Storing Outputs
---------------

To help with storing outputs, there is a variable called ``rows`` which is instantiated as an empty list. When
populated, it will be a list of dictionaries.

.. code-block:: python

    # used to store generated outputs from the models
    rows: list[dict] = []

This will represent the rows of information that need to be written to the CSV file. It is populated at the end of the
for loop in the ``process_input()`` method.

.. code-block:: python

    rows.append({k: v for (k, v) in zip(fieldnames, values)})

The fieldnames object is a list of strings that represents the names of the columns in the CSV file.

.. code-block:: python

    # a list representing the names of each column in the generated .csv file
    fieldnames: list[str] = ['Image Source', 'Conditional Caption', 'Unconditional Caption', 'Text Found in Image',
                             'Compiled Output', 'Date Processed', 'Time Processed']

----

``store_outputs()``
...................

**Parameters**:
    - ``rows: list[dict]``
**Returns**:
    - ``bool``

A list of dictionaries is taken as a parameter to this method. Each dictionary in the list represents a row to be added
to the CSV file.

.. code-block:: python

    # create a writer object to write the given rows in the csv file
    writer = csv.DictWriter(file, fieldnames=rows[0].keys())

    # only write the column headers if the file was created for the first time
    if not file_exists:
        writer.writeheader()

    for row in rows:
        writer.writerow(row)

    print(f'\nData stored successfully in "{utils.output_file_path()}"')

If the file is being created for the first time, the first row in the file will be the titles of each column to label
them. Otherwise, they won't be written.
