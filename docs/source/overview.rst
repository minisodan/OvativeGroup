Overview
========

**Project Overview: Ovative Group Capstone**
----------------------------------------------------

In this capstone project for Ovative Group, we have developed an in-house tool specifically designed for the marketing team to expedite the processing of advertising images. By leveraging advanced machine learning models, this system enhances image understanding and text generation, facilitating rapid analysis and strategic use in marketing campaigns. Our integrated solution combines multiple technologies to process images, extract text, and generate detailed descriptions, thereby optimizing the marketing workflow.

**Features**
------------

- **Image Captioning**: Utilizes the Salesforce/blip-image-captioning-large model to produce two types of captions: a standard caption and a conditional caption prefixed with "an image of" to vary the descriptive focus.

- **Optical Character Recognition (OCR)**: Implements tomofi/EasyOCR to detect and extract text from images with a confidence level above 30%.

- **Language Understanding**: Employs the cohere large language model to synthesize the outputs from the OCR and image captioning models into a coherent text description of each image.

**Output**
----------

All results are systematically recorded in a CSV file on your desktop. This structured dataset includes fields for the image source, captions, extracted text, and processing timestamps.

**Efficiency**
--------------

Our application is crafted in Python and is optimized with threading to enhance processing speed, ensuring quick and efficient analysis. The system is managed within the Miniconda environment, facilitating streamlined package management and environment configuration.

This project exemplifies the power of integrating multiple AI tools to create a versatile and robust system for image and text analysis....
