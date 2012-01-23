from django.conf import settings
from django.shortcuts import render
from django.views.generic.simple import direct_to_template
from models import Clip

def home(request):
    context = {
        'objects': Clip.objects.all(),
    }
    return render(request, 'index.html', context)

def about(request):
    return direct_to_template(request, 'about.html', {})
