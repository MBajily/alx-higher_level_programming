#!/usr/bin/python3

"""base model class."""
import json
import turtle
import csv


class Base:
    """Base model.

    Private Class Attributes:
        __nb_object (int): Number Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): identity of Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if (list_dictionaries is None) or (list_dictionaries == []):
            return "[]"

        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON

        Args:
            list_objs (list): list of inherited Base.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")

            else:
                l_dict = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(l_dict))


    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization

        Args:
            json_string (str): JSON of a list
        Returns:
            an empty list or the Python list represented.
        """
        if (json_string is None) or (json_string == "[]"):
            return []

        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied

        Args:
            **dictionary (dict): Key/value pairs
        """
        if dictionary and (dictionary != {}):
            if cls.__name__ == "Rectangle":
                n = cls(1, 1)

            else:
                n = cls(1)

            n.update(**dictionary)

            return n


    @classmethod
    def load_from_file(cls):
        """Return a list of classes

        Reads from `<cls.__name__>.json`.

        Returns:
            an empty list or a list of instantiated classes.
        """
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization.

        Args:
            list_objs (list): A list of inherited Base.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for object_ in list_objs:
                    writer.writerow(object_.to_dictionary())


    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes.

        Reads from `<cls.__name__>.csv`.

        Returns:
            an empty list or a list of instantiated classes.
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]

                else:
                    field_names = ["id", "size", "x", "y"]

                l_dict = csv.DictReader(csvfile, fieldnames=field_names)
                l_dict = [dict([k, int(v)] for k, v in d.items()) for d in l_dict]
                return [cls.create(**d) for d in l_dict]

        except IOError:
            return []


    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares

        Args:
            list_rectangles (list): A list of Rectangle
            list_squares (list): A list of Square
        """
        trt = turtle.Turtle()
        trt.screen.bgcolor("#b7312c")
        trt.pensize(3)
        trt.shape("turtle")

        trt.color("#ffffff")
        for rect in list_rectangles:
            trt.showturtle()
            trt.up()
            trt.goto(rect.x, rect.y)
            trt.down()

            for i in range(2):
                trt.forward(rect.width)
                trt.left(90)
                trt.forward(rect.height)
                trt.left(90)

            trt.hideturtle()

        trt.color("#b5e3d8")
        for sq in list_squares:
            trt.showturtle()
            trt.up()
            trt.goto(sq.x, sq.y)
            trt.down()

            for i in range(2):
                trt.forward(sq.width)
                trt.left(90)
                trt.forward(sq.height)
                trt.left(90)

            trt.hideturtle()

        turtle.exitonclick()
