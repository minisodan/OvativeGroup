import unittest
import os
from app.image_processor import ImageProcessor


class TestSingleton(unittest.TestCase):
    def setUp(self) -> None:
        self.processor = ImageProcessor()

    def test_same_singleton(self):
        """
        Tests that multiple references point to the same instance of the singleton.
        """

        self.singleton: ImageProcessor = ImageProcessor()
        self.assertEqual(self.singleton, self.processor)

    def test_singleton_attributes(self):
        self.assertTrue(self.processor.urls == [])
        self.assertTrue(self.processor.path == os.path.join(os.path.expanduser('~'), 'Desktop', 'Ovative Group Caption '
                                                                                                'Generator'))
