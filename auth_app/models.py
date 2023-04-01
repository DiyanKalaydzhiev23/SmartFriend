from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.postgres.fields import ArrayField

from SmartFriend.helpers import OPENING_TEXT
from auth_app.managers import CustomUserManager


class CustomUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'username'

    username = models.CharField(
        max_length=25,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    objects = CustomUserManager()


class Profile(models.Model):

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=50,
        default='',
        blank=True,
    )

    last_name = models.CharField(
        max_length=50,
        default='',
        blank=True,
    )

    summary_conversation = models.CharField(
        max_length=250,
        default='',
        blank=True,
    )

    current_conversation_messages = ArrayField(
        models.TextField(),
        default=[
            OPENING_TEXT
        ],
        blank=True,
    )

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
