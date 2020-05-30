from django import forms
from .models import Image,Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image_comment']
        fields = ['comment']

class ImageRegistrationForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'posted_by', 'image_profile_foreign_key']
        fields = ['image_caption', 'image_name', 'image']