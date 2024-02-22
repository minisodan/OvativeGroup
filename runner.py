import utils
from application.image_caption_generator import start


def main():
    utils.clear_terminal()
    print('Welcome to the Ovative Group Caption Generator!', end='\n\n')
    start()


if __name__ == '__main__':
    main()

# To run the terminal application, make sure your terminal is in the root directory of the project
# In the terminal, run 'python -m runner'
# This runs this file as a module of the entire project, allowing imports to function properly
