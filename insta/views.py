from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image, Profile

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'home.html', {'images':images, 'profiles':profiles})
