from django.db import models

class Slider(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="Sliders/")
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=500)


class CallToAction(models.Model):
    title = models.CharField(max_length=255, help_text="Title of the Call to Action section")
    description = models.TextField(help_text="Description or message for the Call to Action")
    button_text = models.CharField(max_length=100, default="Call To Action", help_text="Text for the CTA button")
    link_url = models.URLField(blank=True, null=True, help_text="URL for the CTA button link")

    def __str__(self):
        return self.title

from django.db import models

class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='members/', null=True, blank=True)  # This is the ImageField

    def __str__(self):
        return self.username




# Create your models here.
