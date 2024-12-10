from django.shortcuts import render, redirect
from .models import PrayerRequest, Sermon,DailyDevotion
from .forms import PrayerRequestForm

def features_page(request):
    return render(request, 'features_page.html')



def prayer_request_view(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = PrayerRequestForm()

    return render(request, 'prayer_requests.html', {'form': form})

def sermons(request):
    sermons = Sermon.objects.all()
    return render(request, 'sermon_page.html', {'sermons': sermons})

def devotions(request):
    devotions = DailyDevotion.objects.all()
    return render(request, 'devotions.html', {'devotions': devotions})

def thank_you(request):
    return render(request, 'thank_you.html')

