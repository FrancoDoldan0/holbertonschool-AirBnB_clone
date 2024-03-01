#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage

class HBNBCommand(cmd.Cmd):
    """interpreter"""
    prompt = "(hbnb) "
    model_classes = {
        "BaseModel",
        "User",
        "Place",
        "City",
        "State",
        "Amenity",
        "Review"
    }

    def do_quit(self, args):
        """Exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True

    def do_help(self, arg):
        """help"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """empty line  shouldn’t execute anything"""
        pass

    def do_create(self, args):
        """
        Create a new instance of BaseModel
        """

        if not args:
            print("** class name missing **")
        if args not in HBNBCommand().model_classes:
            print(" ** class doesn't exist ** ")
        else:
            new_instance = BaseModel()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
