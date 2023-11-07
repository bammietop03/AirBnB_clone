#!/usr/bin/python3
"""
A program called console.py that contains the entry point of the command interpreter
"""
import cmd


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
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()
