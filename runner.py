import utils
from app.image_caption_generator import start


"""
To run the terminal application, make sure your terminal is in the root directory of the project. 
In that directory, run 'python -m runner'. This runs this file as a module of the entire project, allowing imports to 
function properly.
"""


def main():
    utils.clear()
    print('Welcome to the Ovative Group Caption Generator!\n')
    start()


if __name__ == '__main__':
    main()
