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

    def do_quit(self, name_args):
        """Exit the program"""
        return True

    def do_EOF(self, name_args):
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
        name_args = arg_passed.split()

        if len(name_args) == 0:
            print("** class name missing **")
            return

        class_name = name_args[0]

        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return

        from models.base_model import BaseModel
        new_instance = eval(f"{arg_passed}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg_passed):

        """checks if a class name was passed"""
        name_args = arg_passed.split()
        if len(name_args) == 0:
            print("** class name missing **")
            return

        """check if the class name is in the class dictionary"""
        class_name = name_args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return

        """check if the id class was passed"""
        if len(name_args) < 2:
            print("** instance id missing **")
            return

        """check if the name and id are not in the class dictionary"""
        from models import storage
        if f"{name_args[0]}.{name_args[1]}" not in storage.all():
            print("** no instance found **")
            return
        else:
            print(storage.all()[f"{name_args[0]}.{name_args[1]}"])
            return """if name and id exist"""

    def do_destroy(self, arg_passed):
        """coments"""
        name_args = arg_passed.split()

        """checks if a class name was passed"""
        if len(name_args) == 0:
            print("** class name missing **")
            return

        """check if the class name is in the class dictionary"""
        class_name = name_args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return

        """check if the id class was passed"""
        if len(name_args) == 1:
            print("** instance id missing **")
            return

        """check if the name and id are not in the class dictionary"""
        from models import storage
        if f"{name_args[0]}.{name_args[1]}" not in storage.all():
            print("** no instance found **")
            return
        else:
            del storage.all()[f"{name_args[0]}.{name_args[1]}"]
            storage.save()
            return

    def do_all(self, args_passed):
        """all method"""
        from models import storage
        """
        The do_all method prints instances from storage based on the
        provided class. If no class is given, it prints all instances.
        If an invalid class is provided, it shows an error message.
        If a valid class is given, it prints instances belonging to that class
        """
        name_args = args_passed.split()
        instances = storage.all()

        if not name_args:
            print([str(instance) for instance in instances.values()])
        elif name_args[0] not in self.model_classes:
            print("** class doesn't exist **")
        else:
            """In this else block, the first argument(which is the class name)
            is taken and used to search for instances in the storage.
            All instances in the storage are iterated over,
            and the class name of each instance is compared to the
            provided class name.
            If they match, the instance is converted to a string and
            added to a list.
            Finally, this list of instances is printed.
            """
            class_name = name_args[0]
            matching_instances = []
            for key, instance in instances.items():
                class_from_key = key.split('.')[0]
                if class_from_key == class_name:
                    instance_str = str(instance)
                    matching_instances.append(instance_str)
            print(matching_instances)

    def do_update(self, args_passed):
        from models import storage
        """
        update method
        """

        name_args = args_passed.split()

        """checks if a class name was passed"""
        if len(name_args) == 0:
            print("** class name missing **")
            return

        """check if the class name is in the class dictionary"""
        class_name = name_args[0]
        if class_name not in self.model_classes:
            print("** class doesn't exist **")
            return

        """check if the id class was passed"""
        if len(name_args) < 2:
            print("** instance id missing **")
            return

        """check if the name and id are not in the class dictionary"""
        from models import storage
        if f"{name_args[0]}.{name_args[1]}" not in storage.all():
            print("** no instance found **")
            return

        """check if the name of the atribute was passed"""
        if len(name_args) < 3:
            print("** attribute name missing **")
            return

        """check if the value was passed"""
        if len(name_args) < 4:
            print("** value missing **")
            return
        else:
            instance = storage.all()[f"{name_args[0]}.{name_args[1]}"]
            setattr(instance, name_args[2], name_args[3].strip('"'))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
