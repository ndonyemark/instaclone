from django.shortcuts import render, redirect
from .forms import ImageRegistrationForm
from .models import Image

def index(request):
    images = Image.get_all_images()
    title = 'Home'
    return render(request, 'home.html', {'title': title, 'images': images})

def post_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form_to_be_saved = form.save(commit=False)
            form_to_be_saved.posted_by = current_user
            form_to_be_saved.save()
            return redirect('index')
    else:
        form = ImageRegistrationForm()

    title = 'post image'
    return render(request, 'post_image.html', {'title': title, 'form': form})

def single_image_details(request, image_id):
    single_image = Image.get_single_image_details(image_id)

    title = 'single image details'
    return render(request, 'single_image.html', {'title': title, 'image': single_image})


