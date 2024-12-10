from django.contrib import admin
from .models import Slider, Service, CallToAction,Member,NewsletterSubscription

# Register your models here.
admin.site.register(Service)
admin.site.register(Slider)
admin.site.register(CallToAction)
admin.site.register(Member)
admin.site.register(NewsletterSubscription)


