import unittest
from models.review import Review
from models.base_model import BaseModel
from models.review import Review


class TestReviewMethods(unittest.TestCase):
    def test_review_instance_creation(self):
        """
        Test if Review instance is created successfully.
        """
        review_instance = Review()
        self.assertIsInstance(review_instance, Review)

    def test_base_model_inheritance(self):
        """
        Test if Review class inherits from BaseModel.
        """
        review_instance = Review()
        self.assertIsInstance(review_instance, BaseModel)

    def test_review_attributes(self):
        """
        Test if Review instance has expected attributes.
        """
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, 'text'))
        self.assertTrue(hasattr(review_instance, 'user_id'))
        self.assertTrue(hasattr(review_instance, 'place_id'))


if __name__ == '__main__':
    unittest.main()
