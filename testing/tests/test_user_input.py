import unittest
from unittest.mock import patch, MagicMock
from PIL import Image
from io import BytesIO
from app.image_processor import ImageProcessor


class TestImageProcessor(unittest.TestCase):
    def test_nothing(self):
        return