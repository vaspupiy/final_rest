from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        verbose_name='id'
    )
    first_name = models.CharField(
        max_length=64,
        verbose_name='first_name'
    )
    last_name = models.CharField(

        max_length=64,
        verbose_name='last_name'
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        verbose_name='email'
    )

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
