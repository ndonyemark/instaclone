from django import forms
from .models import Image, Comments

class ImageRegistrationForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'posted_by', 'image_profile_foreign_key']
        fields = ['image_caption', 'image_name', 'image']

class CommentsForm(forms.ModelForm):
    class Meta:

        model = Comments
        exclude = ['posted_by', 'date_posted', 'image']