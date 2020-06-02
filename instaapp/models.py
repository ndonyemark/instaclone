from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='userImages')
    image_name = models.CharField(max_length = 40)
    image_caption = models.CharField(max_length = 20)
    # image_profile_foreign_key = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        return self.save()
    
    def delete_image(self):
        return self.delete()
    
    @classmethod
    def get_single_image_details(cls, image_id):
        single_image_details = Image.objects.get(id = image_id)
        return single_image_details
    
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        return all_images
    
    def __str__(self):
        return self.image_caption

class Comments(models.Model):
    comment = models.TextField()
    posted_by = models.OneToOneField(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)