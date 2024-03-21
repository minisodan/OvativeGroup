import io
import unittest
from unittest.mock import Mock
import app.image_caption_generator as icg


class TestUserInput(unittest.TestCase):
    def setUp(self) -> None:
        self.icg = icg.ImageProcessor

    def test_process_input_successful(self) -> None:
        user_input = 'hi'
        expected_error_string = ('Invalid input, hi, was given. Please provide an image URL(s) or an existing directory'
                                 'to multiple images.')
        actual_error_string = f'Invalid input, "{user_input}", was given. Please provide an image URL(s) or an existing directory to multiple images.'

    def test_process_input_fail(self):
        mock : Mock = Mock()
        self.icg.process_input("hi") = mock



