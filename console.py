#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
     a program called console.py that contains the entry point of the command interpreter
    """
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "Place",
        "City",
        "Amenity",
        "State",
        "Review"
    }

    def do_quit(self, line):
        """
        Exiting the program with quit
        """
        return True

    def do_EOF(self, line):
        """
        Exiting the program with EOF (ctrl+D)
        """
        print("")
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
    
    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        """
        if not line:
            print("** class name missing **")
            return
        
        my_line = line.split(" ")

        if my_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        
        if len(my_line) == 1:
            print("** instance id missing **")
            return
        
        key = "{}.{}".format(my_line[0], my_line[1])
        store = storage.all()

        if key not in store:
            print("** no instance found **")
            return

        obj = store[key]
        print(obj)

    def do_delete(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """
        if not line:
            print("** class name missing **")
            return
        # split the arguments into a list
        my_line = line.split(" ")

        if my_line[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        
        if len(my_line) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(my_line[0], my_line[1])
        store = storage.all()

        if key not in store:
            print("** no instance found **")
            return
        
        del store[key]
        storage.save()
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
