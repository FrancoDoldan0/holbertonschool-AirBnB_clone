#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


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

    def do_quit(self, name_arg):
        """Exit the program"""
        return True

    def do_EOF(self, name_arg):
        """Exit the program"""
        return True

    def do_help(self, arg_passed):
        """help"""
        cmd.Cmd.do_help(self, arg_passed)

    def emptyline(self):
        """empty line shouldn’t execute anything"""
        pass

    def do_create(self, arg_passed):
        """
        The code first splits the user input into words,
        checks if the class name is provided and if the class exists.
        Then, it creates an instance of the specified class, saves it,
        and finally prints the ID of the created instance.
        """
        name_arg = arg_passed.split()

        if len(name_arg) == 0:
            print("** class name missing **")
            return

        class_name = name_arg[0]

        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return

        from models.base_model import BaseModel
        new_instance = eval(f"{arg_passed}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg_passed):

        """checks if a class name was passed"""
        name_arg = arg_passed.split()
        if len(name_arg) == 0:
            print("** class name missing **")
            return

        """check if the class name is in the class dictionary"""
        class_name = name_arg[0]
        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return

        """check if the id class was passed"""
        if len(name_arg) < 2:
            print("** instance id missing **")
            return

        """check if the name and id are not in the class dictionary"""
        from models import storage
        if f"{name_arg[0]}.{name_arg[1]}" not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()[f"{name_arg[0]}.{name_arg[1]}"])
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
