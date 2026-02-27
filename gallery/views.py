from django.shortcuts import render
from gallery.models import Photo


def index(request):
    """Страница главная"""
    photos = Photo.objects.all()
    return render(request, "gallery/index.html", context={"photos": photos})
