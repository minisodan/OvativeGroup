import os
import utils
from application.image_caption_generator import ImageCaptionGenerator

if __name__ == '__main__':
    utils.clear_terminal()
    print('Welcome to the Ovative Group Image Caption Generator!', end='\n\n')
    image_caption_generator = ImageCaptionGenerator()
    image_caption_generator.start()

# To run the test suite, make sure your terminal is in the root directory of the project
# In the terminal, run 'python -m runner'
# This runs this file as a module of the entire project, allowing imports to function properly
