# Generated by Django 4.0.4 on 2022-06-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='My',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='аты')),
                ('district', models.CharField(max_length=25, verbose_name='Району')),
                ('university', models.CharField(max_length=50, verbose_name='Университеттин аты')),
            ],
        ),
    ]