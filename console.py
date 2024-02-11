#!/usr/bin/python3
"""Console Module
This module controls all databases.
Can create, modify and delete instances.
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models import storage
from datetime import datetime
import shlex


class HBNBCommand(cmd.Cmd):
     """command processor class."""
    prompt = "(hbnb) "
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'Amenity': Amenity
    }

    def emptyline(self):
        """
        When an empty line is entered in response to the prompt,
        it won't repeat the last nonempty command entered.

        """
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        EOF command to exit the program
        """
        return True

    def help_quit(self):
        """help command for quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """help command for EOF"""
        print("EOF command to exit the program")

    def do_create(self, line):
        """
        Create command to create a new instance
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def help_create(self):
        """help command for create"""
        print("create command to create a new instance")

    def do_show(self, line):
        """
        Show command to display an instance
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        instance = storage.all()[key]
        print(instance)

    def help_show(self):
        """help command for show"""
        print("show command to display an instance")

    def do_destroy(self, line):
        """
        Destroy command to delete an instance
        """
        if not line:
            print("** class name missing **")
            return
        args = shlex.split(line)
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def help_destroy(self):
        """help command for destroy"""
        print("destroy command to delete an instance")

    def do_all(self, line):
        """
        All command to display all instances
        """
        if not line:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)
            return
        args = shlex.split(line)
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instances = [str(obj) for key, obj in storage.all().items()
                     if class_name == key.split('.')[0]]
        print(instances)

    def help_all(self):
        """help command for all"""
        print("all command to display all instances")

    def do_update(self, line):
        """
        Update command to update an instance
        """
        args = shlex.split(line)
        if not args:
            print('** class name missing **')
            return

        class_name = args[0]

        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print('** instance id missing **')
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"

        if key not in storage.all():
            print('** no instance found **')
            return

        if len(args) < 3:
            print('** attribute name missing **')
            return

        attribute_name = args[2]

        if len(args) < 4:
            print('** value missing **')
            return

        attribute_value = self.analyze_parameter_value(args[3], class_name, attribute_name)
        setattr(storage.all()[key], attribute_name, attribute_value)
        setattr(storage.all()[key], 'updated_at', datetime.now())
        storage.save()

    def help_update(self):
        """help command for update pro"""
        print("update command to update an instance")

    def analyze_parameter_value(self, value, class_name, attribute_name):
        """
        Analyzes the parameter value and returns appropriate data type.
        """
        if class_name in HBNBCommand.classes and \
            attribute_name in HBNBCommand.classes[class_name]().__dict__:
                attribute_type = type(HBNBCommand.classes[class_name]().__dict__[attribute_name])
                if attribute_type == int:
                    return int(value)
                elif attribute_type == float:
                    return float(value)
                else:
                    return value
        return value


if __name__ == '__main__':
    HBNBCommand().cmdloop()

