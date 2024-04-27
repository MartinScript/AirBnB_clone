#!/usr/bin/python3
"""Module for testing the City class"""

import unittest
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_module_doc(self):
        """Test module documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_city(self):
        """Test PEP8 conformance for models/city.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_city(self):
        """Test PEP8 conformance for tests/test_models/test_city.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_city.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_doc(self):
        """Test constructor documentation"""
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_inheritance_and_attributes(self):
        """Test inheritance from BaseModel and attributes types"""
        with self.subTest(msg="Inheritance"):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg="Attributes"):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == "__main__":
    unittest.main()
