#!/usr/bin/python3
"""
A program called console.py that contains the entry point of the
command interpreter
"""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_names = [subclass.__name__ for subclass in BaseModel.get_subclasses()]


class HBNBCommand(cmd.Cmd):
    """
    Handles the command-line interpreter for the Airbnb Clone project.

    Attributes:
        prompt (str): The custom command prompt, set to "(hbnb)".

    Public Methods:
        do_quit(self, arg): Allows exiting the program with the "quit" command.
        do_EOF(self, arg): Allows exiting the program with Ctrl+D (EOF).
        emptyline(self): Does nothing on an empty line.

    Usage:
        Run this console to interact with the Holberton Airbnb Clone project.
        Enter commands at the prompt, and use "quit" or Ctrl+D to exit.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def precmd(self, arg):
        """
        if "update" in arg:
            class_id, rest_of_command = arg.split(None, 1)
            rest_of_command = rest_of_command.replace('"', '')
            return f"{class_id} {rest_of_command}"
        """    
        if "." in arg:
            new_str = re.sub(r'[){}:\'"]', "", arg)
            new_str = re.sub(r'[(.,]', " ", new_str).split()
            new_str[0], new_str[1] = new_str[1], new_str[0]
            arg = " ".join(new_str)
        return super().precmd(arg)

    def do_create(self, arg):
        """ creates a new instance of BaseModel or User, saves it
        (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if args[0] in class_names:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()

            if args[0] not in class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]

                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()

            if args[0] not in class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]

                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on
        the class name. Ex: $ all BaseModel or $ all.
        """
        all_object = storage.all()
        object_list = []

        if arg:
            args = arg.split()
            if args[0] not in class_names:
                print("** class doesn't exist **")
                return

            object_list = [str(obj) for key, obj in all_object.items() if
                           key.split(".")[0] == args[0]]
        else:
            object_list = [str(all_object[key]) for key in all_object]

        if not object_list:
            print("** no instance found **")
        else:
            print(object_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()

            if args[0] not in class_names:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                key = args[0] + "." + args[1]
    
                if key in storage.all():
                    instance = storage.all()[key]
                    for i in range(2, len(args) - 1, 2):
                        if i + 1 < len(args):
                            attr_name = args[i]
                            attr_value = args[i + 1]
                            if attr_value.isdigit():
                                attr_value = int(attr_value)

                            setattr(instance, attr_name, attr_value)
                        else:
                            print("** invalid number of arguments **")
                            break
                    instance.save()
                else:
                    print("** no instance found **") 

    def do_count(self, arg):
        """Retrieves the number of instances of a specified class.
        Usage: <class name>.count()
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            if args[0] not in class_names:
                print("** class doesn't exist **")
            else:
                count = len([obj for obj in storage.all() if args[0] in obj])
                print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
