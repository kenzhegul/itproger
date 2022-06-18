from django.contrib import admin

from main.models import Products, Student, Comment, Profile, Advertising, Flowers, Photos

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')
    list_display_links = list_display

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = list_display

@admin.register(Flowers)
class FlowersAdmin(admin.ModelAdmin):
    list_display = ('id', 'header')
    list_display_links = list_display