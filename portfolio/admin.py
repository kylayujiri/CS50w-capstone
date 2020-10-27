from django.contrib import admin

from .models import Artist, Work, Comment, Album

# Register your models here.
admin.site.register(Artist)
admin.site.register(Work)
admin.site.register(Comment)
admin.site.register(Album)
