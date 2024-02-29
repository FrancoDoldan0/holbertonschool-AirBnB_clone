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
        elif args not in self.classes:
            print("* class doesn't exist **")
        else:

            new_instance = BaseModel()
            print(new_instance.id)

    def do_show(self, args):
        """string representation of an instance
            based on the class name and id"""
    args = args.split()
    if not args:
        print("** class name missing **")
    elif args[0] not in self.classes:
        print("** class doesn't exist **")
    elif len(args) < 2:
        print("** instance id missing **")
    else:
        instance_key = args[0] + "." + args[1]
        if instance_key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[instance_key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
