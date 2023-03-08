from django.contrib import admin

from posts.models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title" , "create", "status"]
    list_filter = ["status",]
    list_editable = ["status",]
