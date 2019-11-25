"""Artist models"""

# Django
from django.db import models

# Utilities
from cct_art_gallery_api.utils.models import CCTArtGalleryModel

class Artist(CCTArtGalleryModel):
    """Artist model."""

    first_name = models.CharField(
        'artist first name',
        max_length=30
    )

    last_name = models.CharField(
        'artist last name',
        max_length=150
    )

    biography = models.TextField(
        'artist biography',
        blank=True,
        null=True,
    )

    website = models.URLField(
        'artist website'
    )

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    address = models.CharField(
        'artist address',
        max_length=255
    )

    photo = models.ImageField(
        'profile picture',
        upload_to='artists/pictures/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        'deleted',
        default=False,
        help_text=(
            'Artist is never deleted, his status changes to true'
        )
    )

    def __str__(self):
        """Return name of the artist"""
        return self.first_name + " " + self.last_name
