#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from datetime import datetime
from models.engine.file_storage import FileStorage
from shlex import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    # classes variable to store
    classes = {
        'BaseModel': base_model.BaseModel,
        'User': user.User,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity
    }

    prompt = "(hbnb) "
    file_path = "file.json"

    # I was trying to se this def to solve something
    # it will be deleted if we don't want it
    def update_classes(self):
        # load existing instances if not loaded
        FileStorage.reload()
        # Update the classes attr
        HBNBCommand.classes = FileStorage().all()

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        ClassName = arg.split()[0]

        if ClassName in HBNBCommand.classes:
            new_instance = HBNBCommand.classes[ClassName]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        arguments = arg.split()

        if not arguments:
            print("** class name missing **")
            return

        ClassName = arguments[0]

        if ClassName not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]
        key = f"{ClassName} {instance_id}"

        if key in FileStorage.all():
            del FileStorage().all()[key]
            FileStorage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances """
        if not arg:
            instance = [str(obj) for obj in storag.all().values()]
            print(instance)
            return

        ClassName = arg.split()[0]

        if ClassName not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance = [str(obj) for key, obj in FileStorage().all().items()
                    if ClassName == key.split(' ')[0]]
        print(instance)

    def do_show(self, arg):
        arguments = arg.split()

        if not arguments:
            print("** class name missing **")
            return

            ClassName = arg[0]

            if ClassName not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            # to check if at least the name of the class and it's id present
            if len(arguments) < 2:
                print("** instance id missing **")
                instance_id = arguments[1]
            key = f"{ClassName} {instance_id}"

            if key not in FileStorage().all():
                print("** no instance found **")
                return

            instance = FileStorage().all()[key]
            print(instance)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        # split arg into a list taking into account the special characters
        arguments_list = shlex.split(arg)

        # checks if class name found
        if len(arguments_list) == 0:
            print("** class name missing **")
            return

        ClassName = arguments_list[0]

        if ClassName not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        # to check if at least the name of the class and it's id present
        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments_list[1]
        key = f"{ClassName} {instance_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        # check if name of attribute is missing
        if len(arguments_list) < 3:
            print("** attribute name missing **")
            return

        attName = arguments_list[3]

        # check if attribute value is missing
        if len(arguments_list) < 4:
            print("** value missing **")
            return

        attValue_str = arguments_list[3]

        # Get attribute value type and for instance
        instance = FileStorage().all()[key]
        attrValueType = type(getattr(instance, attName, None))

        # cast attribute type
        if attrValueType == str:
            attrValue = attValue_str
        elif attrValueType == int:
            if attValue_str.isdigit():
                attrValue = int(attValue_str)
            else:
                print("** invalid value **")
                return
        elif attrValueType == float:
            try:
                attrValue = float(attValue_str)
            except ValueError:
                print("** invalid value **")
                return
        else:
            print("** invalid value **")
            return

        # update and save changes
        setattr(instance, attName, attrValue)
        FileStorage().save()

        print("Updated successfully.")

    def do_quit(self, arg):
        # update classes before exiting
        self.update_classes()
        return True

    def help_quit(self):
        print("Quit command to exit the program with formatting")

    def do_EOF(self):
        print("")
        # update classes before exiting
        self.update_classes()
        return True

    def help_EOF(self):
        print("Quit command to exit the program without formatting")


if _name_ == '_main_':
    HBNBCommand().cmdloop()