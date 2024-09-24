from django.db import models

# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=255,blank=False, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)


