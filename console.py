#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """interpreter"""
    prompt = "(hbnb) "

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
        """Create a new instance of BaseModel"""

        if not args:
            print("** class name missing **")
        elif arg not in self.classes:
            print("* class doesn't exist **")
        else:

            new_instance = BaseModel()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
