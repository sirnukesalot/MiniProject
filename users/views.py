from pyexpat.errors import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from blog.forms import ProfileForm
from users.forms import LoginForm
from users.models import Profile, Follow


# from users.models import Follow


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})


def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    return render(request, 'users/profile.html', {'profile_user': user, 'profile': profile})


def profile_edit(request):
    if request.method == 'POST':
        user = request.user
        profile = get_object_or_404(Profile,user=user)
        profile.bio = request.POST.get('bio',profile.bio)
        profile.profile_pic = request.FILES.get('profile_pic',profile.profile_pic)
        profile.save()
        return redirect('all_posts')
    else:
        profile = get_object_or_404(Profile,user=request.user)
    return render(request, 'users/profile_edit.html', { 'profile': profile})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', username=user.username)
        else:
            return render(request, 'users/login.html')
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('all_posts')

# @login_required
# def follow_user(request,username):
#     follow_some_user = get_object_or_404(User, username=username)
#     profile = Profile.objects.get(user=follow_some_user)
#     if request.user != follow_user:
#         Follow.objects.get_or_create(follower=request.user, following=follow_some_user)
#     return render(request, 'users/profile.html', {'profile_user': follow_some_user, 'profile': profile})
#
# @login_required
# def unfollow_user(request,username):
#     unfollow_some_user = get_object_or_404(User, username=username)
#     profile = Profile.objects.get(user=unfollow_some_user)
#     follow = Follow.objects.filter(follower=request.user, following=unfollow_some_user).first
#     if follow:
#         follow.delete()
#     return render(request, 'users/profile.html', {'profile_user': unfollow_some_user, 'profile': profile})
