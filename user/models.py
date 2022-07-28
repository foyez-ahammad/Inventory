from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=30, null=True)
    image = models.ImageField(default='static/img/profile/profile.jpg', upload_to='static/img/profile')
    # image_url = models.CharField(max_length=3000, default='https://source.unsplash.com/640x950/?profile')
