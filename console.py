#!/usr/bin/python3
import cmd
#from models.base_model import BaseModel
import models
"""
program console
"""


class HBNBCommand(cmd.Cmd):
    """console that contains the entry point of the command interpreter"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        """exits the program"""
        return quit()

    def do_EOF(self, line):
        """exits the program"""
        return exit()

    def help(self, line):
        """shows the user the different commands the console has"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()