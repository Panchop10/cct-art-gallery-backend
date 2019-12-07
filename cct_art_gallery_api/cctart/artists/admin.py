"""Artist admin."""

# Django
from django.contrib import admin

# Models
from cctart.artists.models import Artist

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Artist admin."""

    list_display = (
        'slug_name',
        'first_name',
        'last_name',
        'website',
        'email',
        'biography',
        'is_active'
    )
    search_fields = (
        'slug_name',
        'first_name',
        'last_name',
        'email',
    )
    list_filter = (
        'is_active',
    )

    actions = ['enable_artists', 'disable_artists']

    def enable_artists(self, request, queryset):
        """Active artists."""
        queryset.update(is_active=True)
    enable_artists.short_description = 'Make selected artists visible in the app'

    def disable_artists(self, request, queryset):
        """Disable artists."""
        queryset.update(is_active=False)
    disable_artists.short_description = 'Make selected artists hidden in the app'
