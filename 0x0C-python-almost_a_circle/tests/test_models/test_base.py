#!/usr/bin/python3
"""Defines unittests."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing."""

    def test_no_arg(self):
        ut1 = Base()
        ut2 = Base()
        self.assertEqual(ut1.id, ut2.id - 1)

    def test_three_bases(self):
        ut1 = Base()
        ut2 = Base()
        ut3 = Base()
        self.assertEqual(ut1.id, ut3.id - 2)

    def test_None_id(self):
        ut1 = Base(None)
        ut2 = Base(None)
        self.assertEqual(ut1.id, ut2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        ut1 = Base()
        ut2 = Base(12)
        ut3 = Base()
        self.assertEqual(ut1.id, ut3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_complex_id(self):
        self.assertEqual(complex(5), Base(complex(5)).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcefg'), Base(bytearray(b'abcefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcefg'), Base(memoryview(b'abcefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)



class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_dicts(self):
        rst1 = Rectangle(2, 3, 5, 19, 2)
        rst2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [rst1.to_dictionary(), rst2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_to_json_string_square_two_dicts(self):
        ut_s1 = Square(10, 2, 3, 4)
        ut_s2 = Square(4, 5, 21, 2)
        list_dicts = [ut_s1.to_dictionary(), ut_s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")

        except IOError:
            pass
        
        try:
            os.remove("Square.json")
        
        except IOError:
            pass
        
        try:
            os.remove("Base.json")
        
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        rst1 = Rectangle(10, 7, 2, 8, 5)
        rst2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rst1, rst2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        ut_s1 = Square(10, 7, 2, 8)
        ut_s2 = Square(8, 1, 2, 3)
        Square.save_to_file([ut_s1, ut_s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        input_list = [{"id": 89, "width": 10, "height": 4}]
        json_list = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_list)
        self.assertEqual(list, type(output_list))

    def test_from_json_string_one_rectangle(self):
        input_list = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_list)
        self.assertEqual(input_list, output_list)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_from_json_string_two_rectangles(self):
        input_list = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list = Rectangle.to_json_string(input_list)
        output_list = Rectangle.from_json_string(json_list)
        self.assertEqual(input_list, output_list)

    def test_from_json_string_one_square(self):
        input_list = [{"id": 89, "size": 10, "height": 4}]
        json_list = Square.to_json_string(input_list)
        output_list = Square.from_json_string(json_list)
        self.assertEqual(input_list, output_list)

    def test_from_json_string_two_squares(self):
        input_list = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list = Square.to_json_string(input_list)
        output_list = Square.from_json_string(json_list)
        self.assertEqual(input_list, output_list)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        rst1 = Rectangle(3, 5, 1, 2, 7)
        rst1_dictionary = rst1.to_dictionary()
        rst2 = Rectangle.create(**rst1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rst1))

    def test_create_rectangle_new(self):
        rst1 = Rectangle(3, 5, 1, 2, 7)
        rst1_dictionary = rst1.to_dictionary()
        rst2 = Rectangle.create(**rst1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rst2))

    def test_create_rectangle_is(self):
        rst1 = Rectangle(3, 5, 1, 2, 7)
        rst1_dictionary = rst1.to_dictionary()
        rst2 = Rectangle.create(**rst1_dictionary)
        self.assertIsNot(rst1, rst2)

    def test_create_rectangle_equals(self):
        rst1 = Rectangle(3, 5, 1, 2, 7)
        rst1_dictionary = rst1.to_dictionary()
        rst2 = Rectangle.create(**rst1_dictionary)
        self.assertNotEqual(rst1, rst2)

    def test_create_square_original(self):
        ut_s1 = Square(3, 5, 1, 7)
        ut_s1_dictionary = ut_s1.to_dictionary()
        ut_s2 = Square.create(**ut_s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(ut_s1))

    def test_create_square_new(self):
        ut_s1 = Square(3, 5, 1, 7)
        ut_s1_dictionary = ut_s1.to_dictionary()
        ut_s2 = Square.create(**ut_s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(ut_s2))

    def test_create_square_is(self):
        ut_s1 = Square(3, 5, 1, 7)
        ut_s1_dictionary = ut_s1.to_dictionary()
        ut_s2 = Square.create(**ut_s1_dictionary)
        self.assertIsNot(ut_s1, ut_s2)

    def test_create_square_equals(self):
        ut_s1 = Square(3, 5, 1, 7)
        ut_s1_dictionary = ut_s1.to_dictionary()
        ut_s2 = Square.create(**ut_s1_dictionary)
        self.assertNotEqual(ut_s1, ut_s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        rst1 = Rectangle(10, 7, 2, 8, 1)
        rst2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rst1, rst2])
        l_rctngls_out = Rectangle.load_from_file()
        self.assertEqual(str(rst1), str(l_rctngls_out[0]))

    def test_load_from_file_second_rectangle(self):
        rst1 = Rectangle(10, 7, 2, 8, 1)
        rst2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rst1, rst2])
        l_rctngls_out = Rectangle.load_from_file()
        self.assertEqual(str(rst2), str(l_rctngls_out[1]))

    def test_load_from_file_rectangle_types(self):
        rst1 = Rectangle(10, 7, 2, 8, 1)
        rst2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rst1, rst2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        ut_s1 = Square(5, 1, 3, 3)
        ut_s2 = Square(9, 5, 2, 3)
        Square.save_to_file([ut_s1, ut_s2])
        l_squares = Square.load_from_file()
        self.assertEqual(str(ut_s1), str(l_squares[0]))

    def test_load_from_file_second_square(self):
        ut_s1 = Square(5, 1, 3, 3)
        ut_s2 = Square(9, 5, 2, 3)
        Square.save_to_file([ut_s1, ut_s2])
        l_squares = Square.load_from_file()
        self.assertEqual(str(ut_s2), str(l_squares[1]))

    def test_load_from_file_square_types(self):
        ut_s1 = Square(5, 1, 3, 3)
        ut_s2 = Square(9, 5, 2, 3)
        Square.save_to_file([ut_s1, ut_s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        rst1 = Rectangle(10, 7, 2, 8, 5)
        rst2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rst1, rst2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        ut_s1 = Square(10, 7, 2, 8)
        ut_s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([ut_s1, ut_s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    # def test_save_to_file__csv_cls_name(self):
    #     s = Square(10, 7, 2, 8)
    #     Base.save_to_file_csv([s])
    #     with open("Base.csv", "r") as f:
    #         self.assertTrue("8,10,7,2", f.read())

    # def test_save_to_file_csv_overwrite(self):
    #     s = Square(9, 2, 39, 2)
    #     Square.save_to_file_csv([s])
    #     s = Square(10, 7, 2, 8)
    #     Square.save_to_file_csv([s])
    #     with open("Square.csv", "r") as f:
    #         self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        rst1 = Rectangle(10, 7, 2, 8, 1)
        rst2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rst1, rst2])
        l_rctngls_out = Rectangle.load_from_file_csv()
        self.assertEqual(str(rst1), str(l_rctngls_out[0]))

    def test_load_from_file_csv_second_rectangle(self):
        rst1 = Rectangle(10, 7, 2, 8, 1)
        rst2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rst1, rst2])
        l_rctngls_out = Rectangle.load_from_file_csv()
        self.assertEqual(str(rst2), str(l_rctngls_out[1]))

    def test_load_from_file_csv_rectangle_types(self):
        rst1 = Rectangle(10, 7, 2, 8, 1)
        rst2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rst1, rst2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        ut_s1 = Square(5, 1, 3, 3)
        ut_s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([ut_s1, ut_s2])
        l_squares = Square.load_from_file_csv()
        self.assertEqual(str(ut_s1), str(l_squares[0]))

    def test_load_from_file_csv_second_square(self):
        ut_s1 = Square(5, 1, 3, 3)
        ut_s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([ut_s1, ut_s2])
        l_squares = Square.load_from_file_csv()
        self.assertEqual(str(ut_s2), str(l_squares[1]))

    def test_load_from_file_csv_square_types(self):
        ut_s1 = Square(5, 1, 3, 3)
        ut_s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([ut_s1, ut_s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    # def test_load_from_file_csv_no_file(self):
    #     output = Square.load_from_file_csv()
    #     self.assertEqual([], output)

    # def test_load_from_file_csv_more_than_one_arg(self):
    #     with self.assertRaises(TypeError):
    #         Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
