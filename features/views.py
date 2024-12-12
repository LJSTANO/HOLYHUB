from django.shortcuts import render
from Members.models import Member

# Create your views here.
def feature_view(request):
    members = Member.objects.all()  # Get all members
    return render(request, 'features.html', {'members': members})