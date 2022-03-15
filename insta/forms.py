from .models import Profile,Image, Comment
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image']
