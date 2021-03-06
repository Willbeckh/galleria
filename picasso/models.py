import datetime
from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    '''This Class defines the category model'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Name: {self.name}"

    def save_category(self):
        '''method that saves the category'''
        self.save()

    def delete_category(self, id):
        '''method that deletes the category'''
        self.category = Category.objects.get(pk=id).delete()

    def update_category(self, id, name):
        '''method that update a particular category details'''
        try:
            self.category = Category.objects.filter(pk=id).update(name=name)
        except Exception as e:
            print('Error! unable to update category details: ', e)


class Location(models.Model):
    '''this classdefines the location model structure'''
    location_tag = models.CharField(default='Mars',
                                    max_length=50,  blank=True, unique=True)

    def __str__(self):
        return f"name: {self.location_tag}"

    def save_location(self):
        '''method that saves a location'''
        self.save()

    def delete_location(self, id):
        '''method that deletes a location tag'''
        self.location = Location.objects.get(pk=id).delete()

    def update_location(self, id, name):
        '''method that update a particular location tag'''
        try:
            self.location = Location.objects.filter(pk=id).update(location_tag=name)
        except Exception as e:
            print('Error! unable to update location details', e)


class Image(models.Model):
    """Class that defines the image data fields"""
    image_file = CloudinaryField('image')
    image_name = models.CharField(max_length=100, null=False)
    image_description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    categories = models.ManyToManyField(Category)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.image_name}"

    def was_published_recently(self):
        '''method to check if the question was published recently'''
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def save_image(self):
        '''method to save the selected image'''
        self.save()

    def delete_selected_image(self, id):
        '''method to delete the selected image'''
        try:
            self.image = Image.objects.filter(pk=id).delete()
        except Exception as e:
            print('Error: ', e)

    def update_image(self, image_name, image_description):
        '''method to update the selected image'''
        try:
            self.image = Image.objects.filter(id=self.id).update(
                image_name=image_name, image_description=image_description)
        except Exception as e:
            print("Error occured on update method: ", e)

    def search_image_by_category(self, category):
        '''method to search the image by category'''
        images = Image.objects.filter(categories__name__icontains=category)
        return images

    def filter_image_by_location(self, location):
        images = Image.objects.filter(image_location__location_tag__icontains=location)
        return images