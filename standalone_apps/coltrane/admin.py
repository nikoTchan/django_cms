from django.contrib import admin
from coltrane.models import Category

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = { 'slug': ['title'] }
  fieldsets = [
      (None,               { 'fields': ['title', 'description'] }),
      ('More information', { 'fields': ['slug'] }),
  ]
  list_display = ('title', 'slug', 'description')
  search_fields = ['title']

admin.site.register(Category, CategoryAdmin)