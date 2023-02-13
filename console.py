#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
     a program called console.py that contains the entry point of the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
        Exiting the program with quit
        """
        return True

    def do_EOF(self, line):
        """"
        Exiting the program with EOF (ctrl+D)
        """
        return True

    def emptyline(self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()