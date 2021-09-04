from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
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