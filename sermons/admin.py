# admin.py
from django.contrib import admin
from .models import PrayerRequest, Sermon, DailyDevotion

admin.site.register(PrayerRequest)
admin.site.register(Sermon)
admin.site.register(DailyDevotion)
