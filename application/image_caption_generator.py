from application.image_processor import ImageProcessor


class ImageCaptionGenerator:
    def __init__(self):
        self.image_processor: ImageProcessor

    def start(self):
        user_input: str = input('Please provide an image URL or directory path.\n> ')
        self.process_input(user_input)

    def process_input(self, user_input: str) -> None:
        image_processing = ImageProcessor(user_input)
        image_processing.validate_file_extension()
        return
