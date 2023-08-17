from django.contrib import admin

from .models import Category, Post, Tag

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title',)
    list_display_links = ('slug', )
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...