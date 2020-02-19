#!/usr/bin/python3
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""
program console
"""


list_class = ["BaseModel", "User", "Amenity", "City", "Place", "Review", "State"]


class HBNBCommand(cmd.Cmd):
    """console that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return quit()

    def do_EOF(self, line):
        """ the command when write Ctrl+D """
        print()
        return exit()

    def emptyline(self):
        """ Line empty when write \n """
        pass

    #    def help(self, line):
    #        """shows the user the different commands the console has"""

    def do_create(self, line):
        args = split(line)
        if len(line) == 0:
            print("** class name missing **")
            return False
        if not args[0] in list_class:
            print("** class doesn't exist **")
        else:
            classes = eval(args[0] + "()")
            getid = getattr(classes, 'id')
            storage.save()
            print(getid)

    def do_show(self, line):
        args = split(line)
        if len(line) == 0:
            print("** class name missing **")
            return False
        if args[0] in list_class:
            if len(args) > 1:
                objs = storage.all()
                key = args[0] + '.' + args[1]
                if key in objs:
                    print(objs[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        args = split(line)
        if len(line) == 0:
            print("** class name missing **")
            return False
        if args[0] in list_class:
            if len(args) > 1:
                objs = storage.all()
                key = args[0] + '.' + args[1]
                if key in objs:
                    objs.pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line):
        args = split(line)
        new_list = []
        objs = storage.all()
        if len(line) > 1:
            if args[0] in list_class:
                for key, value in objs.items():
                    class_split = key.split(".")
                    if args[0] == class_split[0]:
                        new_list.append(value.__str__())
            else:
                print("** class doesn't exist **")
                return False
        else:
            for key, value in objs.items():
                new_list.append(value.__str__())
        print(new_list)

    def do_update(self, line):
        """method to update the attributes of the classes"""
        args = split(line)
        if len(line) == 0:
            print("** class name missing **")
            return False
        if args[0] in list_class:
            if len(args) > 1:
                objs = storage.all()
                key = args[0] + '.' + args[1]
                if key in objs:
                    if len(args) > 2:
                        if len(args) > 3:
                            get_attr = storage.all().get(key)
                            setattr(get_attr, args[2], args[3])
                            storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
