from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=10,blank=True,null=True)
    image = models.ImageField(default='default.png', upload_to='profile_pices',blank=True,null=True)
    address = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.img.path)