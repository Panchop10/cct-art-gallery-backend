"""Category serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from cctart.categories.models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
    """Category model serializer."""

    class Meta:
        """Meta class."""

        model = Category
        fields = (
            'slug_name',
            'name',
            'photo',
        )

        read_only_fields = ('slug_name',)
