#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def test_state_instance(self):
        instance = State()

        """Test if State instance is created successfullyi
        and inherits from BaseModel,
        and if 'name' attribute is present and initialized
        as an empty string"""
        self.assertIsInstance(instance, State)
        self.assertIsInstance(instance, BaseModel)
        self.assertTrue(hasattr(instance, 'name'))
        self.assertEqual(instance.name, "")


if __name__ == '__main__':
    unittest.main()
