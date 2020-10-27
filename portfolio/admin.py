from django.contrib import admin

from .models import Artist, Work, Comment, Album, Category

# Register your models here.
admin.site.register(Artist)
admin.site.register(Work)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Category)
