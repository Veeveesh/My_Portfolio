from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length= 1000)
    subject = models.CharField(max_length=1000)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length= 1500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class Blog(models.Model):
    title = models.CharField(max_length=1000)
    Description = models.CharField(max_length=2000)
    Content = models.CharField(max_length=7000)
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=1000)
    level = models.IntegerField(default=100)

    def __str__(self):
        return self.name
