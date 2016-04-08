from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title_EN', 'description_EN']
    list_display_links = ['title_EN']
    list_editable = ['description_EN']
    # list_filter = ["updated", "timestamp"]
    search_fields = ['title_PT', 'title_EN', 'title_DE', 'description_PT']

    class Meta:
        model = Gallery

admin.site.register(Gallery, GalleryAdmin)
