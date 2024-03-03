#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
import unittest
from models import FileStorage


class TestPlaceClass(unittest.TestCase):
    def test_place_name(self):
        """
        Test for setting and getting the name attribute of Place
        """
        element = Place()
        element.name = "Tres Cruces"
        obj_key = element.__class__.__name__ + "." + element.id
        self.assertEqual(element.name, 'Tres Cruces')
        self.assertEqual
        (FileStorage._FileStorage__objects[key].name, element.name)

    def test_place_description(self):
        instance = Place()
        instance.description = "Cozy apartment"
        self.assertEqual(instance.description, "Cozy apartment")


if __name__ == '__main__':
    unittest.main()
