# Generated by Django 4.0.4 on 2022-05-31 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Аты')),
                ('hobby', models.TextField(verbose_name='Хоббиси')),
            ],
        ),
    ]
