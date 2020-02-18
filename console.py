#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
"""
program console
"""


class HBNBCommand(cmd.Cmd):
    """console that contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
    Thomas = (globals()['BaseModel'])
#    storage.save()

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
        if len(line) == 0:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        elif line == 'BaseModel':
            print(BaseModel.id)

    def do_show(self, line):
        if len(line) == 0:
            print("** class name missing **")
        elif line != 'BaseModel':
            print("** class doesn't exist **")
        elif line == 'BaseModel':
            print("** instance id missing **")
#        elif line[2] is not BaseModel.id:
#            print("** no instance found **")

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