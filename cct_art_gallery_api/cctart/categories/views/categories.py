"""Categories views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Serializers
from cctart.categories.serializers import CategoryModelSerializer

# Models
from cctart.categories.models import Category

class CategoryViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Category view set."""

    serializer_class = CategoryModelSerializer
    lookup_field = 'slug_name'

    def get_queryset(self):
        """Restrict list to active-only."""

        queryset = Category.objects.all()
        if self.action == 'list':
            return queryset.filter(is_active=True)
        return queryset

    def perform_destroy(self, instance):
        """Disable artist."""
        instance.is_active = False
        instance.save()
