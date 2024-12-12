from django.contrib import admin

from blog.forms import ContactForm
from blog.models import ContactMessage

admin.site.register(ContactMessage)
