from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='ishots/')
    image_name = models.CharField(max_length=50)
    image_caption = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def save_image(self):
        """
        Method to save images
        """
        self.save()

    def delete_image(self):
        """
        Method to delete image
        """
        self.delete()

    def __str__(self):
        return self.image_name

class Profile(models.Model):
    prof_photo = models.ImageField(upload_to='ishots/')
    bio = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.bio