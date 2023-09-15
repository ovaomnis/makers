from django.contrib import admin

from .models import Post, Comment, PostImage

# Register your models here.
class ImageInlineAdmin(admin.TabularInline):
    model = PostImage
    fields = ('image',)
    max_num = 5

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'like_count']
    list_filter = ['owner']
    search_fields = ['title']
    inlines = [ImageInlineAdmin]

    def like_count(self, obj):
        return obj.likes.count()

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass