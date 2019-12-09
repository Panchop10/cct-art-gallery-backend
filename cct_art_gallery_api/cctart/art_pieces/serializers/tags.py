"""Art Piece Tag serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.art_pieces.models import ArtPieceTag

class ArtPieceTagModelSerializer(serializers.ModelSerializer):
    """Art Piece Tag model serializer."""

    class Meta:
        """Meta class."""

        model = ArtPieceTag
        fields = (
            'id',
            'name'
        )

        read_only_fields = ('id',)
