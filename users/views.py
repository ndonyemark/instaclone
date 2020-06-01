from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created! You can now login")
            return redirect('login')
    else:
        form = UserRegistration()
    title = 'User Registration'
    return render(request, 'users/register.html', {'form': form, 'title': title})

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.Post, instance=request.user)
        p_form = ProfileUpdateForm(request.Post, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success('You have successfully updated your profile!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    title = 'Profile'
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', {'title': title}, context)
