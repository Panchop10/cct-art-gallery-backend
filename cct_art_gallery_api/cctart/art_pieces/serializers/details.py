"""Art Piece Detail serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.art_pieces.models import ArtPieceDetail

class ArtPieceDetailModelSerializer(serializers.ModelSerializer):
    """Art Piece Detail model serializer."""

    class Meta:
        """Meta class."""

        model = ArtPieceDetail
        fields = (
            'id',
            'name',
            'detail'
        )
