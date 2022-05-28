from django.test import TestCase

# local imports
from picasso.models import Image


# Create your tests here.
class TestImageModel(TestCase):
    """Class that defines the image model tests"""

    def setUp(self):
        """Method to create the test data"""
        self.image = Image(image_name='subaru',
                           image_description='subaru ya mambaru')

    def test_instance(self):
        """Method to test the instance of the image model"""
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        """Method to test the save image method"""
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        """Method to test the delete image method"""
        self.image.save_image()
        self.image.delete_selected_image(self.image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
        
    def test_update_image(self):
        """Method to test the update image method"""
        self.image.save_image()
        self.image.update_image(self.image.id, 'subaru STI', 'subaru ni mpya')
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
