from django.contrib import admin

from posts.models import Post, Comment

# admin.site.register(Post)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ["title" , "create", "status"]
    list_filter = ["status",]
    list_editable = ["status",]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post","name","created"]
