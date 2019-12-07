"""Category models"""

# Django
from django.db import models

# Utilities
from cctart.utils.models import CCTArtGalleryModel
from django_extensions.db.fields import AutoSlugField

class Category(CCTArtGalleryModel):
    """Category model."""

    slug_name = AutoSlugField(populate_from='name')

    name = models.CharField(
        'category name',
        max_length=50
    )

    photo = models.ImageField(
        'category photo',
        upload_to='img/categories/pictures/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Tell us if a category is active or not'
        )
    )

    def __str__(self):
        """Return name of the category"""
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
