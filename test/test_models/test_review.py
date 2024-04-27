#!/usr/bin/python3
"""Module for testing the Review class"""

import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_module_doc(self):
        """Test module documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """Test PEP8 conformance for models/review.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_review(self):
        """Test PEP8 conformance for tests/test_models/test_review.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_review.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_doc(self):
        """Test constructor documentation"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_inheritance_and_attributes(self):
        """Test inheritance from BaseModel and attribute types"""
        with self.subTest(msg="Inheritance"):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg="Attributes"):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)


if __name__ == "__main__":
    unittest.main()
