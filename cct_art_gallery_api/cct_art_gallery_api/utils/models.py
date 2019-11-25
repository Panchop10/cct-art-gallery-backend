"""Django models utilities"""

#Django
from django.db import models

class CCTArtGalleryModel(models.Model):
    """CCTArtGalleryModel base model.
    CCTArtGalleryModel acts as an anstract base class from which every
    other model in the project will inherit. This class provides
    every table with the folowwing attributes:
        + created (Datetime): Store the datetime the object was created
        + modified (Datetime): Store last datetime when the object was
            modified
    """

    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified_at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
