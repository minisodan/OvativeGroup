Overview
========

**Project Overview: Ovative Group Capstone**
----------------------------------------------------

In this capstone project for Ovative Group, we have developed an in-house tool designed for the marketing team to speed up the processing of advertising images.
Our integrated solution combines multiple technologies to process images, extract text, and generate detailed descriptions, thereby optimizing the marketing workflow.

**Features**
------------

- **Image Captioning**: Utilizes the Salesforce/blip-image-captioning-large model to produce two types of captions: a standard caption and a conditional caption prefixed with "an image of" to vary the descriptive focus.

- **Optical Character Recognition (OCR)**: Implements EasyOCR to detect and extract text from images with a confidence level above 30%.

- **Language Understanding**: Employs the Cohere large language model to synthesize the outputs from the OCR and image captioning models into a coherent text description of each image.

**Output**
----------

All results are  recorded in a CSV file on your desktop. This structured dataset includes fields for the image source, captions, extracted text, and processing timestamps.
Running the program will create a folder with CSV in it unless it already exists.

**Efficiency**
--------------

Our application is written in Python and is optimized with threading to enhance processing speed, ensuring quick and efficient analysis. The system is managed within the Miniconda environment, facilitating streamlined package management and environment configuration.


