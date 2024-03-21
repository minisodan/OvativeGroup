import io
import unittest
from unittest.mock import Mock
import app.image_caption_generator as icg


class TestUserInput(unittest.TestCase):
    def setUp(self) -> None:
        self.icg = icg.ImageProcessor

    def test_process_input_successful(self) -> None:
        mock: Mock = Mock()
        icg.process_input = mock
        icg.process_input("https://i.pinimg.com/736x/8f/8c/f2/8f8cf2b9a584100047ff16974a5464e8.jpg")

        mock.assert_called_once()
