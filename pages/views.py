from django.shortcuts import render
from django.http import HttpResponse
from pics.models import pic


def home_view(request, *args, **kwargs):
    return render(request, "home.html",{})


def gallery(request, *args, **kwargss):
    pic_count = pic.objects.count()
    pictures =[]
    for i in range(2, pic_count+1):
        this_obj = pic.objects.get(id=i)
        pictures.append (this_obj)
    gallery_context = {'pictures' : pictures}
    return render(request, "gallery.html", gallery_context)

def about(request, *args, **kwargs):
    return render(request, "about.html",{})

def contact(request, *args, **kwargs):
    return render(request, "contact.html",{})

