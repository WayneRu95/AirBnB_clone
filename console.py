#!/usr/bin/python3
"""
Airbnb Console Module

This module implements a console application for interacting with the Airbnb system.
"""

import sys
import cmd

class AirbnbConsole(cmd.Cmd):
    """
    The Airbnb console application.

    This class provides functionality for interacting with the Airbnb system via the command line.
    """

    prompt = '(hbnb) '

    def __init__(self):
        super().__init__()
        self.prompt = '(hbnb) '  

    def emptyline(self):
        """
        Override emptyline method to handle empty input.
        """
        pass

    def do_nothing(self, arg):
        """
        Does nothing
        """
        pass

    def do_help(self, arg):
        """
        Display help message.
        """
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    def do_EOF(self, arg):
        """
        Close console when EOF is reached.
        """
        print("")
        return True

    def do_quit(self, arg):
        """
        Quit console.
        """
        return True

    def do_update(self, arg):
        """
        Update attributes of an instance.

        Structure: update [class name] [id] [attribute] [value]
        Example: update BaseModel 1234-5678-9012 email "example@example.com"
        """
        args = arg.split()
        if len(args) < 4:
            print("Usage: update [class name] [id] [attribute] [value]")
            return
        class_name = args[0]
        obj_id = args[1]
        attribute = args[2]
        value = " ".join(args[3:])
        key = class_name + '.' + obj_id
        try:
            obj = storage.all()[key]
        except KeyError:
            print("** no instance found **")
            return
        setattr(obj, attribute, value)
        storage.save()
        print("Attribute updated successfully.")

    def default(self, arg):
        """
        Handle unrecognized commands.
        """
        print("Command not recognized:", arg)

if __name__ == "__main__":
    airbnb_console = AirbnbConsole()

    # Check if input is coming from a pipe
    if not sys.stdin.isatty():
        # Non-interactive mode
        for line in sys.stdin:
            airbnb_console.onecmd(line.strip())
    else:
        # Interactive mode
        airbnb_console.cmdloop()

