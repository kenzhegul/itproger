from django.urls import path
from .views import index, about, msg, hdr, flr, photo

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('flr', flr, name='flr'),
    path('msg', msg, name='msg'),
    path('hdr', hdr, name='hdr'),
    path('photo', photo, name='photo'),

]