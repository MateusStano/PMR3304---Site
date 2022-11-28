from django.contrib import admin

from .models import Album, Review, List

admin.site.register(Album)
admin.site.register(Review)
admin.site.register(List)
