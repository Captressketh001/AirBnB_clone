#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    pass
    prompt = '(hbnb)'
    def do_quit(self, line):
        """
        Exiting the program with quit
        """
        return True

    def do_EOF(self, line):
        """"
        Exiting the program with EOF
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()