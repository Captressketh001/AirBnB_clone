#!/usr/bin/python3

import cmd
from models import base_model
from models.base_model import BaseModel
from models import storage

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
        try:
            if not line:
                raise SyntaxError()
            
            my_line = line.split(" ")
            kwargs = {}

            for i in range(1, len(my_line)):
                key, value = tuple(my_line[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace('_', " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value
            if kwargs == {}:
                obj = eval(my_line[0])()
            else:
                obj = eval(my_line[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
    


if __name__ == '__main__':
    HBNBCommand().cmdloop()
