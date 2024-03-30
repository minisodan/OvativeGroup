import unittest
from unittest.mock import patch, MagicMock
import os
from utils import *


class TestUtilityFunctions(unittest.TestCase):

    def test_quitting(self):
        self.assertTrue(quitting('q'))
        self.assertTrue(quitting('quit'))
        self.assertFalse(quitting(''))
        self.assertFalse(quitting('quit!'))

    def test_is_dir(self):
        self.assertTrue(is_dir(os.getcwd()))
        self.assertFalse(is_dir('nonexistent_directory'))

    def test_is_url(self):
        self.assertTrue(is_url('https://www.example.com'))
        self.assertFalse(is_url('not_a_url'))

    def test_clean_url(self):
        self.assertEqual(clean_url('www.example.com'), 'https://www.example.com')
        self.assertEqual(clean_url('http://example.com'), None)

    # def test_create_dir(self):
    #     # Mock os.makedirs function
    #     with patch('os.makedirs') as mock_makedirs:
    #         # Call the function under test
    #         directory = create_dir()
    #
    #         # Assert that os.makedirs was called once
    #         mock_makedirs.assert_called_once()
    #
    #         # Assert that the returned directory exists
    #         self.assertTrue(os.path.isdir(directory))

    def test_is_valid_extension(self):
        self.assertTrue(is_valid_extension('jpg'))
        self.assertFalse(is_valid_extension('txt'))

    def test_filter_and_validate(self):
        image_sources = ['https://www.example.com/image.jpg', 'test_images', 'not_a_url']
        filtered_images = filter_and_validate(image_sources)
        self.assertEqual(len(filtered_images), 1)  # Only valid image should be added


if __name__ == '__main__':
    unittest.main()
