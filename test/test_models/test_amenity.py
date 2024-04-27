#!/usr/bin/python3
"""Module for testing Amenity class"""

import unittest
import json
import pep8
import datetime

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_module_doc(self):
        """Test module documentation"""
        doc = Amenity.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_amenity(self):
        """Test PEP8 conformance for amenity module"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_amenity(self):
        """Test PEP8 conformance for test_amenity module"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_doc(self):
        """Test constructor documentation"""
        doc = Amenity.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_inheritance(self):
        """Test if Amenity class inherits from BaseModel"""
