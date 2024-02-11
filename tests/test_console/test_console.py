#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
import sys
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test console"""
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @staticmethod
    def capture_output(func, *args, **kwargs):
        """
        Helper function to capture output of a method
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            func(*args, **kwargs)
            return captured_output.getvalue().strip()
        finally:
            sys.stdout = sys.__stdout__

    def test_quit(self):
        with patch('builtins.input', return_value="quit"):
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        with patch('builtins.input', return_value="EOF"):
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create(self):
        output = self.capture_output(self.console.onecmd, "create")
        self.assertIn("** class name missing **", output)

        output = self.capture_output(self.console.onecmd, "create UnknownClass")
        self.assertIn("** class doesn't exist **", output)

        output = self.capture_output(self.console.onecmd, "create BaseModel")
        self.assertGreater(len(output), 0)  # Check if the instance ID is present
        self.assertIn("BaseModel", output)

    def test_show(self):
        with patch('builtins.input', return_value="show BaseModel.123"):
            output = self.capture_output(self.console.onecmd, "show BaseModel.123")
            self.assertIn("** instance id missing **", output)

    def test_destroy(self):
        with patch('builtins.input', return_value="destroy BaseModel.123"):
            output = self.capture_output(self.console.onecmd, "destroy BaseModel.123")
            self.assertIn("** instance id missing **", output)

    def test_all(self):
        # Check when no class name is provided
        output = self.capture_output(self.console.onecmd, "all")
        self.assertIn("Objects:", output)

        output = self.capture_output(self.console.onecmd, "all UnknownClass")
        self.assertIn("** class doesn't exist **", output)

        output = self.capture_output(self.console.onecmd, "all BaseModel")
        self.assertGreater(len(output), 0)  # Check if there's at least one instance

    def test_update(self):
        with patch('builtins.input', return_value="update BaseModel"):
            output = self.capture_output(self.console.onecmd, "update BaseModel")
            self.assertIn("** instance id missing **", output)


if __name__ == '__main__':
    unittest.main()
