from django.db import models

class Profile(models.Model):
    profile_photo = models.ImageField()
    profile_bio = models.TextField()

    def save_profile(self):
        return self.save()
    
    def delete_profile(self):
        return self.delete()

class Image(models.Model):
    image = models.ImageField()
    image_name = models.CharField(max_length = 40)
    image_caption = models.CharField(max_length = 20)
    image_comments = models.ManyToManyField(related_name='comment')
    image_profile_foreign_key = models.ForeignKey(on_delete=models.CASCADE)

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

class Comments(models.Model):
    comment = models.TextField()