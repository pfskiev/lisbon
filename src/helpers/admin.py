from django.contrib import admin

from .models import GBNavigation, PTNavigation, DENavigation, Helpers

admin.site.register(PTNavigation)
admin.site.register(GBNavigation)
admin.site.register(DENavigation)
admin.site.register(Helpers)
