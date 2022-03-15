from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment, Likes
from .forms import ProfileForm, ImageForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.objects.all()
    profiles = Profile.objects.all()
    comments = Comment.objects.all()
    likes = Likes.objects.all
    current_user = request.user
    return render(request, 'home.html', locals())

@login_required(login_url='accounts/login/')
def add_image(request):
    current_user = request.user
    images=Image.objects.all()

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            add=form.save(commit=False)
            add.profile = current_user
            add.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request,'image.html',locals())

@login_required(login_url='/accounts/login/')
def profile(request):
    images=Image.objects.all()
    current_user = request.user
    if request.method == 'POST':    
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile =form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form=ProfileForm()
    return render(request, 'profile/new_profile.html', locals())

@login_required(login_url='/accounts/login/')
def display_profile(request, id):
    userProf=User.objects.filter(id=id).first()
    profile = userProf.profile
    profile = Profile.get_by_id(id)
    images = Image.get_profile_images(id)
    user_found = User.objects.get(id=id)
    follower = len(Follow.objects.followers(user_found))
    following = len(Follow.objects.following(user_found))
    people=User.objects.all()
    people_following=Follow.objects.following(request.user)

    return render(request,'profile/profile.html',locals())

def search(request):
    profiles = User.objects.all()

    if 'username' in request.GET and request.GET['username']:
        search_term = request.GET.get('username')
        results = User.objects.filter(username__icontains=search_term)
        print(results)

        return render(request,'search_results.html',locals())
    return redirect(home)


def comment(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    profile_owner = User.objects.get(username=current_user)
    comments = Comment.objects.all()
    print(comments)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.comment_owner = current_user
            comment.save()

            print(comments)

        return redirect('home')

    else:
        form = CommentForm()
    return render(request, 'comment.html', locals())

def follow(request,user_id):
    users=User.objects.get(id=user_id)
    follow = Follow.objects.add_follower(request.user, users)

    return redirect('/profile/', locals())

def like(request, image_id):
    current_user = request.user
    image=Image.objects.get(id=image_id)
    new_like,created= Likes.objects.get_or_create(liked_by=current_user, image=image)
    new_like.save()

    return redirect('home')
