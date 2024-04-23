Overview
========

Project Overview: Ovative Group Capstone

In this capstone project for Ovative Group, we have developed an in-house tool designed for the marketing team to quickly process advertising images. This system utilizes advanced machine learning models to enhance image understanding and text generation, allowing for rapid analysis and utilization in marketing strategies. Our integrated approach combines multiple models to process images, extract text, and generate detailed descriptions, optimizing the workflow for marketing applications.

Features:
-	Image Captioning: Utilizes the Salesforce/blip-image-captioning-large model to generate two types of captions: a standard caption and a conditional caption prefixed with "an image of" to vary the descriptive focus.
-	Optical Character Recognition (OCR): Implements tomofi/EasyOCR to detect and extract text from images with a confidence level above 30%.
-	Language Understanding: Employs a large language model, cohere, to synthesize the outputs from the OCR and image captioning models into a coherent text description of each image.

Output:
All results are systematically recorded in a CSV file on your desktop, providing a structured dataset with fields for the image source, captions, extracted text, and processing timestamps.

Efficiency:
Our application is built in Python and optimized with threading to enhance processing speed, ensuring quick and efficient analysis. We utilize the Miniconda environment for streamlined package management and environment configuration.
This project demonstrates the power of integrating multiple AI tools to create a versatile and powerful system for image and text analysis.

