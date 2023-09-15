from django.contrib import admin

from .models import Like, Rating, Comment


# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
