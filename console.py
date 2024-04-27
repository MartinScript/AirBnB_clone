#!/usr/bin/python3
import cmd
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    __classes = [
        "User",
        "Amenity",
        "City",
        "Review",
        "State",
        "BaseModel"
    ]

    def do_create(self, args):
        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0] + '()')
            models.storage.save()
            print(new_obj.id)

    def do_show(self, args):
        args = args.split()
        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        else:
            obj = models.storage.all()
            key = args[0] + '.' + args[1]
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        args = args.split()
        obj = models.storage.all()

        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        else:
            key = args[0] + '.' + args[1]
            if key in obj.keys():
                obj.pop(key, None)
                models.storage.save()
            else:
                print("No instance found")

    def do_all(self, args):
        args = args.split()
        obj = models.storage.all()
        new_lst = []

        if len(args) == 0:
            for key in obj.values():
                new_lst.append(key.__str__())
                print(new_lst)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for key in obj.values():
                if obj.__class__.__name__ == args[0]:
                    new_lst.append(key.__str__())
            print(new_lst)

    def do_update(self, args):
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = objects.get(key, None)

            if not obj:
                print("** no instance found **")
                return
            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_EOF(self, args):
        """Handles end of file"""
        return True

    def do_help(self, args):
        """help"""
        cmd.Cmd.do_help(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
