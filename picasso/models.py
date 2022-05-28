import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Image(models.Model):
    """Class that defines the image data fields"""
    image_file = models.ImageField(upload_to='picasso/images/')
    image_name = models.CharField(max_length=100, null=False)
    image_description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

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
    
    def update_image(self, id, image_name, image_description):
        '''method to update the selected image'''
        self.image = Image.objects.filter(pk=id).update(image_name=image_name, image_description=image_description)
        self.save_image()