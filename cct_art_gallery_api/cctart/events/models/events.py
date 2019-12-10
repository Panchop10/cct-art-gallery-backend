"""Event models"""

# Django
from django.db import models

# Utilities
from cctart.utils.models import CCTArtGalleryModel
from django_extensions.db.fields import AutoSlugField

class Event(CCTArtGalleryModel):
    """Event model."""

    artpieces = models.ManyToManyField('art_pieces.ArtPiece', related_name='events')

    slug_name = AutoSlugField(populate_from='name')

    name = models.CharField(
        'event name',
        max_length=150
    )

    date = models.DateTimeField()

    description = models.TextField(
        'artist biography',
        blank=True,
        null=True,
    )

    location = models.CharField(
        'location of the event',
        max_length=255
    )

    photo = models.ImageField(
        'event banner',
        upload_to='img/events/pictures/',
        blank=True,
        null=True
    )

    finished = models.BooleanField(
        default=False,
        help_text=(
            'Tell us if a event is finished or not'
        )
    )

    deleted = models.BooleanField(
        default=False,
        help_text=(
            'Tell us if a event was deleted or not'
        )
    )

    def __str__(self):
        """Return name of the event"""
        return self.name
