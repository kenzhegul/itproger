# Generated by Django 4.0.4 on 2022-05-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Студенттин аты')),
                ('age', models.FloatField(verbose_name='Студенттин жашы')),
                ('address', models.CharField(max_length=30, verbose_name='Адреси')),
                ('hobby', models.CharField(max_length=50, verbose_name='Хоббиси')),
                ('phone', models.FloatField(verbose_name='Телефон номери')),
            ],
        ),
    ]