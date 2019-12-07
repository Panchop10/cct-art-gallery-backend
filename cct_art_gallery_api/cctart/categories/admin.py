"""Category admin."""

# Django
from django.contrib import admin

# Models
from cctart.categories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""

    list_display = (
        'slug_name',
        'name',
        'photo',
        'is_active'
    )
    search_fields = (
        'slug_name',
        'name',
    )
    list_filter = (
        'is_active',
    )

    actions = ['enable_categories', 'disable_categories']

    def enable_categories(self, request, queryset):
        """Active categories."""
        queryset.update(is_active=True)
    enable_categories.short_description = 'Make selected categories visible in the app'

    def disable_categories(self, request, queryset):
        """Disable categories."""
        queryset.update(is_active=False)
    disable_categories.short_description = 'Make selected categories hidden in the app'
