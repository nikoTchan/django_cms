from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django_cms.search.models import SearchKeyword

class SearchKeywordAdmin(admin.ModelAdmin):
  pass

admin.site.register(SearchKeyword, SearchKeywordAdmin)

class SearchKeywordInline(admin.StackedInline): #TabularInline): #
  model = SearchKeyword

class FlatPageAdminWithKeywords(FlatPageAdmin):
  inlines = [SearchKeywordInline]

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)