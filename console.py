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
dict_class = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
              'City': City, 'Place': Place, 'Review': Review, 'State': State}

class HBNBCommand(cmd.Cmd):
    """console that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
#    Thomas = (globals()['BaseModel'])

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
#

    def do_create(self, line):
        args = split(line)
        if len(line) == 0:
            print("** class name missing **")
            return False
        if not args[0] in dict_class:
            print("** class doesn't exist **")
        else:

    def do_show(self, line):
        args = split(line)
        if len(line) == 0:
            print("** class name missing **")
            return False
        if args[0] in dict_class:
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
        if len(line) == 0:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        elif line == 'BaseModel':
            print("** instance id missing **")

    def do_all(self, line):
        if len(line) == 0:
            print("En proceso, todavia no se que poner")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        elif line == 'BaseModel':
            print(storage)

    def do_update(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        elif line == 'BaseModel':
            print("** instance id missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()