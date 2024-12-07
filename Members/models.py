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


class Member(models.Model):
    username = models.CharField(max_length=100,default="Stanley", unique=True)
    email = models.EmailField(unique=True, default="default@holyhub.com")
    password = models.CharField(max_length=128, default="holyhub")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)  # Ensures that each email is unique
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when subscribed

    def __str__(self):
        return self.email

