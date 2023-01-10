from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):
    image = logoManager.objects.get(id=1)

    return render(request, "News/index.html",{
        'image': image,
    }
    )

def ads(request):
    ads = adsManager.objects.all()


    return render(request, "News/index.html",{
        'ads': ads,
    })