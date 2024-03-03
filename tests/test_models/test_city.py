from models.base_model import BaseModel
from models.city import City
import unittest
from models import FileStorage


class TestCityStorage(unittest.TestCase):
    def test_city_name_saved_in_storage(self):
        """
        Test if the name of the city is correctly saved in the storage.
        """
        city_instance = City()
        city_instance.name = "Paso de los Toros"

        self.assertEqual(city_instance.name, "Paso de los Toros")

        storage_k = f"{city_instance.__class__.__name__}.{city_instance.id}"
        city_in_storage = FileStorage._FileStorage__objects.get(storage_k)
        self.assertIsNotNone(city_in_storage)
        self.assertEqual(city_in_storage.name, city_instance.name)


if __name__ == '__main__':
    unittest.main()
