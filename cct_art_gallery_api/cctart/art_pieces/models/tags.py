"""Art Piece Tag models"""

# Django
from django.db import models

# Utilities
from cctart.utils.models import CCTArtGalleryModel

class ArtPieceTag(CCTArtGalleryModel):
    """ArtPieceTag model."""

    art_piece = models.ForeignKey(
        'art_pieces.ArtPiece',
        on_delete=models.CASCADE,
        related_name='tags',
    )

    name = models.CharField(
        'art piece tag',
        max_length=50
    )

    def __str__(self):
        """Return name of the art piece tag"""
        return self.name
