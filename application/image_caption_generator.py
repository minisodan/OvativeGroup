from application.image_processor import ImageProcessor


class ImageCaptionGenerator:
    def __init__(self):
        self.using_url: bool = False
        self.image_processor: ImageProcessor

    def start(self):
        user_input: str = input('Will you use an image URL or a file directory? (url/dir)\n> ')
        self.process_input(user_input)

    def process_input(self, user_input: str) -> None:
        self.using_url = True if user_input.lower().__contains__('u') else False

        image_processing = ImageProcessor(self.using_url)
        image_processing.process_image()
        return
