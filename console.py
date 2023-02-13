#!/usr/bin/python3

import cmd
from models import base_model
from models.base_model import BaseModel

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
        """
        Exiting the program with EOF (ctrl+D)
        """
        return True

    def emptyline(self):
        """
        an empty line + ENTER shouldn’t execute anything
        """
        pass
    
    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        if not line:
            print("** class name missing **")
            return
        
        line = line.split()
        class_name = line[0]

        if class_name not in base_model.classes:
            print(" ** class doesn't exist **")
            return
        obj = base_model.classes[class_name]()
        obj.save()
        print(obj.id)




if __name__ == '__main__':
    HBNBCommand().cmdloop()
