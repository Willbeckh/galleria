import datetime
from django.test import TestCase
from django.utils import timezone

# local imports
from picasso.models import Image, Category, Location


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

    def test_was_published_recently_with_future_question(self):
        '''published_recently() method returns false for questions whose timestamp is future.'''
        time = timezone.now() + datetime.timedelta(days=30)
        ft_question = Image(pub_date=time)
        self.assertIs(ft_question.was_published_recently(), False)

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
        self.image.update_image('Dragger', 'the ziglar, kuwa changanya')
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_search_image_by_category(self):
        """Method to test the search image by category method"""
        self.image.save_image()
        images = Image.objects.filter(image_name__icontains='subaru')
        self.assertTrue(len(images) > 0)

    # TODO: test the search image by location method

class TestCategoryModel(TestCase):
    '''This class tests the category model functionality'''

    def setUp(self):
        '''method to create test data'''
        self.category = Category(name='vibes')

    def test_is_instance(self):
        '''method to test if the category instance is created'''
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        '''method to test the save category method'''
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        '''method to test the delete category method functionality'''
        self.category.save_category()
        self.category.delete_category(self.category.id)
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    def test_update_category(self):
        '''method for testing the update category method'''
        self.category.save_category()
        self.category.update_category('cool', 'vibes on vibes')
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)


class TestLocationModel(TestCase):
    '''This class tests the location model functionality'''

    def setUp(self):
        self.location = Location(name='Nairobi')

    def test_is_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def tearDown(self):
        Location.objects.all().delete()
