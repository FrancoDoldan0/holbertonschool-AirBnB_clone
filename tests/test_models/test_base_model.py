import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test suite for the BaseModel class
    """

    def setUp(self):
        """
        Set up function to initialize a BaseModel instance.
        """
        self.base_model = BaseModel()

    def test_class_type(self):
        """
        Test if the instantiated object is of the correct class type.
        """
        h = BaseModel()
        self.assertEqual(h.__class__.__name__, "BaseModel")

    def test_id_uniqueness(self):
        """
        Test if each instance of BaseModel has a unique ID.
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_created_at(self):
        """
        Test if the 'created_at' attribute
        is set when BaseModel is instantiated.
        """
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_save_at(self):
        """
        Verifies that calling save method updates the 'updated_at' attribute.
        """
        base_model_instance = BaseModel()
        initial_updated_at = base_model_instance.updated_at
        base_model_instance.save()

        self.assertNotEqual(initial_updated_at, base_model_instance.updated_at)


if __name__ == '__main__':
    unittest.main()
