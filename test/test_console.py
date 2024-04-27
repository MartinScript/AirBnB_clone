#!/usr/bin/python3
"""Test cases for the HBNBCommand class in the console module."""

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up the test environment."""
        self.console = HBNBCommand()  # Create an instance of the HBNBCommand class

    def tearDown(self):
        """Tear down the test environment."""
        del self.console  # Delete the instance of the HBNBCommand class after each test

    def test_quit_command(self):
        """Test the quit command."""
        result = self.console.onecmd("quit")  # Execute the quit command
        self.assertTrue(result)  # Assert that the result of the command is True

    def test_EOF_command(self):
        """Test the EOF command."""
        result = self.console.onecmd("EOF")  # Execute the EOF command
        self.assertTrue(result)  # Assert that the result of the command is True


if __name__ == "__main__":
    unittest.main()
