# Generated by Django 3.2.7 on 2021-09-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='users/profile-pictures/default.png', upload_to='users/profile-pictures', verbose_name='Profile Picture'),
        ),
    ]