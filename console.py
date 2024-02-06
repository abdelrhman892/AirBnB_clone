#!/usr/bin/python3
import cmd
from models import base_model
from datetime import datetime
from models.engine.file_storage import FileStorage
from shlex import shlex


class HBNBCommand(cmd.Cmd):
    # classes variable to store
    classes = {'BaseModel':BaseModel}

    prompt = "(hbnb) "
    file_path = "file.json"

    # I was trying to se this def to solve something
    # it will be deleted if we don't want it
    def update_classes(self):
        # load existing instances if not loaded
        storage.reload()
        # Update the classes attr
        HBNBCommand.classes = list(storage.all().keys())

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        ClassName = arg.split()[0]

        if ClassName == "BaseModel":
            new_instance = BaseModel()
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

        if key in storage.all():
            del storage.all()[key]
            storage.save()
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

        instance = [str(obj) for key, obj in storage.all().items()
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
            if len(arguments < 2):
                print("** instance id missing **")
                return

            instance_id = arguments[1]
            key = f"{ClassName} {instance_id}"

            if key not in storage.all():
                print("** no instance found **")
                return

            instance = storage.all()[key]
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
        if len(arguments < 2):
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
        if len(args_list) < 4:
            print("** value missing **")
            return

        attValue_str = arguments_list[3]

        # Get attribute value type and for instance
        instance = storage.all()[key]
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
        storage.save()

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
