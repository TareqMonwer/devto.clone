from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User, 
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