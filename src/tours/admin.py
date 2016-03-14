from django.contrib import admin

from .models import Tour, About, Paragraph, Category

admin.site.register(Tour)
admin.site.register(About)
admin.site.register(Category)
admin.site.register(Paragraph)
