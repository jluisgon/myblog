from django.contrib import admin

# Register your models here.

from .models import Tag, Entry, Category

admin.site.register(Tag)
admin.site.register(Entry)
admin.site.register(Category)

