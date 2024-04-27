#!/usr/bin/python3
"""Module for testing the User class"""

import unittest
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_module_doc(self):
        """Test module documentation"""
        doc = User.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_user(self):
        """Test PEP8 conformance for models/user.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_user(self):
        """Test PEP8 conformance for tests/test_models/test_user.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_constructor_doc(self):
        """Test constructor documentation"""
        doc = User.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_inheritance_and_attributes(self):
        """Test inheritance from BaseModel and attribute types"""
        with self.subTest(msg="Inheritance"):
            self.assertTrue(issubclass(User, BaseModel))

        with self.subTest(msg="Attributes"):
            self.assertIsInstance(User.email, str)
            self.assertIsInstance(User.password, str)
            self.assertIsInstance(User.first_name, str)
            self.assertIsInstance(User.last_name, str)


if __name__ == "__main__":
    unittest.main()
