import unittest
from unittest.mock import patch, MagicMock
from PIL import Image
from io import BytesIO
from app.image_processor import ImageProcessor


class TestImageProcessor(unittest.TestCase):

    @patch('app.image_processor.utils.is_url', return_value=True)
    @patch('app.image_processor.ImageProcessor.__source_to_image_object')
    def test_source_to_image_object_url(self, mock_source_to_image_object, mock_is_url):
        # Mocking __source_to_image_object method
        img_url = "https://example.com/image.jpg"
        mock_source_to_image_object.return_value = [(Image.new('RGB', (100, 100)), img_url)]

        processor = ImageProcessor()
        result = processor._ImageProcessor__source_to_image_object([img_url])

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0][0], Image.Image)
        self.assertEqual(result[0][1], img_url)

    @patch('app.image_processor.utils.is_dir', return_value=True)
    @patch('app.image_processor.ImageProcessor.__source_to_image_object')
    def test_source_to_image_object_dir(self, mock_source_to_image_object, mock_is_dir):
        # Mocking __source_to_image_object method
        img_dir = "/path/to/image/directory"
        mock_source_to_image_object.return_value = [(Image.new('RGB', (100, 100)), img_dir)]

        processor = ImageProcessor()
        result = processor._ImageProcessor__source_to_image_object([img_dir])

        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0][0], Image.Image)
        self.assertEqual(result[0][1], img_dir)

    @patch('app.image_processor.utils.is_dir', return_value=True)
    @patch('PIL.Image.open')
    def test_source_to_image_object_dir_permission_error(self, mock_open, mock_is_dir):
        # Mocking image source as a directory with permission error
        img_dir = "/path/to/image/directory"
        mock_open.side_effect = PermissionError()

        processor = ImageProcessor()
        with self.assertRaises(SystemExit):
            processor._ImageProcessor__source_to_image_object([img_dir])


if __name__ == '__main__':
    unittest.main()
