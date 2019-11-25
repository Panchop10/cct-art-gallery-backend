"""Art Piece models"""

# Django
from django.db import models

# Utilities
from cct_art_gallery_api.utils.models import CCTArtGalleryModel

class ArtPiece(CCTArtGalleryModel):
    """ArtPiece model."""

    likes = models.ManyToManyField(
        'users.User',
        related_name='artpieces'
    )

    category = models.ForeignKey(
        'categories.Category',
        on_delete=models.PROTECT,
        related_name='artpieces'
    )

    artist = models.ForeignKey(
        'artists.Artist',
        on_delete=models.PROTECT,
        related_name='artpieces'
    )

    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.PROTECT,
        related_name='artpieces',
        blank=True,
        null=True
    )

    name = models.CharField(
        'art piece name',
        max_length=150
    )

    description = models.TextField(
        'art piece description',
        blank=True,
        null=True,
    )

    price = models.PositiveIntegerField()

    photo = models.ImageField(
        'profile picture',
        upload_to='artists/pictures/',
        blank=True,
        null=True
    )

    status = models.BooleanField(
        'deleted',
        default=False,
        help_text=(
            'Art Piece is never deleted, his status changes to true'
        )
    )

    sold = models.BooleanField(
        'sold',
        default=False,
        help_text=(
            'Art Piece is sold'
        )
    )

    def __str__(self):
        """Return name of the art piece"""
        return self.name
