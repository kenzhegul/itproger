# Generated by Django 4.0.4 on 2022-06-16 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_flowers_price_alter_flowers_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='flowers',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]