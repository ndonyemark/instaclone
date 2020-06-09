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
    
    @classmethod
    def get_user_images(cls, poster):
        user_images = Image.objects.filter(posted_by=poster)
        return user_images

    def __str__(self):
        return self.image_caption
    
    @classmethod
    def search_by_caption(cls, seach_term):
        news = cls.objects.filter(image)

class Comments(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    @property
    def count_comments(self):
        comments = self.comment.count()
        return comments

    @classmethod
    def get_image_comments(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments