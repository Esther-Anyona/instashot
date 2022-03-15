from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    prof_photo = models.ImageField(upload_to='ishots/')
    bio = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.username}'

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
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
        return f'{self.user.username}'

class Comment(models.Model):
    image = models.ForeignKey(Image,blank=True, on_delete=models.CASCADE,related_name='comment')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    comment= models.TextField()

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_image_comments(cls, id):
        comments = Comment.objects.filter(image__pk=id)
        return comments

    def __str__(self):
        return str(self.comment)



class Likes(models.Model):
    liked_by=models.ForeignKey(User, on_delete=models.CASCADE)
    image =models.ForeignKey(Image, on_delete=models.CASCADE)


