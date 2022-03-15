from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.profile=User(username ='star')
        self.profile.save()
        # self.profile=Profile(user=self.user,name='rish',bio='yolo.',profile_pic='default.png')
        self.image=Image(image='default.png',image_name='crazy',image_caption='For the sake of adrenaline rush',profile=self.profile)
    def tearDown(self):

        Image.objects.all().delete()
        # Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        saved_image=Image.objects.all().delete()
        self.assertTrue((len(saved_image))>0)

    def test_delete_image(self):
        self.image.delete_image()
        deleted_image = Image.objects.all()
        self.assertTrue(len(deleted_image)==0)  