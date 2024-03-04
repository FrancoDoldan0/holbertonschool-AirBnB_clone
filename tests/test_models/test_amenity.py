import unittest
from models.amenity import Amenity
from amenity import Amenity


class Amenity_Test(unittest.TestCase):
    """
    Tests for Amenity class
    """
    def setUp(self):
        """Set up function."""
        self.amenity = Amenity()

    def test_attributes_existence(self):
        """Test for attributes existence."""
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_is_string(self):
        """Test if id is a string."""
        self.assertIsInstance(self.amenity.name, str)

    def test_default_name(self):
        """Test if the default name is set properly."""
        self.assertEqual(self.amenity.name, "default_name")

    def test_update_name(self):
        """Test if the name attribute can be updated."""
        self.amenity.name = "new_name"
        self.assertEqual(self.amenity.name, "new_name")


if __name__ == '__main__':
    unittest.main()
