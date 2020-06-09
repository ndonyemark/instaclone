from django.shortcuts import render, redirect
from .forms import ImageRegistrationForm, CommentsForm
from .models import Image, Comments
from django.shortcuts import get_object_or_404

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

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        search_articles = Image.search_by_caption(search_term)
        message = f'{search_term}'
        return render(request, 'search.html', {'message': message, 'search_results': search_articles})
        
    else:
        message= "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})

def single_image_details(request, image_id):
    single_image = Image.get_single_image_details(image_id)
    title = 'single image details'
    current_user = request.user
    if request.method == 'POST':
        comments_form=CommentsForm(request.POST)
        if comments_form.is_valid():
            comments = comments_form.save(commit=False)
            comments.image = single_image
            comments.posted_by = current_user
            comments.save()
            return redirect('single_image', image_id)
    else:
        comments_form=CommentsForm()
    return render(request, 'single_image.html', {'title': title, 'image': single_image, 'comments_form':comments_form})

