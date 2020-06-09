from django.shortcuts import render, redirect
from .forms import UserRegistration, UserUpdateForm, ProfileUpdateForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from instaapp.models import Image

def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created! You can now login")
            return redirect('profile_details')
    else:
        form = UserRegistration()
    title = 'User Registration'
    return render(request, 'users/register.html', {'form': form, 'title': title})

def profile(request):
    current_user = request.user
    user_images = Image.objects.get(posted_by = current_user)
    title = 'Profile'
    return render(request, 'users/profile.html', {'title': title, 'user_images': user_images})

def profile_setter(request):
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        profile_form = ProfileForm()
    title = 'Profile_Details'
    return render(request, 'users/profile_details.html', {'title': title, 'profile_form':profile_form})

# def update_profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, 'You have successfully updated your profile!')
#             return redirect('profile')
#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
    
#     title = 'Update'
#     return render(request, 'update_profile.html', {'u_form': u_form, 'p_form': p_form, 'title': title})