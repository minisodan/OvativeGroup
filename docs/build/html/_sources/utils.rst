Utility Functions
=================

This document outlines utility functions used within the application to abstract certain operations and enhance clarity
and usability.

----

clear()
-------

Function to clear the console screen. Uses ``os.system`` to execute platform-specific clear commands.

quitting(user_input: str) -> bool
----------------------------------

Checks if the user input signifies quitting. Returns True if the input is 'q' or 'quit', otherwise False.

end() -> None
-------------

Ends the program execution by clearing the screen and terminating the application.

break_line()
------------

Prints a break line to help separate outputs for better human readability.

is_dir(directory: str) -> bool
------------------------------

Checks if the given path represents an existing local directory.

Parameters:
    - directory (str): Possible directory path.

Returns:
    - bool: True if the path exists and is a directory, False otherwise.

is_url(image_url: str) -> bool
------------------------------

Checks if the given string represents a valid URL.

Parameters:
    - image_url (str): URL of the image.

Returns:
    - bool: True if the string is a valid URL, False otherwise.

clean_url(user_input: str) -> str
---------------------------------

Checks if the user has a "clean" input URL. If the URL lacks 'https://' prefix and starts with 'www', it adds 'https://' to the beginning.

Parameters:
    - user_input (str): User input URL.

Returns:
    - str: Cleaned URL.

create_dir() -> None
--------------------

Creates a directory to store generated outputs if it doesn't exist already. Prints a message indicating the creation status.

output_file_path() -> str
-------------------------

Returns the path to the output file.

Returns:
    - str: Path to the output file.

validate_and_add_url(img_source: str, image_sources: list[str]) -> None
-----------------------------------------------------------------------

Validates and adds a URL to the list of image sources if it has a valid file extension.

Parameters:
    - img_source (str): URL of the image.
    - image_sources (list[str]): List of image sources.

validate_and_add_files(directory: str, image_sources: list[str]) -> None
------------------------------------------------------------------------

Validates and adds local image files from the given directory to the list of image sources if they have valid file extensions.

Parameters:
    - directory (str): Path of the directory with image files to be validated.
    - image_sources (list[str]): List of image sources.

is_valid_extension(img_source: str) -> bool
-------------------------------------------

Checks if the given string contains a valid file extension.

Parameters:
    - img_source (str): Source of the image with a file extension.

Returns:
    - bool: True if the extension is valid, False otherwise.

filter_and_validate(image_sources: list[str]) -> list[str]
----------------------------------------------------------

Filters and validates a list of image sources, distinguishing between URLs and local files, and adds them to the result list.

Parameters:
    - image_sources (list[str]): List of image sources.

Returns:
    - list[str]: Validated and filtered list of image sources.

