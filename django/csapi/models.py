from django.db import models
from django.contrib.auth.models import User

class OriginImage(models.Model):
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE)
    origin_image = models.ImageField(upload_to = 'origin_images/')

class SeparatedImage(models.Model):
    origin_image = models.ForeignKey(OriginImage, on_delete=models.CASCADE)
    separated_image = models.ImageField(upload_to = 'separated_images/')
