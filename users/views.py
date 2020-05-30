from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegistration()
        if form.is_valid():
            form.save()
            messages.success("Account has been created! You can now login")
            return redirect('index')
    else:
        form = UserRegistration()
    title = 'User Registration'
    return render(request, 'users/register.html', {'form': form, 'title': title})
