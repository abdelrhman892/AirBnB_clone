#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
import shlex
from models import storage


class HBNBCommand(cmd.Cmd):
    # classes variable to store
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place,
            'Review': Review,
            'State': State,
            'Amenity': Amenity
    }

    prompt = "(hbnb) "
    file_path = "file.json"

    # create: Creates a new instance of BaseModel.
    # saves it (to the JSON file) and prints the id.
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

    # Deletes an instance based on the class name and id
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
            del storage().all()[key]
            storage.save()
        else:
            print("** no instance found **")

    # Prints all string representation of
    # all instances based or not on the class name
    def do_all(self, arg):
        """Prints all string representation of all instances """
        if not arg:
            instance = [str(obj) for obj in storage.all().values()]
            print(instance)
            return

        ClassName = arg.split()[0]

        if ClassName not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        instance = [str(obj) for key, obj in storage.all().items()
                    if ClassName == key.split('.')[0]]
        print(instance)

    # Prints the string representation of
    # an instance based on the class name and id
    def do_show(self, arg):
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
        key = f"{ClassName}.{instance_id}"

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

        if len(arguments_list) < 2:
            """to check if at least the name of the class and it's id present"""
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

        att_name = arguments_list[3]

        # check if attribute value is missing
        if len(arguments_list) < 4:
            print("** value missing **")
            return

        att_value_str = arguments_list[3]

        # Get attribute value type and for instance
        instance = storage.all()[key]
        attrValueType = type(getattr(instance, att_name, None))

        # cast attribute type
        if attrValueType == str:
            attrValue = att_value_str
        elif attrValueType == int:
            if att_value_str.isdigit():
                attrValue = int(att_value_str)
            else:
                print("** invalid value **")
                return
        elif attrValueType == float:
            try:
                attrValue = float(att_value_str)
            except ValueError:
                print("** invalid value **")
                return
        else:
            print("** invalid value **")
            return

        # update and save changes
        setattr(instance, att_name, attrValue)
        storage.save()

        print("Updated successfully.")

    def do_quit(self, arg):
        # update classes before exiting
        storage.reload()
        return True

    def help_quit(self):
        print("Quit command to exit the program with formatting")

    def do_EOF(self):
        print("")
        # update classes before exiting
        storage.reload()
        return True

    def help_EOF(self):
        print("Quit command to exit the program without formatting")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
