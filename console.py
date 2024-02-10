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
from datetime import datetime


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

    def analyze_parameter_value(self, value):
        """
        Analyzes the parameter value and returns the appropriate data type.
        """
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value

    def do_create(self, arg):
        """
        create: Creates a new instance of BaseModel.
        saves it (to the JSON file) and prints the id.
        """
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
        """Deletes an instance based on the class name and id"""
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

    def do_show(self, arg):
        """
        Prints the string representation of
        an instance based on the class name and id
        """
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

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
<<<<<<< HEAD
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
=======
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                storage.save()
>>>>>>> Naira

    def do_quit(self, arg):
        # update classes before exiting
        storage.reload()
        return True

    def help_quit(self):
        print("Quit command to exit the program with formatting")

    def do_EOF(self, arg):
        print("")
        # update classes before exiting
        storage.reload()
        return True

    def help_EOF(self):
        print("Quit command to exit the program without formatting")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
