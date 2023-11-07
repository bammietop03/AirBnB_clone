#!/usr/bin/python3
"""
A program called console.py that contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Handles the command-line interpreter for the Holberton Airbnb Clone project.

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

    def do_create(self, arg):
        """ creates a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
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
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
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
        """Prints all string representations of all instances."""
        args = arg.split()
        if not arg:
            all_object = storage.all()
            object_list = []
            for key in all_object:
                object_list.append(str(all_object[key]))
            print(object_list)
        else:
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            all_object = storage.all()
            object_list = []
            for key, obj in all_object.items():
                if key.split(".")[0] == args[0]:
                    object_list.append(str(obj))
            if not object_list:
                print("** no instance found **")
            else:
                print(object_list)
    
    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
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
                attr_name = args[2]
                attr_value = args[3]
                setattr(instance, attr_name, eval(attr_value))
                instance.save()
            else:
                print("** no instance found **")

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
