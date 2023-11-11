#!/usr/bin/python3
""" Test Cases for Console.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestConsoleCommands(unittest.TestCase):

    def setUp(self):
        """ Set up a new HBNBCommand instance before each test """
        self.console = HBNBCommand()

    def test_do_quit(self):
        """ Test the 'quit' command """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_do_EOF(self):
        """ Test the 'EOF' command """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))
            self.assertEqual(mock_stdout.getvalue(), '\n')

    def test_create_object(self):
        """ Test the 'create' command with a valid class name """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    def test_do_show_no_id(self):
        """ Test the 'Show' command with no id """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    def test_do_destroy_no_id(self):
        """ Test the destroy command with no id"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    def test_do_all(self):
        """ Testing all """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all")
            self.assertIn("BaseModel", mock_stdout.getvalue())

    def test_do_update_no_id(self):
        """ Test the update with ni id"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    def test_do_count(self):
        """ Testing Count command """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("count BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), '1')

    def test_do_create_invalid_class(self):
        """ Testing Create command with invalid class"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create InvalidClass")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

    def test_do_show_invalid_class(self):
        """ Testing Show with invalid class """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show InvalidClass 1234-5678")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

    def test_do_destroy_invalid_class(self):
        """ Testing Destroy with invalid class"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy InvalidClass 1234-5678")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

    def test_do_update_invalid_class(self):
        """ Testing update with invalid class"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update InvalidClass 1234-5678")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

    def test_do_all_invalid_class(self):
        """ Testing all with invalid class"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all InvalidClass")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** class doesn't exist **")

    def test_do_show_missing_id(self):
        """ Testing show with invalid id"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    def test_do_destroy_missing_id(self):
        """ Testing destroy eith missing id"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    def test_do_update_missing_id(self):
        """ Testing update with missing id """
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** instance id missing **")

    def test_do_update_missing_attribute(self):
        """ Testing update with missing attribute"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel 1234-5678")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** attribute name missing **")

    def test_do_update_missing_value(self):
        """ Testing update with missing value"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel 1234-5678 attribute_name")
            self.assertEqual(mock_stdout.getvalue().strip(),
                             "** value missing **")


if __name__ == '__main__':
    unittest.main()