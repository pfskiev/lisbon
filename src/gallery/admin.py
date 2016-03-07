from django.contrib import admin
from .models import Gallery


class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "text", "video"]
    list_display_links = ["video"]
    list_editable = ["text"]
    list_filter = ["video", "title"]

    search_fields = ["title", "text"]

    class Meta:
        model = Gallery


admin.site.register(Gallery)
