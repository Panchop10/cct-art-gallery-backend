"""User models"""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from cct_art_gallery_api.utils.models import CCTArtGalleryModel

class User(CCTArtGalleryModel, AbstractUser):
    """User model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    address = models.CharField(
        'customer address',
        max_length=255,
        blank=True,
        null=True,
    )

    photo = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    is_admin = models.BooleanField(
        'admin',
        default=False,
        help_text=(
            'Help easily distinguish users and perform queries.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text=(
            'Set to true when the user has verified its email address.'
        )
    )

    def __str__(self):
        """Return username"""
        return self.username
