from django.shortcuts import render
from .models import Offerings
# Create your views here.
def index(request):
    offering = Offerings.objects.all()
    context = {
        'offering': offering
    }
    return render(request, 'pages/index.html', context)