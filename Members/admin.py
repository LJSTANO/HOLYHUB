from django.contrib import admin
from django.template.defaulttags import register

# Register your models here.
from .models import Slider, Service, CallToAction,Member

admin.site.register(Service)
admin.site.register (Slider)
admin.site.register (CallToAction)
admin.site.register (Member)