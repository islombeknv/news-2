from django.contrib import admin

from posts.models import NewsModel, CategoryModel


@admin.register(CategoryModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']
