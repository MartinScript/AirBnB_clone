#!/usr/bin/python3
"""Module for testing BaseModel class"""

import unittest
import json
import pep8
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_module_doc(self):
        """Test module documentation"""
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """Test PEP8 conformance for models/base_model.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_base_model(self):
        """Test PEP8 conformance for tests/test_models/test_base_model.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_doc_constructor(self):
        """Test constructor documentation"""
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_creation_and_to_dict(self):
        """Test creation of BaseModel instance and its to_dict method"""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str,
        }
        my_model_json = my_model.to_dict()
        for key, value in model_types_json.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, my_model_json)
                self.assertIs(type(my_model_json[key]), value)

    def test_attribute_types(self):
        """Test attribute types of BaseModel instance"""
        second_model = BaseModel()
        self.assertIsInstance(second_model, BaseModel)
        second_model.name = "Andres"
        second_model.my_number = 80
        self.assertEqual(second_model.name, "Andres")
        self.assertEqual(second_model.my_number, 80)
        model_types = {
            "my_number": int,
            "name": str,
            "updated_at": datetime.datetime,
            "id": str,
            "created_at": datetime.datetime,
        }
        for key, value in model_types.items():
            with self.subTest(key=key, value=value):
                self.assertIn(key, second_model.__dict__)
                self.assertIs(type(second_model.__dict__[key]), value)

    def test_uuid_uniqueness(self):
        """Test uniqueness of UUIDs"""
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_consistency(self):
        """Test consistency of datetime attributes"""
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_3.updated_at)
        self.assertNotEqual(model_3.created_at, model_4.created_at)

    def test_string_representation(self):
        """Test the string representation of BaseModel"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id
        expected = "[BaseModel] ({}) {}".format(id_model, my_model.__dict__)
        self.assertEqual(str(my_model), expected)

    def test_constructor_with_kwargs(self):
        """Test constructor with kwargs as attribute values"""
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        js
