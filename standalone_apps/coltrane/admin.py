from django.contrib import admin
from coltrane.models import Category, Entry

class CategoryAdmin(admin.ModelAdmin):
  prepopulated_fields = { 'slug': ['title'] }
  fieldsets = [
      (None,               { 'fields': ['title', 'description'] }),
      ('More information', { 'fields': ['slug'] }),
  ]
  list_display = ('title', 'slug', 'description')
  search_fields = ['title']

class EntryAdmin(admin.ModelAdmin):
  pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Entry, EntryAdmin)