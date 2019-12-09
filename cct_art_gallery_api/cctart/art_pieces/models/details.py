"""Art Piece Detail models"""

# Django
from django.db import models

# Utilities
from cctart.utils.models import CCTArtGalleryModel

class ArtPieceDetail(CCTArtGalleryModel):
    """ArtPieceDetail model."""

    art_piece = models.ForeignKey(
        'art_pieces.ArtPiece',
        on_delete=models.CASCADE,
        related_name='details',
    )

    name = models.CharField(
        'art piece detail name',
        max_length=50
    )

    detail = models.CharField(
        'art piece detail detail',
        max_length=100
    )

    def __str__(self):
        """Return the detail of the art piece"""
        return self.name + ": " + self.detail
