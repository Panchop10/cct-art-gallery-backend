"""Art Piece serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.art_pieces.models import ArtPiece
from cctart.art_pieces.models import ArtPieceDetail
from cctart.art_pieces.models import ArtPieceTag
from cctart.artists.models import Artist
from cctart.categories.models import Category

# Serializers
from cctart.art_pieces.serializers.details import ArtPieceDetailModelSerializer
from cctart.art_pieces.serializers.tags import ArtPieceTagModelSerializer
from cctart.categories.serializers import CategoryModelSerializer
from cctart.artists.serializers import ArtistModelSerializer

class ArtPieceModelSerializer(serializers.ModelSerializer):
    """Art Piece model serializer."""

    category = CategoryModelSerializer(many=False)
    artist = ArtistModelSerializer(many=False)

    details = ArtPieceDetailModelSerializer(many=True)
    tags = ArtPieceTagModelSerializer(many=True)

    class Meta:
        """Meta class."""

        model = ArtPiece
        fields = (
            'slug_name',
            'name',
            'description',
            'price',
            'photo',
            'artist',
            'category',
            'order',
            'details',
            'tags',
            'likes',
            'events'
        )

        read_only_fields = ('slug_name', 'likes', 'events')

class AddArtPieceModelSerializer(serializers.ModelSerializer):
    """Add Art Piece model serializer."""

    category = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Category.objects.filter()
    )
    artist = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Artist.objects.filter()
    )

    details = ArtPieceDetailModelSerializer(many=True)
    tags = ArtPieceTagModelSerializer(many=True)

    class Meta:
        """Meta class."""

        model = ArtPiece
        fields = (
            'name',
            'description',
            'price',
            'photo',
            'artist',
            'category',
            'order',
            'details',
            'tags'
        )

    def create(self, data):
        """Create art pieces with details, tags, artist."""

        details_data = data.pop('details')
        tags_data = data.pop('tags')

        art_piece = ArtPiece.objects.create(**data)

        for detail_data in details_data:
            ArtPieceDetail.objects.create(art_piece=art_piece, **detail_data)

        for tag_data in tags_data:
            ArtPieceTag.objects.create(art_piece=art_piece, **tag_data)

        return art_piece


class UpdateArtPieceModelSerializer(serializers.ModelSerializer):
    """Update Art Piece model serializer."""

    category = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Category.objects.filter(),
        required = False
    )
    artist = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=Artist.objects.filter(),
        required = False
    )

    details = ArtPieceDetailModelSerializer(many=True, required=False)
    tags = ArtPieceTagModelSerializer(many=True, required=False)

    class Meta:
        """Meta class."""

        model = ArtPiece
        fields = (
            'name',
            'description',
            'price',
            'photo',
            'artist',
            'category',
            'order',
            'details',
            'tags'
        )

    def update(self, instance, data):
        """Update art pieces."""
        art_piece = instance
        
        if 'details' in data:
            details_data = data.pop('details')
            for detail_data in details_data:
                ArtPieceDetail.objects.create(art_piece=art_piece, **detail_data)

        if 'tags' in data:
            tags_data = data.pop('tags')
            for tag_data in tags_data:
                ArtPieceTag.objects.create(art_piece=art_piece, **tag_data)

        return super(UpdateArtPieceModelSerializer, self).update(instance, data)
