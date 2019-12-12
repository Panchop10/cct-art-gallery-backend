"""User serializer."""

# Django
from django.contrib.auth import password_validation

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.users.models import User
from cctart.art_pieces.models import ArtPiece
from cctart.orders.models import Order

# Serializers
from cctart.categories.serializers import CategoryModelSerializer
from cctart.artists.serializers import ArtistModelSerializer


class SingleArtPieceModelSerializer(serializers.ModelSerializer):
    """Single Art Piece model serializer."""

    category = CategoryModelSerializer(many=False)
    artist = ArtistModelSerializer(many=False)

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
            'category'
        )

        read_only_fields = ('slug_name',)


class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""


    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'address',
            'photo',
            'last_login',
            'is_admin'
        )

        read_only = ('is_admin', 'last_login', 'username')

class UserLikesViewSet(serializers.ModelSerializer):
    """User Likes model serializer."""

    category = CategoryModelSerializer(many=False)
    artist = ArtistModelSerializer(many=False)

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
            'category'
        )

class UserOrdersViewSet(serializers.ModelSerializer):
    """User Orders model serializer."""

    artpieces = SingleArtPieceModelSerializer(many=True)

    class Meta:
        """Meta class."""

        model = Order
        fields = (
            'pk',
            'date',
            'total',
            'payment_method',
            'delivered',
            'artpieces'
        )

class AddUserLikesViewSet(serializers.ModelSerializer):
    """User Likes model serializer."""

    artpiece = serializers.SlugRelatedField(
        slug_field='slug_name',
        queryset=ArtPiece.objects.filter()
    )

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'artpiece',
        )

    def create(self, data):
        """Create event with art pieces."""
        user = self.context['user']
        artpiece = data['artpiece']
        user.artpieces.add(artpiece)
        user.save()

        return artpiece


class UserSignUpModelSerializer(serializers.ModelSerializer):
    """User sign up serializer.

    Handle sign up data validation and user creation
    """

    password_confirmation = serializers.CharField(min_length=8)

    class Meta:
        """Meta class."""

        model = User
        fields = (
            'username',
            'password',
            'password_confirmation',
            'first_name',
            'last_name',
            'email',
            'address',
            'photo',
            'last_login'
        )

    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Passwords don't match.")
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        data.pop('password_confirmation')
        user = User.objects.create_user(
            **data,
            is_verified=True,
            is_admin=self.context['admin']
        )
        return user
