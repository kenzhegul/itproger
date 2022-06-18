from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Называние')
    descriptions = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')


class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name='Студенттин аты')
    age = models.FloatField(verbose_name='Студенттин жашы')
    address = models.CharField(max_length=30, verbose_name='Адреси')
    hobby = models.CharField(max_length=50, verbose_name='Хоббиси')
    phone = models.FloatField(verbose_name='Телефон номери')

class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='Аты')
    comment = models.TextField(verbose_name='Комментарий')

class Profile(models.Model):
    name = models.CharField(max_length=20, verbose_name='Аты')
    last_name = models.CharField(max_length=25, verbose_name='Фамилиясы')
    university = models.CharField(max_length=50, verbose_name='Университеттин аты')

class Advertising(models.Model):
    header = models.TextField(verbose_name='Тема')
    name = models.CharField(max_length=100, verbose_name='Келген коноктун аты')
    data = models.CharField(max_length=30, verbose_name='Күнү, айы, сааты')
    address = models.TextField(verbose_name='Адреси')

class Flowers(models.Model):
    title = models.CharField(max_length=100, verbose_name='аты')
    header = models.TextField(verbose_name='Заголовок')
    price = models.FloatField(verbose_name='баасы')
    img = models.ImageField(upload_to='images', null=True, blank=True)


class Photos(models.Model):
    img = models.ImageField(upload_to='images', null=True, blank=True)