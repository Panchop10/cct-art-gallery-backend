"""Category models"""

# Django
from django.db import models

# Utilities
from cct_art_gallery_api.utils.models import CCTArtGalleryModel

class Category(CCTArtGalleryModel):
    """Category model."""

    name = models.CharField(
        'category name',
        max_length=50
    )

    photo = models.ImageField(
        'category photo',
        upload_to='category/pictures/',
        blank=True,
        null=True
    )

    active = models.BooleanField(
        default=False,
        help_text=(
            'Tell us if a category is active or not'
        )
    )

    def __str__(self):
        """Return name of the category"""
        return self.name
