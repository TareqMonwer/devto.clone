from django_lifecycle import LifecycleModel, hook, AFTER_CREATE
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse_lazy


class CustomUser(AbstractUser, LifecycleModel):
    pass

    def get_absolute_url(self):
        return reverse_lazy('users:profile', args=[self.username])

    @hook(AFTER_CREATE)
    def do_after_create_jobs(self):
        try:
            Profile.objects.create(user=self)
        except Exception as e:
            print(e)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Profile Picture',
        upload_to='users/profile-pictures',
        default='users/profile-pictures/default.png'
    )
    bio = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=50,
        default="Bangladesh"
    )

    def __str__(self) -> str:
        return self.user.username
