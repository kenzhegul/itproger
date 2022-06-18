from django.shortcuts import render
from django.template.response import TemplateResponse

from main.models import Comment, Profile, Advertising, Flowers, Photos

def index(request):
    text = Comment.objects.all()
    profile = Profile.objects.all()
    advertising = Advertising.objects.all()
    return render(request, 'main/index.html', {'text':text, 'profile':profile, 'advertising':advertising})


def about(request):
    return render(request, 'main/about.html')

def flr(request):
    flower = Flowers.objects.all()
    return render(request, 'main/flower.html', {'flower':flower})

def photo(request):
    photo = Photos.objects.all()
    return render(request, 'it/photo.html', {'photo':photo})


def msg(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, "it/msg.html", context=data)


def hdr(request):
    header = "Personal Data"
    langs = ["English", "German", "Spanish"]
    user = {"name": "Tom", "age": 23}
    addr = ("Абрикосовая", 23, 45)

    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "it/hdr.html", data)