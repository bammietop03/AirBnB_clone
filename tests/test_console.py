#!/usr/bin/python3
""" Test Cases for Console.py"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def test_create_models(self):
        """ Test the 'create' command for different classes """
        classes = ['BaseModel', 'User', 'State', 'City',
                   'Place', 'Amenity', 'Review']
        with patch('sys.stdout', new=StringIO()) as output:
            for class_name in classes:
                command = f"create {class_name}"
                self.console.onecmd(command)
                self.assertFalse(HBNBCommand().onecmd(command))
                self.assertLess(0, len(output.getvalue().strip()))

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
            self.console.onecmd("count BaseModel\n")
            count = int(mock_stdout.getvalue().strip())
            self.assertGreaterEqual(count, 1)

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

    def test_all_models(self):
        """ Test the 'all' command for different classes """
        classes = ['BaseModel', 'User', 'State', 'City', 'Place', 'Amenity', 'Review']
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            for class_name in classes:
                self.console.onecmd(f"all {class_name}")
                output_lines = mock_stdout.getvalue().strip().split('\n')
                for line in output_lines:
                    # Check if each class name is present in the line
                    self.assertIn(class_name, line)


    def test_count_models(self):
        """ Test the 'count' command for different classes """
        classes = ['BaseModel', 'User', 'State', 'City',
                   'Place', 'Amenity', 'Review']
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            for class_name in classes:
                self.assertFalse(HBNBCommand().onecmd(f"{class_name}.count()"))
                self.assertGreaterEqual("1", mock_stdout.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertGreaterEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertGreaterEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertGreaterEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertGreaterEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertGreaterEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertGreaterEqual("1", output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertGreaterEqual("1", output.getvalue().strip())

    def test_show_models(self):
        """ Test the 'show' command for different classes """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "BaseModel.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            testCmd = f"BaseModel.update({testID}, attr_name, 'attr_value')"
            self.assertFalse(HBNBCommand().onecmd(testCmd))
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "User.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "State.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "Place.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "City.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "Amenity.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            command = "Review.show({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())


if __name__ == '__main__':
    unittest.main()
