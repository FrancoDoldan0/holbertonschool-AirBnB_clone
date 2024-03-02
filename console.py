#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd


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
        """empty line shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """""Creates a new instance of a class"""
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand().model_classes:
            print("** class doesn't exist **")
            return

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.amenity import Amenity
        from models.city import City
        from models.review import Review
        from models.place import Place
        new_instance = eval(f"{arg}()")
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
